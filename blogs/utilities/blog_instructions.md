# How to make a blog post

Create a blog post in the posts-md directory as a markdown file. Save the file as yyyy-mm-dd.md. 

the blog_template.html file is a boilerplate for all blog posts.

run:

```
python3 md_to_html.py
```

This should convert each blog post into an html file with the boilerplate code. Then, run:

```
python3 blogs-list_generate.py
```

This creates a list of blog posts that the `blog.html` file can access to list.