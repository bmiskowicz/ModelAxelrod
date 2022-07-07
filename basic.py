import random


graphSize = 1000
features = 10



class Drawables:    
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




def updateValues():
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

    Drawables.iterations=Drawables.iterations+1
    
    #getting interaction with some probability if they have at least one same feature
    if(numberOfDifferences>0 and numberOfDifferences<features):
        Drawables.iterations=Drawables.iterations+1
        randomNumber=random.randint(0, 99)
        if(randomNumber<(100/features)*(features-numberOfDifferences)):
                        
            #getting random different feature
            feature=differencesList[random.randint(0, numberOfDifferences-1)]

            #changing the actor's feature
            Drawables.actors[actual][feature]=Drawables.actors[actual+neighbour][feature]

            #changing the actor's group if their features are the same 
            if(Drawables.actors[actual]==Drawables.actors[actual+neighbour]):
                Drawables.actorsGroups[actual]=Drawables.actorsGroups[actual+neighbour]
                
                #ending the simulation if all actors have the same values
                x=0
                for x in range(99):
                    if (Drawables.actors[0] != Drawables.actors[x]): 
                        break
                else:
                    Drawables.bloop=0
                    print(Drawables.iterations)


    

    


Drawables = Drawables()
Actors()
while(Drawables.bloop):
    updateValues()