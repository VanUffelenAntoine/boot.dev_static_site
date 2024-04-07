from htmlnode import ParentNode
from inline_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading  = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list" 

def markdown_to_blocks(markdown):
    blocks= markdown.split('\n\n')
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")
    
    if block.startswith(('# ','## ','### ','#### ', '##### ')):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    return block_type_paragraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_html_node(block))
    return ParentNode('div',children)

def block_to_html_node(block):
    type = block_to_block_type(block)
    if type == block_type_quote:
        return block_to_html_quote(block)
    if type == block_type_unordered_list:
        return block_to_html_ulist(block)
    if type == block_type_ordered_list:
        return  block_to_html_olist(block)
    if type == block_type_code:
        return block_to_html_code(block)
    if type == block_type_heading:
        return block_to_html_heading(block)
    if type == block_type_paragraph:
        return block_to_html_paragraph(block)
    raise ValueError("Invalid block type")

def block_to_html_quote(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def block_to_html_list(listTag, labelLen, block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[labelLen:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode(listTag, html_items)

def block_to_html_ulist(block):
    return block_to_html_list('ul', 2, block)
def block_to_html_olist(block):
    return block_to_html_list('ol', 3, block)

def block_to_html_code(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def block_to_html_heading(block):
    amount_of_hashtags = block.split(' ')[0].count('#')
    return ParentNode(f'h{amount_of_hashtags}', text_to_children(block.lstrip(r'#{1,5}\ ?')))

def block_to_html_paragraph(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    return ParentNode('p', text_to_children(paragraph))

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(node.text_node_to_html_node())
    return children