from textnode import (
    TextNode,    
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,)
from inline_markdown import (split_nodes_delimiter,)

def main():
    print("# hello world")
    node = TextNode("This is text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    print(new_nodes)
main()