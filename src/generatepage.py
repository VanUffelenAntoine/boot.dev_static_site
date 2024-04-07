import os
from markdown_blocks import markdown_to_blocks, markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path}, to {dest_path} using {template_path}')
    markdown = open(from_path).read()
    template = open(template_path).read()
    title = extract_title(markdown)

    new_html = template.replace('{{ Title }}', title).replace('{{ Content }}', markdown_to_html_node(markdown).to_html())

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    html_file = open(dest_path, 'w+')
    html_file.write(new_html)

    print(f'Generated page from {from_path}, to {dest_path} using {template_path}')

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    for dir in os.listdir(dir_path_content):
        if dir.rfind('.md') >= 0:
            generate_page(os.path.join(dir_path_content, dir), template_path, os.path.join(dest_dir_path, dir.rstrip('.md') + '.html'))
        else:
            print(f'Not found at {dir}')
            generate_page_recursive(os.path.join(dir_path_content, dir + '/'), template_path, os.path.join(dest_dir_path, dir + '/'))