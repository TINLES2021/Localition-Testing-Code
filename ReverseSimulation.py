import math as m
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



with open('outputs/distanceList.txt') as json_file:
    data = json.load(json_file)
print(json.dumps(data, indent=4, separators=(",", ": ")))

convertedDistances = {}
        
nrOfNodes= data['number of nodes'] # nrOfNodes get send first so we can use that knowledge.
print(nrOfNodes)
for i in range(nrOfNodes):
    node = data[str(i)]
    valueDict = {}
    for keys in node: 
        if keys == "height":
            a = {}
            a = node['height']
        else:
            dZ = abs(a - data[keys]['height'])
            recalcDistance = m.sqrt(pow(node[keys],2)-pow(dZ,2))
            temp = {keys:recalcDistance}
            valueDict.update(temp)
    convertedDistances[str(i)] = valueDict        
print(json.dumps(convertedDistances, indent=4, separators=(",", ": ")))

for i in range(nrOfNodes):
    mainNode = convertedDistances[str(i)] #Create Node to use as base
    mainIndexList = list(mainNode.keys()) #Create list to index trough values
    
    a = mainNode.get(mainIndexList[0]) #first value in main dict
    b = mainNode.get(mainIndexList[1]) #second value in main dict
    
    secondNode = convertedDistances.get(mainIndexList[2]) #Checking node created to form triangle
    secondIndexList = list(secondNode.keys())
    
    c = secondNode.get(secondIndexList[1])
    ang_c = m.acos((pow(a,2) + pow(b,2) - pow(c,2))/(2*a*b))

    d  = mainNode.get(mainIndexList[2])
    e  = secondNode.get(secondIndexList[2])
    ang_e = m.acos((pow(b,2) + pow(d,2) - pow(e,2))/(2*b*d))
    print("a=",a,"b=",b,"c=",c,"d=",d,"e=",e)

    node1pos = [0,0]
    node2pos = []
    node3pos = []
    node4pos = []
    node2pos.insert(0,a)
    node2pos.insert(1,0)
    

    node3pos.insert(0, b * m.cos(ang_c))
    node3pos.insert(1, b * m.sin(ang_c))

    node4pos.insert(0, d * m.cos((ang_c + ang_e))) 
    node4pos.insert(1, d * m.sin((ang_c + ang_e))) 



    plt.scatter([node1pos[0],node2pos[0],node3pos[0],node4pos[0]], 
    [node1pos[1],node2pos[1],node3pos[1],node4pos[1]])
    plt.show()
