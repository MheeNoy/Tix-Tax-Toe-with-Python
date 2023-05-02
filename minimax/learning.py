import math


def minimax(curDepth, nodeIndex, maxTurn, scores, targerDepth ):
    print
    if(curDepth == targerDepth):
        return scores[nodeIndex]
    print
    if(maxTurn):
        return max(minimax(curDepth + 1,nodeIndex * 2, False,scores,targerDepth), 
                   minimax(curDepth + 1 ,nodeIndex * 2 + 1
                           , False, scores,targerDepth)) 
        return
    
    
    else :
        return min(minimax(curDepth + 1,nodeIndex * 2,True,scores,targerDepth),
                   minimax(curDepth + 1 ,nodeIndex * 2 + 1
                           , True, scores,targerDepth)) 

scores = [23,11,12,25,23,33,10,55]
#11 23 7 16
#23 16
#16

treeDepth = math.log(len(scores) ,2)
print(treeDepth)
print ("The optimal value is : ", end ="")
print (minimax(0,0,True,scores,treeDepth))