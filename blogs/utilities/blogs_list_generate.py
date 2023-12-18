from pathlib import Path
from datetime import datetime
import json

# source folder for blog posts in html 
blogs_folder_path = Path("/home/raghav/raghavthakar.net/blogs/posts-html")
# target folder for json for the blog posts list
json_folder_path  = Path("/home/raghav/raghavthakar.net/blogs/utilities/")
# json filename
json_file = 'blogs_list.json'

# Get a list of all html blog files in theposts-html folder
blog_file_list = [file.name for file in blogs_folder_path.iterdir() if file.is_file()]

json_dict = {}
for blog_file in blog_file_list:
    print(blog_file)

    # make sure the file is an html file
    try:
        if blog_file[-5:] != '.html':
            raise NameError
    
    except NameError:
        print("Couldn't process ", blog_file, ", the file format is incompatible.")
        continue
    
    # if the file is html, starting characters are the date
    blog_date_str = blog_file[:-5]
    print(blog_date_str)

    json_dict[blog_date_str] = 'blogs/posts-html/' + blog_file

print(json_dict)

# Serializing json
json_object = json.dumps(json_dict, indent=4)
# Writing to json
with open(str(json_folder_path.absolute()) + '/' + json_file, "w") as outfile:
    outfile.write(json_object)