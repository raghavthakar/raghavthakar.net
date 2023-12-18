import markdown
from pathlib import Path
import re
import frontmatter

# source folder of project posts in markdown
md_parent_folder_path = Path("projects/posts-md")

# target folder for project posts in html 
html_parent_folder_path = Path("projects/posts-html")

# project template file
template_file = Path("projects/utilities/project_template.html")

# Get a list of all markdown files in the md files folder
md_file_list = [file.name for file in md_parent_folder_path.iterdir() if file.is_file()]

# Get the contents of the html template by opening the file
with open(template_file) as t_f:
    template_content = t_f.read()

# Print the list of files
for md_file in md_file_list:
    print(md_file)

    # make sure the file is a markdown file
    try:
        if md_file[-3:] != '.md':
            raise NameError
    
    except NameError:
        print("Couldn't process ", md_file, ", the file format is incompatible.")
        continue
    
    # access the file and store its contents
    # access the file and store its contents
    with open(str(md_parent_folder_path.absolute()) + '/' + md_file, "r") as md_f:
        md_metadata = frontmatter.load(md_f)
    
    # get the filename of the md_file without the extension
    # this is the date of the project
    project_date_in_words = md_file[:-3]
    # the tags of the project
    project_tags = md_metadata.get("tags", [])
    
    # convert this text into html using the markdown package
    try:
        html_text = markdown.markdown(md_metadata.content)
    except Exception as exception:
        print("Couldn't convert file contents to Markdown: ", exception)
    
    # find the regex match, and the actual tag, and the data to insert
    project_file_content = re.sub('<\s*div\s+id\s*=\s*"project-content"\s*>', '<div id="project-content">'+html_text, template_content)
    # repeat that for the project date
    project_file_content = re.sub('<\s*div\s+id\s*=\s*"publish-date"\s*>', '<div id="publish-date">Published (yyyy/mm/dd): '+str(project_date_in_words), project_file_content)
    # repeat that for the project tags
    project_file_content = re.sub('<\s*div\s+id\s*=\s*"project-tags"\s*>', '<div id="project-tags">Tags: '+str(project_tags), project_file_content)

    with open(str(html_parent_folder_path.absolute()) + '/' + (project_date_in_words + '.html'), 'w') as project_file:
        project_file.write(project_file_content)

print("Conversions complete.")
