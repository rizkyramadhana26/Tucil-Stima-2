from numpy import argmin,argmax,cross,arccos,clip,dot
from numpy.linalg import norm

def myConvexHull(points):
    #return list of lines that shape the convex hull
    #line is a pair of integer [a,b]. a and b are index of the points that shape the line
    rows = len(points)
    minAbsis=argmin(points,0)[0]
    maxAbsis=argmax(points,0)[0]
    p1 = points[minAbsis]
    pn = points[maxAbsis]

    above = [i for i in range(0,rows) if aboveLine(p1[0],p1[1],pn[0],pn[1],points[i][0],points[i][1])==1]
    below = [i for i in range(0,rows) if aboveLine(p1[0],p1[1],pn[0],pn[1],points[i][0],points[i][1])==-1]

    hullAbove=convexHullAbove(points,above,[minAbsis,maxAbsis])
    hullBelow=convexHullAbove(points,below,[maxAbsis,minAbsis])
    result=hullAbove + hullBelow
    return result
    
def convexHullAbove(points,indexes,line):
    #return list of lines that shapes the convex hull at the left of the line
    rows = len(indexes)
    if rows==0 : #basis
        return [[line[0],line[1]]]
    elif rows==1: #basis
        return [[line[0],indexes[0]],[indexes[0],line[1]]]
    else : #reccurence
        next = getNextPoint(points,indexes,[points[line[0]],points[line[1]]])
        left=[]
        right=[]
        for index in indexes :
            isAbove=aboveLine(points[line[0]][0],points[line[0]][1],points[next][0],points[next][1],points[index][0],points[index][1])
            if isAbove==1 : 
                left+=[index]

        for index in indexes :
            isAbove=aboveLine(points[next][0],points[next][1],points[line[1]][0],points[line[1]][1],points[index][0],points[index][1])
            if isAbove==1 :
                right+=[index]

        #divide to two regions and solve each of them
        leftConvexHull = convexHullAbove(points,left,[line[0],next])
        rightConvexHull = convexHullAbove(points,right,[next,line[1]])

        #combine
        result=leftConvexHull+rightConvexHull
        return result

def getNextPoint(points,indexes,line): #indexes have two elements at least
    #return the furthest point from a line. If several points have same distance, will return the point that maximize the angle formed
    maxDistance=-1
    maxIndex=0
    for index in indexes:
        distance = calculateDistance(points[index],line)
        if  distance > maxDistance :
            maxDistance=distance
            maxIndex=index
        elif distance==maxDistance :
            maxIndex=getMaxAngle(points,index,maxIndex,line)   
    return maxIndex

def calculateDistance(point,line) :
    return norm(cross(line[1]-line[0], line[0]-point)) / norm(line[1]-line[0])

def getMaxAngle(points,index,maxIndex,line):
    p=line[1]-line[0]
    q=points[index]-line[0]
    r=points[maxIndex]-line[0]
    angle1=arccos(clip(dot(p,q)/norm(p)/norm(q),-1,1))
    angle2=arccos(clip(dot(p,r)/norm(p)/norm(r),-1,1))
    if angle1>angle2 :
        return index
    else :
        return maxIndex

def aboveLine(x1,y1,x2,y2,x3,y3):
    param = (x1*y2+x3*y1+x2*y3) - (x3*y2+x2*y1+x1*y3)
    if param>0:
        return 1 #x3,y3 located above line
    elif param<0:
        return -1 #x3,y3 located below line
    else :
        return 0 #x3,y3 located in line