import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.animation
import random

graphSize = 10
nodeSize = 3000/graphSize
features=5

G = nx.Graph()

fig, ax = plt.subplots(figsize=(10,10))

class Drawables:    
    iterations=0

    #Nodes colors - default (should be empty)
    redNodes = []
    orangeNodes = []
    yellowNodes = []
    greenNodes = []
    oliveNodes = []

    #Edges colors - default (should be empty)
    redEdges = []
    orangeEdges = []
    yellowEdges = []
    greenEdges = []
    oliveEdges = []
    blackEdges = []

    #groups features - default (should be empty)
    redGroups = []
    orangeGroups = []
    yellowGroups = []
    greenGroups = []
    oliveGroups = []

    #actors and their features
    actors = [[0]*features]*(graphSize*graphSize)
    actorsGroups = [0]*(graphSize*graphSize)

    def __init__(self):
        #defining groups
        Drawables.redGroups = [random.randint(0,9) for _ in range(features)]

        Drawables.orangeGroups = [random.randint(0,9) for _ in range(features)]
        numberOfDifferences = 0
        for i in range(features):
            if(Drawables.orangeGroups[i]!=Drawables.redGroups[i]):
                numberOfDifferences=numberOfDifferences+1
        while numberOfDifferences==0 or numberOfDifferences==features:
            Drawables.orangeGroups = [random.randint(0,9) for _ in range(features)]
            numberOfDifferences = 0
            for i in range(features):
                if(Drawables.orangeGroups[i]!=Drawables.redGroups[i]):
                    numberOfDifferences=numberOfDifferences+1


        Drawables.yellowGroups = [random.randint(0,9) for _ in range(features)]
        numberOfDifferences = 0
        for i in range(features):
            if(Drawables.orangeGroups[i]!=Drawables.yellowGroups[i]):
                numberOfDifferences=numberOfDifferences+1
        while Drawables.yellowGroups==Drawables.redGroups or numberOfDifferences==0 or numberOfDifferences==features:
            Drawables.yellowGroups = [random.randint(0,9) for _ in range(features)]
            numberOfDifferences = 0
            for i in range(features):
                if(Drawables.orangeGroups[i]!=Drawables.yellowGroups[i]):
                    numberOfDifferences=numberOfDifferences+1


        Drawables.greenGroups = [random.randint(0,9) for _ in range(features)]
        numberOfDifferences = 0
        for i in range(features):
            if(Drawables.greenGroups[i]!=Drawables.yellowGroups[i]):
                numberOfDifferences=numberOfDifferences+1
        while Drawables.greenGroups==Drawables.redGroups or Drawables.greenGroups==Drawables.orangeGroups or numberOfDifferences==0 or numberOfDifferences==features:
            Drawables.greenGroups = [random.randint(0,9) for _ in range(features)]
            numberOfDifferences = 0
            for i in range(features):
                if(Drawables.greenGroups[i]!=Drawables.yellowGroups[i]):
                    numberOfDifferences=numberOfDifferences+1


        Drawables.oliveGroups = [random.randint(0,9) for _ in range(features)]
        numberOfDifferences = 0
        for i in range(features):
            if(Drawables.greenGroups[i]!=Drawables.oliveGroups[i]):
                numberOfDifferences=numberOfDifferences+1
        while Drawables.oliveGroups==Drawables.redGroups or Drawables.oliveGroups==Drawables.orangeGroups or Drawables.oliveGroups==Drawables.yellowGroups or numberOfDifferences==0 or numberOfDifferences==features:
            Drawables.oliveGroups = [random.randint(0,9) for _ in range(features)]
            numberOfDifferences = 0
            for i in range(features):
                if(Drawables.greenGroups[i]!=Drawables.oliveGroups[i]):
                    numberOfDifferences=numberOfDifferences+1


def Actors():
    #defining actors features values
    i=0
    for i in range(graphSize*graphSize):
        actorGroup = random.randint(1, 5)
        if(actorGroup==1):   Drawables.actors[i] = Drawables.redGroups.copy()
        elif(actorGroup==2): Drawables.actors[i] = Drawables.orangeGroups.copy()
        elif(actorGroup==3): Drawables.actors[i] = Drawables.yellowGroups.copy()
        elif(actorGroup==4): Drawables.actors[i] = Drawables.greenGroups.copy()
        elif(actorGroup==5): Drawables.actors[i] = Drawables.oliveGroups.copy()
        Drawables.actorsGroups[i] = actorGroup

#Main function
def updatePlot():
    ## Clear plot
    ax.clear()
    
    ## Plot size
    pos = [graphSize*graphSize]

    ## Create plot
    i = 0
    labeldict = {}
    G.clear_edges()
    for x in range(graphSize):
        for y in range(graphSize):
            labeldict[i]=''.join(str(e) for e in Drawables.actors[i])
            G.add_node(i, pos = (x+1, y+1))

            if y < graphSize-1: 
                
                numberOfDifferences=0
                j=0
                for j in range(features):
                    if(Drawables.actors[i][j]!=Drawables.actors[i+1][j]):
                        numberOfDifferences=numberOfDifferences+1

                if(numberOfDifferences>0 and numberOfDifferences<features): G.add_edge(i,i+1, weight=8.7)

            if x < graphSize-1:
                
                numberOfDifferences=0
                j=0
                for j in range(features):
                    if(Drawables.actors[i][j]!=Drawables.actors[i+graphSize][j]):
                        numberOfDifferences=numberOfDifferences+1

                if(numberOfDifferences>0 and numberOfDifferences<features): G.add_edge(i,i+graphSize, weight=4.7)
            i = i+1

    pos=nx.get_node_attributes(G,'pos')

    #set new nodes
    Drawables.redNodes = []
    Drawables.orangeNodes = []
    Drawables.yellowNodes = []
    Drawables.greenNodes = []
    Drawables.oliveNodes = []

    i=0
    for i in range(graphSize*graphSize):
        if(Drawables.actorsGroups[i]==1):    Drawables.redNodes.append(i)
        elif (Drawables.actorsGroups[i]==2): Drawables.orangeNodes.append(i)
        elif (Drawables.actorsGroups[i]==3): Drawables.yellowNodes.append(i)
        elif (Drawables.actorsGroups[i]==4): Drawables.greenNodes.append(i)
        elif (Drawables.actorsGroups[i]==5): Drawables.oliveNodes.append(i)
    
    ## Color Nodes
    nx.draw_networkx(G, pos, node_size = nodeSize, with_labels=False)
    nx.draw_networkx_nodes(G, pos, nodelist=Drawables.redNodes, node_size = nodeSize, node_color="red")
    nx.draw_networkx_nodes(G, pos, nodelist=Drawables.orangeNodes, node_size = nodeSize, node_color="orange")
    nx.draw_networkx_nodes(G, pos, nodelist=Drawables.yellowNodes, node_size = nodeSize, node_color="yellow")
    nx.draw_networkx_nodes(G, pos, nodelist=Drawables.greenNodes, node_size = nodeSize, node_color="green")
    nx.draw_networkx_nodes(G, pos, nodelist=Drawables.oliveNodes, node_size = nodeSize, node_color="olive")
    ## Labels
    nx.draw_networkx_labels(G, pos,  labels=labeldict, font_size=6, font_color="black")

    ## Color edges
    nx.draw_networkx_edges(G, pos, edgelist=Drawables.redEdges,alpha=0.5, width=6, edge_color="red")
    nx.draw_networkx_edges(G, pos, edgelist=Drawables.orangeEdges,alpha=0.5, width=6, edge_color="orange")
    nx.draw_networkx_edges(G, pos, edgelist=Drawables.yellowEdges,alpha=0.5, width=6, edge_color="yellow")
    nx.draw_networkx_edges(G, pos, edgelist=Drawables.greenEdges,alpha=0.5, width=6, edge_color="green")
    nx.draw_networkx_edges(G, pos, edgelist=Drawables.oliveEdges,alpha=0.5, width=6, edge_color="olive")
    nx.draw_networkx_edges(G, pos, edgelist=Drawables.blackEdges,alpha=0.5, width=6, edge_color="black")

#In this function you should write your code!
def updateValues(num):
    #getting random actor
    actual = random.randint(0, graphSize*graphSize-1)

    #checking what neighbours he has
    avaliable=[]
    if(actual>graphSize-1): avaliable.append(-graphSize)
    if(actual<graphSize*(graphSize-1)): avaliable.append(graphSize)
    if(actual%graphSize>0): avaliable.append(-1)
    if(actual%graphSize<graphSize-1): avaliable.append(1)

    #getting random neighbour
    neighbour=random.choice(avaliable)

    #counting different features
    i=0
    differencesList=[]
    numberOfDifferences = 0
    for i in range(features):
        if(Drawables.actors[actual][i]!=Drawables.actors[actual+neighbour][i]):
            differencesList.append(i)
            numberOfDifferences=numberOfDifferences+1

    #getting interaction with some probability if they have at least one same feature
    if(numberOfDifferences>0 and numberOfDifferences<features):
        Drawables.iterations=Drawables.iterations+1
        print(Drawables.iterations)
        randomNumber=random.randint(0, 99)
        j=0
        if(randomNumber<(100/features)*(features-numberOfDifferences)):
            #showing the interaction
            Drawables.redEdges = []
            Drawables.orangeEdges = []
            Drawables.yellowEdges = []
            Drawables.greenEdges = []
            Drawables.oliveEdges = []

            if(Drawables.actorsGroups[actual+neighbour]==1): Drawables.redEdges = [(actual, actual+neighbour)]
            elif(Drawables.actorsGroups[actual+neighbour]==2): Drawables.orangeEdges = [(actual, actual+neighbour)]
            elif(Drawables.actorsGroups[actual+neighbour]==3): Drawables.yellowEdges = [(actual, actual+neighbour)]
            elif(Drawables.actorsGroups[actual+neighbour]==4): Drawables.greenEdges = [(actual, actual+neighbour)]
            elif(Drawables.actorsGroups[actual+neighbour]==5): Drawables.oliveEdges = [(actual, actual+neighbour)]
            
            #getting random different feature
            feature=differencesList[random.randint(0, numberOfDifferences-1)]

            #changing the actor's feature
            Drawables.actors[actual][feature]=Drawables.actors[actual+neighbour][feature]

            #changing the actor's group if their features are the same 
            if(Drawables.actors[actual]==Drawables.actors[actual+neighbour]): Drawables.actorsGroups[actual]=Drawables.actorsGroups[actual+neighbour]
            

    updatePlot(num)
    
#Main function
def main(num):
    updateValues(num)


Drawables = Drawables()
Actors()

ani = matplotlib.animation.FuncAnimation(fig, main, interval=0.1, repeat=False)
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()