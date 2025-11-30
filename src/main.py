from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://wwww.bot.dev")
    print(node)

main()