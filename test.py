import math
import random

from new_eleusis_new import *
from node import *
#from create_tree import *
#from b_scientist import *
from copy import deepcopy
from create_tree import *
from atomic_rule import *
from generate_rule import *

current_rule = ""
attribute_matrix = []
attribute_dict = {}
label_dict = {}

card_labels = []

first_round = True

previous2 = ""
previous1 = ""
current = ""

cards_seen = []

board_state = []

info_gain = 0
entropy_dict = {}

seenFalse=False

FinalRule=""

""" GLOBAL"""
cardsLastThree =[]
cardsCount=0
boardState1=[]
scoreCard=0


def update_card_to_boardState(card):            # Updates the recent three cards played
    #cardsLastThree = []
    global cardsLastThree
    if len(cardsLastThree) == 3:
        cardsLastThree= cardsLastThree[:2]
        cardsLastThree.append(card)
    else:
         cardsLastThree.append(card)
    # print("cardsLastThree ",cardsLastThree)
    update_BoardState(card)
    return 0

def update_BoardState(card_Played,val_Card):        #Updates the actual board state
    """
    Returns current board state
    Input: Card played and its value
    Output: Board state
    """
    global cardsCount, boardState1, scoreCard
    cardsCount+=1
    # print (cardsCount)
    temp_State=[]
    boardLen=len(boardState1)
    # print(boardLen)

    #temp_Correct=temp_State[0]
    #temp_Incorrect_State=temp_State[1]
    if boardLen == 0 or boardLen == 1 or boardLen == 2:
        boardState1.append((card_Played,[]))
    else:
        temp_State = boardState1[boardLen - 1]
        if (val_Card == False):
            temp_State[1].append(card_Played)
            boardState1[boardLen-1]=temp_State
            #temp_Incorrect_State.append(card_Played)
            #player.boardstate[boardLen-1]=(temp_Correct,temp_Incorrect_State)
            #player.correctCards.append(current)
            #scoreCard+=2
        elif (val_Card == True):
            boardState1.append((card_Played,[]))
        else:
            print("Error: Played card is not valid")
    #print(boardState1)

    # print("boardState : ", boardState1)


"""CODE ENDSSs"""


def score():                    #Calculates the scores for our player
    global scoreCard
    for i in range(4, len(attribute_matrix) - 1, 4):
        if (attribute_matrix[i][len(attribute_matrix[i]) - 1] == True):
            scoreCard += 1
        elif (attribute_matrix[i][len(attribute_matrix[i]) - 1] == False):
            scoreCard += 2
    return scoreCard

'''BOARD STATE STARTS'''
def my_BoardState(board,card,result):               #Calls update_BoardState to update the boardstate
    global previous2, previous1, current, first_round, seenFalse
    # print(board)

    if first_round == True:
        # print("first")
        previous2 = board[0]
        previous1 = board[1]
        current = board[2]
        # print(previous2, previous1, current)


        card_labels.append(True)
        card_labels.append(True)
        card_labels.append(True)



        update_BoardState(previous2, True)
        update_BoardState(previous1, True)
        update_BoardState(current, True)

        evaluate(previous2, True)
        cards_seen.append(previous2)

        evaluate(previous1, True)
        cards_seen.append(previous1)

        evaluate(current, True)
        cards_seen.append(current)

        evaluate(card, result)
        cards_seen.append(card)
        update_BoardState(card, result)

        if result == True:
            previous2 = previous1
            previous1 = current
            current = card

        # print("first round is no longer true")
        first_round = False
        #print("if: ", card)


    else:
        #print("else: ", card)
        # print("subsequent")
        cards_seen.append(card)
        evaluate(card, result)

        if result == True:
            previous2 = previous1
            previous1 = current
            current = card
        if(result==False):
            seenFalse=True

        update_BoardState(card, result)



'''BOARD STATE ENDS'''






def entropyB(list_CardAttributes):          #Calculates the entropy and gives the attribiute with max gain
    global attribute_dict1
    global label_dict1

    attribute_dict1 = {'VALUE': 0, 'COLOR': 1, 'SUIT': 2, 'E/O': 3, 'ROYAL': 4, 'VAL_P': 5,
                       'SUIT_P': 6, 'CARD_P': 7}
    # attribute_dict1 = {'value' : 0, 'color' : 1, 'suit' : 2, 'even/odd' : 3, 'royal' : 4, 'val_p': 5,
    #                  'suit_p' : 6, 'card_p' : 7}
    label_dict1 = {'VALUE': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'], 'COLOR': ['R', 'B'],
                   'SUIT': ['C', 'D', 'H', 'S'], 'E/O': ['even', 'odd'], 'ROYAL': ['royal', '!royal'],
                   'VAL_P': ['IV', 'DV', 'DIV', 'IDV', 'EV'], 'SUIT_P': ['IS', 'DS', 'DIS', 'IDS', 'ES'],
                   'CARD_P': ['IC', 'DC', 'DIC', 'IDC', 'EC']}

    # label_dict1 = {'value': ['1','2','3','4','5','6','7','8','9','10','11','12','13'] , 'color': ['R', 'B'], 'suit': ['C', 'D', 'H', 'S'], 'even/odd': ['even', 'odd'], 'royal': ['royal', '!royal'],
    #            'val_p': ['IV', 'DV', 'DIV', 'IDV', 'EV'], 'suit_p': ['IS', 'DS', 'DIS', 'IDS', 'ES'], 'card_p': ['IC', 'DC', 'DIC', 'IDC', 'EC']}

    options = ['VALUE', 'COLOR', 'SUIT', 'E/O', 'ROYAL', 'VAL_P',
               'SUIT_P', 'CARD_P']

    temp_CardAttributes = list_CardAttributes
    # options = ['value','color','suit','even/odd','royal','val_p','suit_p','card_p']
    value1 = 0
    color1 = 0
    suit1 = 0
    evenodd1 = 0
    royal1 = 0
    val_p1 = 0
    suit_p1 = 0
    card_p1 = 0
    count_InstancesDictionary = {}
    entropy_dictionary = {}
    entropy_Calculator = 0
    best_pick = "NONE"

    for i in list_CardAttributes[0]:
        for j in range(len(options)):
            if i == 'VALUE':
                value1 = +1
            if i == 'COLOR':
                color1 = +1
            if i == 'SUIT':
                suit1 = +1
            if i == 'E/O':
                evenodd1 = +1
            if i == 'ROYAL':
                royal1 = +1
            if i == 'VAL_P':
                val_p1 = +1
            if i == 'SUIT_P':
                suit_p1 = +1
            if i == 'CARD_P':
                card_p1 = +1
    # print(value1,color1,suit1,evenodd1,royal1,val_p1,suit_p1,card_p1)

    # print(value,)

    count_Attributes = len(list_CardAttributes[0])
    count_Cards = len(list_CardAttributes)
    for k in options:
        if k == 'VALUE':
            continue
            if value1 == 0:
                continue
        if k == 'COLOR':
            if color1 == 0:
                continue
        if k == 'SUIT':
            if suit1 == 0:
                continue
        if k == 'E/O':
            if evenodd1 == 0:
                continue
        if k == 'ROYAL':
            if royal1 == 0:
                continue
        if k == 'VAL_P':
            if val_p1 == 0:
                continue
        if k == 'SUIT_P':
            if suit_p1 == 0:
                continue
        if k == 'CARD_P':
            if card_p1 == 0:
                continue

        attibutes_Options = label_dict1[k]
        # print (attibutes_Options)
        for m in range(0, count_Cards):
            for n in temp_CardAttributes[m]:
                # print (n)
                for l in range(0, len(attibutes_Options)):
                    if m == 0:
                        count_InstancesDictionary.update({attibutes_Options[l]: [0, 0, 0]})
                    if n == attibutes_Options[l]:
                        # print (m,n,l)
                        count_InstancesDictionary[attibutes_Options[l]][0] = \
                        count_InstancesDictionary[attibutes_Options[l]][0] + 1
                        if temp_CardAttributes[m][len(temp_CardAttributes[m]) - 1] == True:
                            count_InstancesDictionary[attibutes_Options[l]][1] = \
                            count_InstancesDictionary[attibutes_Options[l]][1] + 1
                        else:
                            count_InstancesDictionary[attibutes_Options[l]][2] = \
                            count_InstancesDictionary[attibutes_Options[l]][2] + 1

    # print("11111:",count_InstancesDictionary)
    for a in options:
        if a == 'VALUE':
            continue
        sum_Value = 0
        temp_Value = []
        for b in label_dict1[a]:
            # print (b)
            if b in count_InstancesDictionary:
                temp_Value.append(count_InstancesDictionary[b])
                attribute_val = b
            else:
                continue
        # print (temp_Value)
        if label_dict1[a][0] not in count_InstancesDictionary:
            continue
        total_Values = len(temp_Value)
        for c in range(0, total_Values):
            sum_Value += temp_Value[c][0]
            # print(sum_Value)
        for d in range(0, total_Values):
            if temp_Value[d][0] is not 0:
                temp_Val2 = round((temp_Value[d][1] / temp_Value[d][0]), 2)
                temp_Val3 = round((temp_Value[d][2] / temp_Value[d][0]), 2)
                temp_Val1 = round((temp_Value[d][0] / sum_Value), 2)
            else:
                continue
            # print (temp_Val1,temp_Val2,temp_Val3)
            if temp_Val1 == 0 or temp_Val2 == 0 or temp_Val3 == 0:
                # best_pick='True'
                entropy_Calculator = 0
            else:
                entropy_Calculator += round(
                    (-(temp_Val1) * (temp_Val2 * (math.log(temp_Val2, 2)) + temp_Val3 * (math.log(temp_Val3, 2)))), 2)

                # print(d,entropy_Calculator)
        entropy_dictionary.update({a: entropy_Calculator})
        # print(entropy_dictionary)
    entropy_sorted = sorted(entropy_dictionary.items(), key=lambda t: t[1])  # list of tuples
    # print("entropy::",entropy_sorted)
    # print(entropy_dictionary)
    # if best_pick == "NONE":
    best_pick = entropy_sorted[0][0]

    # print(best_pick)
    # best_pick = entropy_sorted[0][0]
    return best_pick

def possible_values(j, matrix):             #It returns the possible values for an attribute  from attribute_matrix
    temp2=[]
    t = matrix[0]
    # print("matrix[0]:, ", matrix[0])
    # print()

    index = t.index(j)
    # print("looking for: ", index)

    for i in matrix[1:]:
        for j in range(0, len(i)):
        # if(x[new_i] not in temp2):
        #     temp2.extend(x[new_i])
            if j == index:
                if i[j] not in temp2:
                    temp2.append(i[j])

    return temp2

def exclude(remove, val, attribute_mat1):           #Creates the sub matrix from the excluded value of a particular matrix
    temp=[]
    copy = deepcopy(attribute_mat1)
    t=copy[0]
    # print("remove: ", remove)
    new_i=t.index(remove)
    # print("index: ", new_i)
    t.pop(new_i)
    temp.append(t)

    for x in copy[1:]:
        if(x[new_i]==val):
            x.pop(new_i)
            temp.append(x)

    # for x in att[1:]:
    #     for y in range(0, len(x)):
    #         if y == new_i:
    #             #print("deleting: ", x[y])
    #             del x[y]
    #     temp.append(x)
        # if(x[new_i]==j):
        #     x.pop(new_i)
        #     temp.append(x)
    # print("***************temp")
    # print (temp)

    temp_dict={'True': 0, 'False': 0}
    for k in temp[1:]:
        for l in range (len(k),len(k)+1):
            #print(k[l-1])
            if k[l-1] == True:
                temp_dict["True"] = temp_dict["True"] + 1
            else:
                temp_dict["False"]= temp_dict["False"] + 1

    if(temp_dict["True"]==0):
        return temp,"False"

    elif(temp_dict["False"]==0):
        return temp,"True"

    return temp, ''

def test(Root_Node, attribute_mat,Root_Obj):                # This function creates the tree given a root node according to the entropy function
    #Root=ethan(attribute_matrix)
    # print_matrix()
    for i in possible_values(Root_Node,attribute_mat):
        # print("Current attribute",Root_Node)
        # print("current attribute value: ", i)
        # print(attribute_matrix)


        temp_2d,bool = exclude(Root_Node, i, attribute_mat)
        # print("************")
        # print("temp2d: ", temp_2d)
        if(bool == "False"):
            # print("all false")
            Leaf_Obj = Node('False')
            Leaf_Obj.matrix = temp_2d
            Leaf_Obj.parent=Root_Obj
            Leaf_Obj.upArc=i
            # print("upArc ",Leaf_Obj.upArc)
            Root_Obj.add_child(Leaf_Obj)
            Root_Obj.arc_label.append(i)


        elif(bool == "True"):
            # print("all true")
            Leaf_Obj = Node('True')
            Leaf_Obj.matrix = temp_2d
            Leaf_Obj.parent = Root_Obj
            Leaf_Obj.upArc=i
            # print("upArc ", Leaf_Obj.upArc)
            Root_Obj.add_child(Leaf_Obj)
            Root_Obj.arc_label.append(i)

        else:

            if (len(temp_2d[0])>2):                 #To exclude the case in which we are left with the VALUE and LABEL attribute only in our temp2d matrix.
                Child_Root=entropyB(temp_2d)
                '''Create Child Node Object from Root_Obj'''
                Child_Obj=Node(Child_Root)
                Child_Obj.matrix = temp_2d
                Child_Obj.parent = Root_Obj
                Child_Obj.upArc = i
                # print("upArc ", Child_Obj.upArc)
                # print(Child_Obj.matrix)
                Root_Obj.add_child(Child_Obj)
                Root_Obj.arc_label.append(i)
                # print("TEMP_2D ", temp_2d)
                test(Child_Root, Child_Obj.matrix, Child_Obj)

    #return Child_Obj

def final_test(attribute_matrix):           #This function returns the root node of the tree
    Root_Node = entropyB(attribute_matrix)
    # print("Root_Node", Root_Node)

    Root_Obj = Node(Root_Node)
    Root_Obj.matrix = attribute_matrix
    Root_Obj.parent="ORPHAN"
    Root_Obj.upArc="UNKNOWN"
    test(Root_Node,attribute_matrix,Root_Obj)
    return Root_Obj


def setRule(temp_rule):
    global current_rule
    current_rule = temp_rule



def scientist( hand, ended):
    global previous2, previous1, current, card_labels, cards_seen, board_state, FinalRule, boardState1
    card = random.choice(hand)
    #print (boardState1)



    if first_round==True:
        # print("entered first round")
        initialize_dict()
        initialize_matrix()
        card=random.choice(hand)

        #generate rule and set
        if previous2 != "":
            FinalRule=generate_rule(previous2, previous1, current)

        return card

    elif first_round == False:# and ended == False:
        #get_gain(attribute_matrix)
        # print("BEFORE FINAL TEST")
        Root=final_test(attribute_matrix)
        # print("AFTER FINAL TEST")
        # print("ROOT :",Root)

        tempArr=[]
        tempArr=print_tree(Root, tempArr)
        # print("TRUE NODES", tempArr)
        pathMat=[]
        for i in tempArr:
            blah = []
            pathMat.append(cal_Path(i,blah))
        # print(pathMat)
        if(len(pathMat)==0):
            FinalRule = orFunc(generate_rule(previous2, previous1, current))
            print("FINAL RULE : ", FinalRule)
            print("")
            return card
        atmoicOR=[]
        FinalRule=""
        for j in pathMat:
            atomicAnd=[]
            for k in j[::-1]:
                atomicAnd.append(atomic_rule(k))
            atmoicOR.append(andFunc(atomicAnd))

        FinalRule=orFunc(atmoicOR)


        if ended == True:
            print("Score : ",score())
            print("FINAL RULE : ", FinalRule)
            return FinalRule
        else:
            return card

    # elif (ended == True):
    #     print("Ended by Adv")
    #     print(FinalRule)
    #     return FinalRule





def evaluate(card, result):         #Creates the attribute matrix
    global attribute_matrix

    new_row = ['0'] * 8

    ##value
    val = value(card)
    new_row[attribute_dict.get(str('VALUE'))] = str(val)

    ##color
    col = color(card)
    new_row[attribute_dict.get(str('COLOR'))] = col

    ##suit
    su = suit(card)
    new_row[attribute_dict.get(str('SUIT'))] = su

    ##even odd
    if even(card) == True:
        new_row[attribute_dict.get('E/O')] = 'even'
    else:
        new_row[attribute_dict.get('E/O')] = 'odd'

    #royal
    if is_royal(card) == True:
        new_row[attribute_dict.get('ROYAL')] = 'royal'
    else:
        new_row[attribute_dict.get('ROYAL')] = '!royal'


    #increasing number
    if value(current) > value(previous1) and value(previous1) > value(previous2):
        new_row[attribute_dict.get('VAL_P')] = 'IV'

    #decreasing number
    elif value(current) < value(previous1) and value(previous1) < value(previous2):
        new_row[attribute_dict.get('VAL_P')] = 'DV'

    #decreasing increasing number
    elif value(current) > value(previous1) and value(previous1) < value(previous2):
        new_row[attribute_dict.get('VAL_P')] = 'DIV'

    #increasing decreasing number
    elif value(current) < value(previous1) and value(previous1) > value(previous2):
        new_row[attribute_dict.get('VAL_P')] = 'IDV'

    #same number
    elif equal(value(current), value(previous1)) and equal(value(current), value(previous2)):
        new_row[attribute_dict.get('VAL_P')] = 'EV'



    # increasing suit
    if greater(suit(current), suit(previous1)) and greater(suit(previous1), suit(previous2)):
        new_row[attribute_dict.get('SUIT_P')] = 'IS'

    # decreasing suit
    elif less(suit(current), suit(previous1)) and less(suit(previous1), suit(previous2)):
        new_row[attribute_dict.get('SUIT_P')] = 'DS'

    # decreasing increasing suit
    elif greater(suit(current), suit(previous1)) and less(suit(previous1), suit(previous2)):
        new_row[attribute_dict.get('SUIT_P')] = 'DIS'

    # increasing decreasing suit
    elif less(suit(current), suit(previous1)) and greater(suit(previous1), suit(previous2)):
        new_row[attribute_dict.get('SUIT_P')] = 'IDS'

    #same suit
    elif equal(suit(current), suit(previous1)) and equal(suit(current), suit(previous2)):
        new_row[attribute_dict.get('SUIT_P')] = 'ES'


    #increasing card
    if greater(current, previous1) and greater(previous1, previous2):
        new_row[attribute_dict.get('CARD_P')] = 'IC'

        # decreasing suit
    elif less(current, previous1) and less(previous1, previous2):
        new_row[attribute_dict.get('CARD_P')] = 'DC'

    # decreasing increasing suit
    elif greater(current, previous1) and less(previous1, previous2):
        new_row[attribute_dict.get('CARD_P')] = 'DIC'

    # increasing decreasing suit
    elif less(current, previous1) and greater(previous1, previous2):
        new_row[attribute_dict.get('CARD_P')] = 'IDC'

    # same suit
    elif equal(current, previous1) and equal(current, previous2):
        new_row[attribute_dict.get('CARD_P')] = 'EC'

    new_row.append(result)
    attribute_matrix.append(new_row)


def initialize_dict():          #Provides variables for generating attribute matrix
    global attribute_dict
    global label_dict

    attribute_dict = {'VALUE' : 0, 'COLOR' : 1, 'SUIT' : 2, 'E/O' : 3, 'ROYAL' : 4, 'VAL_P': 5,
                      'SUIT_P' : 6, 'CARD_P' : 7}

    values = list(range(0, 14))
    label_dict = {'value': list(values), 'color': [13, 14], 'suit': [15, 16, 17, 18], 'even/odd': [19, 20], 'royal': [21, 22],
                  'changing values': [23, 24, 25, 26, 27], 'changing suit': [28, 29, 30, 31, 32], 'changing card': [33, 34, 35, 36, 37]}


def initialize_matrix():
    global attribute_matrix

    values = list(range(0, 9))
    values = list(map(str, values))
    list1=['VALUE','COLOR','SUIT','E/O','ROYAL','VAL_P',
                      'SUIT_P','CARD_P','LABEL']

    attribute_matrix.append(list1)


def dealer(card):
    global current_rule, previous2, previous1, current

    my_rule = current_rule
    dealer_tree = parse(my_rule)
    cards = [previous1, current, card]

    result = dealer_tree.evaluate(cards)

    if result == True:
        previous2 = previous1
        previous1 = current
        current = card

    return result

def print_matrix():
    for i in attribute_matrix:
        print (i)