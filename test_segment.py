from node import *
from segment import *

node1 = Node("A", 0, 0)
node2 = Node("B", 1, 1)
node3 = Node("C", 2, 0)
segment1 = Segment ("AB", node1, node2)
segment2 = Segment ("BC", node2, node3)
print (node1)
print (node2)
print (node3)
print (segment1.dest.coordx)
print (segment2)
