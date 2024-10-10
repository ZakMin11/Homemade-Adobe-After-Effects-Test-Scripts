import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

def cleanUp(liz ):
    l = liz
    for i in liz:
        if i == '' or i == ',' or i == 0:
            liz.remove(liz[i])
    return liz

def getTotal(lines):
    tot = 0
    for i in lines:
        if i[:-2] == '':
            break
        else:   
            tot +=float(i[:-2]) 
    return tot

def removeSmall(indList, x):
    k=2
    while k < len(indList):
    #    print(x[indList[k]],x[indList[k-1]])#,x[indList[k-2]])
        three = x[indList[k]] - x[indList[k-1]] #- x[indList[k-2]]
        threeList = [x[indList[k]], x[indList[k-1]]]
    #    print(three)
        if abs(three) < 10:
            #print("HELLO")
            
            indList.remove(min(threeList))
            #indList.remove(indList.index()) #, x[indList[i-2]]])))
            #print(indList)
            #indList.remove(indList.index(min([x[indList[k]] , x[indList[k-1]]]))) #, x[indList[i-2]]])))
            #print(indList)
        k+=1

def plotInd(indList):
    for i in range(len(indList)):
        plt.plot(x[indList[i]],y[indList[i]], marker="*", markersize=15)
        #plt.plot(x,y, scalex=True, scaley=True, data=None, marker=’marker style’, **kwargs)

def writeOutput(indList):
    with open('/Users/zakmineiko/Documents/framesBK.txt', 'w') as out:
        for li in range(len(indList)):
            out.write(str(indList[li]))
            if li != len(indList):
                out.write('\n')

with open('/Users/zakmineiko/Documents/audioData.txt') as f:
    lines = f.readlines()
#print(len(lines[0]))

fig, ax = plt.subplots(figsize=(15, 7.5))

kiz = []

for i in lines:
    kiz.append(i)

kiz = cleanUp(kiz)

#cleanUp(indList)
num = []
ind = 0
indList = []
x = []
y= [0]
secondInd = 0
secondTot = 0

cleanList = cleanUp(lines)

tot  = getTotal(cleanList)
ave = tot/len(cleanList)
#print(ave)
for i in cleanList:
    if float(i)> ave:
        secondTot+=float(i)
        secondInd+=1
    


aveAr = np.empty(300, dtype=int) # for y values bar 
aveAr.fill(ave)

secondAve = secondTot/secondInd
secondAveAr = np.empty(300, dtype=int) # for y values of bar
secondAveAr.fill(secondAve)
#print(secondAve)
def findSpikes(l):
    retlist = []
    ind = 0
    for i in l:
        findMaxOf = [l[ind], l[ind+1], i]
        retlist.append(max(findMaxOf))
    return retlist



    #return list of floats that are apex compared to the maybe four 

aboveSecondAve = []
for i in cleanList:
    if float(i)  > secondAve:
        aboveSecondAve.append(float(i))
#print(aboveSecondAve)
hiv = findSpikes(aboveSecondAve)
#print(hiv)


print("lern of list: ", cleanList[90])
print("lern of hiv: ", float(cleanList[90]))
ionKnow = removeSmall(indList, x)
why = []
for i in range(len(cleanList)):
    why.append(i)#ax.plot(why, cleanList)
#ax.plot()
#plt.show()

#plt.plot(indList,len(indList), marker="*", markersize=15)


for i in range(len(indList)):
    #print(indList[i])
    # x.append(indList())
    if y[indList[i]] > secondAve:
        #print(y[indList[i]])
        plt.plot(x[hiv[i]],y[indList[i]], marker="*", markersize=15)
        #maxList.append(x[indList[i]])
 
#for i in range(len(maxList)):
        
#print(y)
#print(indList)
#line = ax.plot(x,y,lw=2)
#aveLine = ax.plot(x,aveAr,lw=2)
#ave2Line = ax.plot(x,secondAveAr,lw=2)
#print(aveAr)
#ax.plot()
#plt.show()


