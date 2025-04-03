import matplotlib.pyplot as plt
from node import *
from segment import *
class Graph:
    def __init__(self):
        self.nodes=[]
        self.segments=[]

def AddNode (g, n):
    if n in g.nodes:
        return False
    else:
        g.nodes.append(n)
        return True

def AddSegment (g, nombre, nameOriginNode,nameDestinationNode):
    i=0
    j=0
    encontrado1=False
    encontrado2=False
    while i<len(g.nodes) and not encontrado1:
        if nameOriginNode==g.nodes[i].name:
            origen=g.nodes[i]
            encontrado1=True
        else:
            i=i+1
    while j < len(g.nodes) and not encontrado2:
        if nameDestinationNode==g.nodes[j].name:
            destino=g.nodes[j]
            encontrado2=True
        else:
            j=j+1
    seg=Segment(nombre,origen,destino)
    g.segments.append(seg)
    if destino not in origen.neighbors:
        origen.neighbors.append(destino)
    if encontrado1==False or encontrado2==False:
        return False
    if encontrado1==True and encontrado2==True:
        return True

def GetClosest(g,x,y):
    i=0
    n1 = Node('punto', x, y)
    cercano=g.nodes[0]
    menordist=Distance(g.nodes[0],n1)

    while i<len(g.nodes):
        dist=Distance(g.nodes[i],n1)
        if dist<menordist:
            cercano=g.nodes[i]
            menordist=dist
        i=i+1
    print(f'El más cercano es: {cercano.name} (Coord x= {cercano.coordx}, Coord y={cercano.coordy})')

def Plot(g):
    i=0
    plt.grid(color='red', linestyle='dashed', linewidth=0.5)
    plt.title('Versión 1')
    plt.xlabel('Coordenada x')
    plt.ylabel('Coordenada y')
    while i<len(g.nodes):
        plt.plot(g.nodes[i].coordx,g.nodes[i].coordy, marker='o', color='r', markersize=6)
        plt.text(g.nodes[i].coordx+0.1,g.nodes[i].coordy+0.1,g.nodes[i].name,fontsize=10, color='g', weight='bold')
        i=i+1
    j=0
    while j<len(g.segments):
        plt.arrow(g.segments[j].orig.coordx,g.segments[j].orig.coordy,g.segments[j].dest.coordx-g.segments[j].orig.coordx,
                  g.segments[j].dest.coordy-g.segments[j].orig.coordy, head_width=0.05, head_length=0.05, fc='b', ec='b')
        midx=(g.segments[j].orig.coordx+g.segments[j].dest.coordx)/2
        midy = (g.segments[j].orig.coordy + g.segments[j].dest.coordy) / 2
        plt.text(midx,midy,round(g.segments[j].cost,3),fontsize=10, color='black', weight='bold')
        j=j+1


def PlotNode(g,nameOrigin):
    i=0
    encontrado=False
    while i<len(g.nodes) and not encontrado:
        if nameOrigin==g.nodes[i].name:
            nodoorigen=g.nodes[i]
            encontrado=True
        i=i+1

    plt.grid(color='red', linestyle='dashed', linewidth=0.5)
    plt.title('Versión 1')
    plt.xlabel('Coordenada x')
    plt.ylabel('Coordenada y')

    k = 0
    while k < len(g.nodes):
        plt.plot(g.nodes[k].coordx, g.nodes[k].coordy, marker='o', color='grey', markersize=6)
        plt.text(g.nodes[k].coordx+0.1, g.nodes[k].coordy+0.1, g.nodes[k].name, fontsize=10, color='black', weight='bold')
        k = k + 1

    plt.plot(nodoorigen.coordx,nodoorigen.coordy, marker='o', color='b', markersize=6)

    j=0
    while j<len(nodoorigen.neighbors):
        plt.plot(nodoorigen.neighbors[j].coordx,nodoorigen.neighbors[j].coordy,marker='o', color='g', markersize=6)
        j=j+1

    m=0
    while m<len(nodoorigen.neighbors):
        segneighbor=Segment(f'segmento{m}neighbor',nodoorigen,nodoorigen.neighbors[m])
        plt.arrow(segneighbor.orig.coordx,segneighbor.orig.coordy,(segneighbor.dest.coordx-segneighbor.orig.coordx),
                  (segneighbor.dest.coordy-segneighbor.orig.coordy),head_width=0.05, head_length=0.05, fc='r', ec='r')
        m=m+1
        medx=(segneighbor.orig.coordx+segneighbor.dest.coordx)/2
        medy=(segneighbor.orig.coordy+segneighbor.dest.coordy)/2
        plt.text(medx+0.05,medy-0.05,round(segneighbor.cost,3),fontsize=10, color='black', weight='bold')


    if encontrado==False:
        return False
    if encontrado==True:
        return True