import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link, 
)
from htmlnode import LeafNode
from inline_markdown import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        self.assertEqual(
            split_nodes_delimiter([node], "`", text_type_code),
            [
               TextNode("This is text with a ", text_type_text),
               TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ]
        )

    def test_delim_code_double(self):
        node = TextNode("This is text `code block` with a `code block` word", text_type_text)
        self.assertEqual(
            split_nodes_delimiter([node], "`", text_type_code),
            [
               TextNode("This is text ", text_type_text),
               TextNode("code block", text_type_code),
               TextNode(" with a ", text_type_text),
               TextNode("code block", text_type_code),
               TextNode(" word", text_type_text),
            ]
        )
    
    def test_delim_bold(self):
        node = TextNode("This is text **bold block** with a word", text_type_text)
        self.assertEqual(
            split_nodes_delimiter([node], "**", text_type_bold),
            [
               TextNode("This is text ", text_type_text),
               TextNode("bold block", text_type_bold),
               TextNode(" with a word", text_type_text),
            ]
        )
    
    def test_delim_bold_double(self):
        node = TextNode("This is text **bold block** with a **bold block** word", text_type_text)
        self.assertEqual(
            split_nodes_delimiter([node], "**", text_type_bold),
            [
               TextNode("This is text ", text_type_text),
               TextNode("bold block", text_type_bold),
               TextNode(" with a ", text_type_text),
               TextNode("bold block", text_type_bold),
                TextNode(" word", text_type_text),
            ]
        )


    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()