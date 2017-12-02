class Node:


    def __init__(self, label):
        self.label = label
        self.arc_label = []
        self.children = []          #Obj
        self.parent=""
        self.matrix = []
        self.upArc=""


    def __str__(self):
        return str(self.label)

    def add_child(self,obj):
        self.children.append(obj)

    def get_node(self,label):
        return Node(label=label)
