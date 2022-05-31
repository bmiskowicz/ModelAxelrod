import random


graphSize = 30
features = 100



class Drawables:    
    #wb = xw.Book('axelrod.xlsx')  
    #sheet1 = wb.sheets['actors']
    #sheet2 = wb.sheets['groups']
    bloop=1
    iterations=0

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
        while numberOfDifferences==0 or numberOfDifferences==5:
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
        while Drawables.oliveGroups==Drawables.redGroups or Drawables.oliveGroups==Drawables.orangeGroups or Drawables.oliveGroups==Drawables.yellowGroups or numberOfDifferences==0 or numberOfDifferences==5:
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



#In this function you should write your code!
def updateValues():
    #Drawables.blackEdges[0] = (Drawables.blackEdges[0][0] + 1, Drawables.blackEdges[0][1] + 1)
    #getting random actor
    actual = random.randint(0, 99)

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
        #Drawables.sheet1.range(Drawables.iterations+1).value =
        #string= ','.join(str(item) for item in Drawables.actorsGroups)
        #Drawables.sheet2.range(Drawables.iterations+1).value = list2
        Drawables.iterations=Drawables.iterations+1
        randomNumber=random.randint(0, 99)
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
            if(Drawables.actors[actual]==Drawables.actors[actual+neighbour]):
                Drawables.actorsGroups[actual]=Drawables.actorsGroups[actual+neighbour]
                
        #ending the simulation after some interations
        if(Drawables.iterations==100000000):
            print("działam")
            klastry=[]
            x=0
            for groupNr in range(1,6):
                notSeen=list(range(graphSize*graphSize))
                while(notSeen):
                    actuals=[]
                    actuals.append(notSeen[0])
                    cluster=0
                    while(actuals):
                        x=actuals[0]
                        if(Drawables.actorsGroups[x]==groupNr):
                            cluster=cluster+1
                            if(x>9): 
                                if((x-graphSize)in notSeen):
                                    if(Drawables.actorsGroups[x-graphSize]==groupNr):  actuals.append(x-graphSize)
                                    notSeen.remove(x-graphSize)

                            if(x<90):
                                if((x+graphSize)in notSeen):
                                    if(Drawables.actorsGroups[x+graphSize]==groupNr):  actuals.append(x+graphSize)
                                    notSeen.remove(x+graphSize)
                            if(x%graphSize>0):
                                if((x-1)in notSeen):
                                    if(Drawables.actorsGroups[x-1]==groupNr):  actuals.append(x-1)
                                    notSeen.remove(x-1)
                            if(x%graphSize<graphSize-1):
                                if((x+1)in notSeen):
                                    if(Drawables.actorsGroups[x+1]==groupNr):  actuals.append(x+1)
                                    notSeen.remove(x+1)
                            
                        actuals.remove(x)
                        if(x in notSeen): notSeen.remove(x)
                        if not actuals: 
                            if(cluster>0):  klastry.append(cluster)
            print(klastry)
            x=0
            y=0
            for x in range(graphSize):
                lista=[]
                for y in range(graphSize):
                    lista.append(Drawables.actorsGroups[x*graphSize+y])
                print(lista)
            Drawables.bloop=0
                                                      

    

    


Drawables = Drawables()
Actors()
while(Drawables.bloop):
    updateValues()