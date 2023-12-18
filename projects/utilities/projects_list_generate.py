from pathlib import Path
from datetime import datetime
import json

# source folder for project posts in html 
projects_folder_path = Path("projects/posts-html")
# target folder for json for the project posts list
json_folder_path  = Path("projects/utilities/")
# json filename
json_file = 'projects_list.json'

# Get a list of all html project files in theposts-html folder
project_file_list = [file.name for file in projects_folder_path.iterdir() if file.is_file()]

json_dict = {}
for project_file in project_file_list:
    print(project_file)

    # make sure the file is an html file
    try:
        if project_file[-5:] != '.html':
            raise NameError
    
    except NameError:
        print("Couldn't process ", project_file, ", the file format is incompatible.")
        continue
    
    # if the file is html, starting characters are the date
    project_date_str = project_file[:-5]
    print(project_date_str)

    json_dict[project_date_str] = 'projects/posts-html/' + project_file

print(json_dict)

# Serializing json
json_object = json.dumps(json_dict, indent=4)
# Writing to json
with open(str(json_folder_path.absolute()) + '/' + json_file, "w") as outfile:
    outfile.write(json_object)