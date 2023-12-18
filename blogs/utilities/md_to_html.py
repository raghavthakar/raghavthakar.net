import markdown
from pathlib import Path
import re

# source folder of blog posts in markdown
md_folder_path    =                     Path("/home/raghav/raghavthakar.net/blogs/posts-md")
# target folder for blog posts in html 
html_folder_path  =                   Path("/home/raghav/raghavthakar.net/blogs/posts-html")
# blog template file
template_file     = Path("/home/raghav/raghavthakar.net/blogs/utilities/blog_template.html")

# Get a list of all markdown files in the md files folder
md_file_list = [file.name for file in md_folder_path.iterdir() if file.is_file()]

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
    with open(str(md_folder_path.absolute()) + '/' + md_file, "r") as md_f:
        md_text = md_f.read()
    
    # get the filename of themd_file without the extension
    # this is the date of the blog
    blog_date_in_words = md_file[:-3]
    
    # convert this text into html using the markdown package
    try:
        html_text = markdown.markdown(md_text)
    except Exception as exception:
        print("Couldn't convert file contents to Markdown: ", exception)
    
    # find the regex match, and the actual tag, and the data to insert
    blog_file_content = re.sub('<\s*div\s+id\s*=\s*"blog-content"\s*>', '<div id="blog-content">'+html_text, template_content)
    # repeat that for the blog date
    blog_file_content = re.sub('<\s*div\s+id\s*=\s*"publish-date"\s*>', '<div id="publish-date">Published (yyyy/mm/dd): '+str(blog_date_in_words), blog_file_content)

    # write the contents into a blog post file with the date as the name
    with open(str(html_folder_path.absolute()) + '/' + blog_date_in_words + '.html', 'w') as blog_file:
        blog_file.write(blog_file_content)

print("Conversions complete.")
