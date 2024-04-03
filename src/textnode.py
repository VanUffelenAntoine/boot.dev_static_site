from htmlnode import LeafNode
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:

    def __init__(self,text,text_type,url = ""):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self,target):
        return self.text == target.text and self.text_type == target.text_type and self.url == target.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self):
        tag = None
        props = None
        if self.text_type == text_type_bold:
            tag = 'b'
        elif self.text_type == text_type_italic:
            tag = 'i'
        elif self.text_type == text_type_code:
            tag = 'code'
        elif self.text_type == text_type_link:
            tag = 'a'
            props = {"href" : self.url}
        elif self.text_type == text_type_image:
            tag = 'img'
            props = {"src": self.url, "alt": self.text}
        else:
            raise Exception('text_type does not match options')
        return LeafNode(tag, self.text, props)
    
def split_nodes_delimiter(old_nodes, deliminet, text_type):
    
    return ""