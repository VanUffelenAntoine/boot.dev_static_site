import os
from markdown_blocks import markdown_to_blocks, markdown_to_html_node


def extract_title(markdown):
    title = markdown.split('\n')[0]

    if not title.startswith('# '):
        raise Exception('Every page needs a title')
    return title.lstrip('# ')

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path}, to {dest_path} using {template_path}')
    markdown = open(from_path).read()
    template = open(template_path).read()
    title = extract_title(markdown)

    new_html = template.replace('{{ Title }}', title).replace('{{ Content }}', markdown_to_html_node(markdown).to_html())

    dest_dir_path = dest_path[:dest_path.rfind('/')]
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    
    html_file = open(dest_path, 'w+')
    html_file.write(new_html)

    print(f'Generated page from {from_path}, to {dest_path} using {template_path}')
    return new_html

def main():
    markdown = '''
# Introduction

This series, a cornerstone of what I, in my many years as an **Archmage**, have come to recognize as the pinnacle of imaginative creation, stands unrivaled in its depth, complexity, and the sheer scope of its _legendarium_. As we embark on this exploration, let us delve into the reasons why this monumental work is celebrated as the finest in the world.
'''
    generate_page('./content/index.md','./template.html','./public/index.html')


main()