import numpy as np
import math as m
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

size = 1500
samples = 8
debug = False
maxDist = 3000
temp = {}
sensorDict = {}
senddingDict = {"number of nodes": samples}

colors = ["blue","red","green","yellow"]
#Generate Points

x = np.random.rand(samples) * size
y = np.random.rand(samples) * size
z = np.random.rand(samples) * size

#Generate plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

 
#Entering Points

ax.scatter(x,y,z, color='cyan')

for j in range(samples):
    sensorDict = {}
    detector = np.array([x[j], y[j], z[j]])
    temp = {"height":detector[1]}
    sensorDict.update(temp)
    for i in range(samples):
        if j != i:
        #Calculate Distance
    
            totalDistance = 0
            dX = abs(detector[0] - x[i])
            if debug:
                print(dX) 

            dY = abs(detector[1] - y[i])
            
            if debug:
                print(dY)
            
            dZ = abs(detector[2] - z[i])
            if debug:
                print(dZ)

            #Pythagoras Calculations
            dZX = m.sqrt(pow(dZ,2)+pow(dX,2))
            if debug:
                print("dZX value:",dZX)

            totalDistance = m.sqrt(pow(dZX,2)+pow(dY,2))
            if totalDistance <= maxDist:
                temp = {i: totalDistance}
                sensorDict.update(temp)
                senddingDict[j] = sensorDict


                

print(json.dumps(senddingDict, indent=4, separators=(",", ": ")))

with open('outputs/distanceList.txt',"w") as outfile:
    json.dump(senddingDict,outfile, indent=4, separators=(",", ": "))
    print("File created")   

#Show Plot
plt.show()


