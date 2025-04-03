from graph import *
from node import *
from segment import *

g=Graph()
n1=Node('nodo1', 1, 2)
n2=Node('nodo2',3,4)
AddNode(g,n1)
AddNode(g,n2)
AddSegment(g, 'segmento1','nodo1','nodo2')
print(g.segments[0].cost)

GetClosest(g,0,0)
PlotNode(g,'nodo1')