#this functions would enable us to visualize our tree.
from node import *
from copy import deepcopy

#temp=[]


def print_tree(Root_Obj, array):            #This is function is used to create an array of TRUE lead nodes
    temp = array

    for i in Root_Obj.children:
        # print("NODE : ",Root_Obj)
        # print("ARC_VAL : ", Root_Obj.arc_label[Root_Obj.children.index(i)])
        # print("CHILD_LABEL : ", i)
        # print("____________________________")
        #temp.append(Root_Obj)
        if(i.label=="True"):
            # print("I in printtree",i)
            temp.append(i)
            # print("TEMP ",temp)
        print_tree(i, temp)
        #return temp
    return temp

def cal_Path(i, curr_path):              #Function to calculate the path from a given true node to the root.
    tempPath = curr_path

    # if(i.upArc!="UNKNOWN"):
    #     tempPath.append(i.upArc)
    # if(i.parent!=Root.parent):
    #     cal_Path(i.parent, Root)

    if i.upArc != "UNKNOWN":
        tempPath.append(i.upArc)
        cal_Path(i.parent, tempPath)

    return tempPath


    # print(i.upArc)
    return tempPath

def makeAnd(a,b):
    return "and("+a+", "+b+")"

def makeOr(a,b):
    return "or("+a+", "+b+")"

def andFunc(andlist): #Creates an "and" representation of a list of rules
    andString=""
    if (len(andlist) == 1):
        andString = andlist[0]
    else:
        andString = andlist[0]
        for i in range(1, len(andlist)):
            andString= makeAnd(andString, andlist[i])

    return andString


def orFunc(orlist):     #Creates an "OR" representation of a list of rules
    orString = ""
    if (len(orlist) == 1):
        orString = orlist[0]
    else:
        orString = orlist[0]
        for i in range(1, len(orlist)):
            orString = makeOr(orString, orlist[i])

    return orString



