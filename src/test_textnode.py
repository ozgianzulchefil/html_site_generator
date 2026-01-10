import unittest

from textnode import TextNode, TextType
from main import text_node_to_html_node

# My implementation
# class TestTextNode(unittest.TestCase):
#     def test_eq(self):
#         node = TextNode("This is a text node", TextType.BOLD)
#         node2 = TextNode("This is a text node", TextType.BOLD)
#         self.assertEqual(node, node2)
    
#     def test_not_eq(self):
#         node = TextNode("This is a text node", TextType.BOLD)
#         node2 = TextNode("This is anotest text node", TextType.BOLD)
#         self.assertNotEqual(node, node2)
    
#     def test_url_none(self):
#         node = TextNode("This is a text node", TextType.BOLD)
#         node2 = TextNode("This is a text node", TextType.CODE)
#         self.assertNotEqual(node, node2)

# Solution implementation 

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, text, https://www.boot.dev)", repr(node))

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_textbold(self):
        node = TextNode("THIS IS A BOLD TEXT NODE", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "THIS IS A BOLD TEXT NODE")

    def test_textlink(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props["href"], "https://www.boot.dev")

    def test_textimage(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "https://www.boot.dev")
        self.assertEqual(html_node.props["alt"], "This is a text node")


if __name__ == "__main__":
    unittest.main()