class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError ("Subclasses must implement this method")

    # def props_to_html(self):
    #     return {
    #         if self.props == None:
    #             return ""
    #         self.props
    #     }

    # Solution implemented below
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
            
        return props_html

    # def __repr__(self):
    #     print(HTMLNode)
    # Solution implemented below
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("the tag does not exist")
        if self.children is None:
            raise ValueError("children property is missing")
        children_html = ""
        for child in self.children:
            children_html = children_html + child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"