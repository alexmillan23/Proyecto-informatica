from node import *
class Segment:
    def __init__(self,name,orig_Node,dest_Node):
        self.name=name
        self.orig=orig_Node
        self.dest=dest_Node
        self.cost=self.CalcCost()
    def CalcCost(self):
        return (((self.dest.coordx-self.orig.coordx)**2+(self.dest.coordy-self.orig.coordy)**2)**0.5)