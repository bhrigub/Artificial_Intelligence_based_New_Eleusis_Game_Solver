

from new_eleusis_new import *

def generate_rule(temp_previous2, temp_previous, temp_current): # Generate Rule creates a rule if the game ends  in the very first time OR we are not able to get Illegal cards
    rules = []
    simpleRule = []
    #print('asdkj;faskldfj')

    val_pev2 = value(temp_previous2)
    #print(val_pev2)
    val_pev1 = value(temp_previous)
    #print(val_pev1)
    val_cur = value(temp_current)
    #print(val_cur)
    #print('asdkj;faskldfj')




    ###NUMERIC VALUE###
    #strictly increasing
    if value(temp_previous) >  value(temp_previous2) and value(temp_current) > value(temp_previous):
        rules.append("""and(greater(previous[0], previous2[0]), greater(current[0], previous[0]))""")
        simpleRule.append("NumericValue - a < b < c")

    #strictly decreasing
    elif value(temp_previous) <  value(temp_previous2) and value(temp_current) < value(temp_previous):
        rules.append("""and(less(previous[0], previous2[0]), less(current[0], previous[0]))""")
        simpleRule.append("NumericValue - a > b > c")

    #increasing -> decreasing
    elif value(temp_previous) > value(temp_previous2) and value(temp_current) < value(temp_previous):
        rules.append("""and(greater(previous[0], previous2[0]), less(current[0], previous[0]))""")
        simpleRule.append("NumericValue - a < b > c")

    #decreasing -> increasing
    elif value(temp_previous) < value(temp_previous2) and value(temp_current) > value(temp_previous):
        rules.append("""and(less(previous[0], previous2[0]), greater(current[0], previous[0]))""")
        simpleRule.append("NumericValue - a > b < c")

    #decreasing -> equal
    elif value(temp_previous) < value(temp_previous2) and value(temp_current) == value(temp_previous):
        rules.append("""and(less(previous[0], previous2[0]), equal(current[0], previous[0]))""")
        simpleRule.append("NumericValue - a > b = c")

    #increasing -> equal
    elif value(temp_previous) > value(temp_previous2) and value(temp_current) == value(temp_previous):
        rules.append("""and(greater(previous[0], previous2[0]), equal(current[0], previous[0]))""")
        simpleRule.append("NumericValue - a < b = c")

    #equal -> decreasing
    elif value(temp_previous) == value(temp_previous2) and value(temp_current) < value(temp_previous):
        rules.append("""and(equal(previous[0], previous2[0]), less(current[0], previous[0]))""")
        simpleRule.append("NumericValue - a = b > c")

    # equal -> increasing
    elif value(temp_previous) == value(temp_previous2) and value(temp_current) > value(temp_previous):
        rules.append("""and(equal(previous[0], previous2[0]), greater(current[0], previous[0]))""")
        simpleRule.append("NumericValue - a = b < c")

    # equal -> equal
    elif value(temp_previous) == value(temp_previous2) and value(temp_current) == value(temp_previous):
        rules.append("""and(equal(previous[0], previous2[0]), equal(current[0], previous[0]))""")
        simpleRule.append("NumericValue - a = b = c")




    ###SUIT VALUE###
    #strictly increasing
    if greater(suit(temp_previous), suit(temp_previous2)) and greater(suit(temp_current), suit(temp_previous)):
        rules.append("""and(greater(suit(previous), suit(previous2)), greater(suit(current), suit(previous)))""")
        simpleRule.append("SuitValue - a < b < c")

    #strictly decreasing
    elif less(suit(temp_previous), suit(temp_previous2)) and less(suit(temp_current), suit(temp_previous)):
        rules.append("""and(less(suit(previous), suit(previous2)), less(suit(current), suit(previous)))""")
        simpleRule.append("SuitValue - a > b > c")

    #increasing -> decreasing
    elif greater(suit(temp_previous), suit(temp_previous2)) and less(suit(temp_current), suit(temp_previous)):
        rules.append("""and(greater(suit(previous), suit(previous2)), less(suit(current), suit(previous)))""")
        simpleRule.append("SuitValue - a < b > c")

    #decreasing -> increasing
    elif less(suit(temp_previous), suit(temp_previous2)) and greater(suit(temp_current), suit(temp_previous)):
        rules.append("""and(less(suit(previous), suit(previous2)), greater(suit(current), suit(previous)))""")
        simpleRule.append("SuitValue - a > b < c")

    #equal --> decreasing
    elif equal(suit(temp_previous), suit(temp_previous2)) and less(suit(temp_current), suit(temp_previous)):
        rules.append("""and(equal(suit(previous), suit(previous2)), less(suit(current), suit(previous)))""")
        simpleRule.append("SuitValue - a = b > c")

    #equal --> increasing
    elif equal(suit(temp_previous), suit(temp_previous2)) and greater(suit(temp_current), suit(temp_previous)):
        rules.append("""and(equal(suit(previous), suit(previous2)), greater(suit(current), suit(previous)))""")
        simpleRule.append("SuitValue - a = b < c")

    #increasing --> equal
    elif greater(suit(temp_previous), suit(temp_previous2)) and equal(suit(temp_current), suit(temp_previous)):
        rules.append("""and(greater(suit(previous), suit(previous2)), equal(suit(current), suit(previous)))""")
        simpleRule.append("SuitValue - a < b = c")

    #decreasing --> equal
    elif less(suit(temp_previous), suit(temp_previous2)) and equal(suit(temp_current), suit(temp_previous)):
        rules.append("""and(less(suit(previous), suit(previous2)), equal(suit(current), suit(previous)))""")
        simpleRule.append("SuitValue - a > b = c")

    #equal --> equal
    elif less(suit(temp_previous), suit(temp_previous2)) and equal(suit(temp_current), suit(temp_previous)):
        rules.append("""and(equal(suit(previous), suit(previous2)), equal(suit(current), suit(previous)))""")
        simpleRule.append("SuitValue - a = b = c")

    # ###SUIT PATTERN###
    # #all same
    # if equal(suit(temp_previous2), suit(temp_previous)) and equal(suit(temp_previous), suit(temp_current)):
    #     rules.append("""and(equal(suit(previous2), suit(previous)), equal(suit(previous), suit(current)))""")
    #     simpleRule.append("SuitPsttern - a a a")
    #
    # #alternating, aba
    # elif equal(suit(temp_previous2), suit(temp_current)) and not(equal(suit(temp_previous2), suit(temp_previous))):
    #     rules.append("""and(equal(suit(previous2), suit(current)), not(equal(suit(previous2), suit(previous))))""")
    #     simpleRule.append("SuitPattern - a b a")
    #
    # #abb
    # elif equal(suit(temp_previous), suit(temp_current)) and not(equal(suit(temp_previous2), suit(temp_previous))):
    #     rules.append("""and(equal(suit(previous), suit(current)), not(equal(suit(previous2), suit(previous))))""")
    #     simpleRule.append("SuitPattern - a b b")
    #
    # #bba
    # elif equal(suit(temp_previous2), suit(temp_previous)) and not(equal(suit(temp_previous), suit(temp_current))):
    #     rules.append("""and(equal(suit(previous2), suit(previous)), not(equal(suit(previous), suit(current))))""")
    #     simpleRule.append("SuitPattern - b b a")
    #
    # ## all different, abc
    # elif not(equal(suit(temp_previous2), suit(temp_previous))) and not(equal(suit(temp_previous), suit(temp_current))) and not(equal(suit(temp_previous2), suit(temp_current))):
    #     rules.append("""and(not(equal(suit(previous2), suit(previous))), not(equal(suit(previous), suit(current))))""")
    #     simpleRule.append("SuitPattern - a b c")



    ###CARD VALUE###
    #strictly increasing
    if greater(temp_previous, temp_previous2) and greater(temp_current, temp_previous):
        rules.append("""and(greater(previous, previous2), greater(current, previous))""")
        simpleRule.append("CardValue - a < b < c")

    #strictly decreasing
    elif less(temp_previous,  temp_previous2) and less(temp_current, temp_previous):
        rules.append("""and(less(previous, previous2), less(current, previous))""")
        simpleRule.append("CardValue - a > b > c")

    #increasing -> decreasing
    elif greater(temp_previous, temp_previous2) and less(temp_current, temp_previous):
        rules.append("""and(greater(previous, previous2), less(current, previous))""")
        simpleRule.append("CardValue - a < b > c")

    #decreasing -> increasing
    elif less(temp_previous, temp_previous2) and greater(temp_current, temp_previous):
        rules.append("""and(less(previous, previous2), greater(current, previous))""")
        simpleRule.append("CardValue - a > b < c")

    #increasing --> equal
    elif greater(temp_previous, temp_previous2) and equal(temp_current, temp_previous):
        rules.append("""and(greater(previous, previous2), equal(current, previous))""")
        simpleRule.append("CardValue - a < b = c")

    # decreasing -> equal
    elif less(temp_previous, temp_previous2) and equal(temp_current, temp_previous):
        rules.append("""and(less(previous, previous2), equal(current, previous))""")
        simpleRule.append("CardValue - a > b = c")

    # equal --> increasing
    elif equal(temp_previous, temp_previous2) and greater(temp_current, temp_previous):
        rules.append("""and(equal(previous, previous2), greater(current, previous))""")
        simpleRule.append("CardValue - a = b < c")

    # equal --> decreasing
    elif equal(temp_previous, temp_previous2) and less(temp_current, temp_previous):
        rules.append("""and(equal(previous, previous2), less(current, previous))""")
        simpleRule.append("CardValue - a = b > c")

    # equal --> equal
    elif equal(temp_previous, temp_previous2) and equal(temp_current, temp_previous):
        rules.append("""and(equal(previous, previous2), equal(current, previous))""")
        simpleRule.append("CardValue - a = b = c")



    # ###COLOR###
    # #all same
    # if equal(color(temp_previous2), color(temp_previous)) and equal(color(temp_previous), color(temp_current)):
    #     rules.append("""and(equal(color(previous2), color(previous)), equal(color(previous), color(current)))""")
    #     simpleRule.append("Color - a a a")
    #
    # #abb
    # elif equal(color(temp_previous), color(temp_current)) and not(equal(color(temp_previous2), color(temp_previous))):
    #     rules.append("""and(equal(color(previous), color(current)), not(equal(color(previous2), color(previous))))""")
    #     simpleRule.append("Color - a b b")
    #
    # #aba
    # elif equal(color(temp_previous2), color(temp_current)) and not (equal(color(temp_previous), color(temp_previous2))):
    #     rules.append("""and(equal(color(previous2), color(current)), not(equal(color(previous), color(previous2))))""")
    #     simpleRule.append("Color - a b a")
    #
    # #bba
    # elif equal(color(temp_previous2), color(temp_previous)) and not (equal(color(temp_previous), color(temp_current))):
    #     rules.append("""and(equal(color(previous2), color(previous)), not(equal(color(previous), color(current))))""")
    #     simpleRule.append("Color - b b a")



    ###color VALUE###
    #strictly increasing
    if greater(color(temp_previous), color(temp_previous2)) and greater(color(temp_current), color(temp_previous)):
        rules.append("""and(greater(color(previous), color(previous2)), greater(color(current), color(previous)))""")
        simpleRule.append("colorValue - a < b < c")

    #strictly decreasing
    elif less(color(temp_previous), color(temp_previous2)) and less(color(temp_current), color(temp_previous)):
        rules.append("""and(less(color(previous), color(previous2)), less(color(current), color(previous)))""")
        simpleRule.append("colorValue - a > b > c")

    #increasing -> decreasing
    elif greater(color(temp_previous), color(temp_previous2)) and less(color(temp_current), color(temp_previous)):
        rules.append("""and(greater(color(previous), color(previous2)), less(color(current), color(previous)))""")
        simpleRule.append("colorValue - a < b > c")

    #decreasing -> increasing
    elif less(color(temp_previous), color(temp_previous2)) and greater(color(temp_current), color(temp_previous)):
        rules.append("""and(less(color(previous), color(previous2)), greater(color(current), color(previous)))""")
        simpleRule.append("colorValue - a > b < c")

    #equal --> decreasing
    elif equal(color(temp_previous), color(temp_previous2)) and less(color(temp_current), color(temp_previous)):
        rules.append("""and(equal(color(previous), color(previous2)), less(color(current), color(previous)))""")
        simpleRule.append("colorValue - a = b > c")

    #equal --> increasing
    elif equal(color(temp_previous), color(temp_previous2)) and greater(color(temp_current), color(temp_previous)):
        rules.append("""and(equal(color(previous), color(previous2)), greater(color(current), color(previous)))""")
        simpleRule.append("colorValue - a = b < c")

    #increasing --> equal
    elif greater(color(temp_previous), color(temp_previous2)) and equal(color(temp_current), color(temp_previous)):
        rules.append("""and(greater(color(previous), color(previous2)), equal(color(current), color(previous)))""")
        simpleRule.append("colorValue - a < b = c")

    #decreasing --> equal
    elif less(color(temp_previous), color(temp_previous2)) and equal(color(temp_current), color(temp_previous)):
        rules.append("""and(less(color(previous), color(previous2)), equal(color(current), color(previous)))""")
        simpleRule.append("colorValue - a > b = c")

    #equal --> equal
    elif equal(color(temp_previous), color(temp_previous2)) and equal(color(temp_current), color(temp_previous)):
        rules.append("""and(equal(color(previous), color(previous2)), equal(color(current), color(previous)))""")
        simpleRule.append("colorValue - a = b = c")


    ###EVEN/ODD###
    #all even
    if even(temp_previous2) and even(temp_previous) and even(temp_current):
        rules.append("""and(and(even(previous2), even(previous)), and(even(previous), even(current)))""")
        simpleRule.append("EvenOdd - e e e")

    #all odd
    elif odd(temp_previous2) and odd(temp_previous) and odd(temp_current):
        rules.append("""and(and(odd(previous2), odd(previous)), and(odd(previous), odd(current)))""")
        simpleRule.append("EvenOdd - o o o")

    #eeo
    elif even(temp_previous2) and even(temp_previous) and odd(temp_current):
        rules.append("""and(and(even(previous2), even(previous)), and(even(previous), odd(current)))""")
        simpleRule.append("EvenOdd - e e o")

    #eoo
    elif even(temp_previous2) and odd(temp_previous) and odd(temp_current):
        rules.append("""and(and(even(previous2), odd(previous)), and(odd(previous), odd(current)))""")
        simpleRule.append("EvenOdd - e o o")

    #ooe
    elif odd(temp_previous2) and odd(temp_previous) and even(temp_current):
        rules.append("""and(and(odd(previous2), odd(previous)), and(odd(previous), even(current)))""")
        simpleRule.append("EvenOdd - o o e")

    #oee
    elif odd(temp_previous2) and even(temp_previous) and even(temp_current):
        rules.append("""and(and(odd(previous2), even(previous)), and(even(previous), even(current)))""")
        simpleRule.append("EvenOdd - o e e")

    #oeo
    elif odd(temp_previous2) and even(temp_previous) and odd(temp_current):
        rules.append("""and(and(odd(previous2), even(previous)), and(even(previous), odd(current)))""")
        simpleRule.append("EvenOdd - o e o")

    #eoe
    elif even(temp_previous2) and odd(temp_previous) and even(temp_current):
        rules.append("""and(and(even(previous2), odd(previous)), and(odd(previous), even(current)))""")
        simpleRule.append("EvenOdd - e o e")

    ###ROYAL###
    #all royal
    if is_royal(temp_previous2) and is_royal(temp_previous) and is_royal(temp_current):
        rules.append("""and(and(is_royal(previous2), is_royal(previous)), and(is_royal(previous), is_royal(current)))""")
        simpleRule.append("Royal - r r r")

    #R !R R
    elif is_royal(temp_previous2) and  not(is_royal(temp_previous)) and is_royal(temp_current):
        rules.append("""and(and(is_royal(previous2), not(is_royal(previous))), and(not(is_royal(previous)), is_royal(current)))""")
        simpleRule.append("Royal - r nr r")
    #RR !R
    elif is_royal(temp_previous2) and is_royal(temp_previous) and not(is_royal(temp_current)):
        rules.append("""and(and(is_royal(previous2), is_royal(previous)), and(is_royal(previous), not(is_royal(current))))""")
        simpleRule.append("Royal - r r nr")

     # !R RR
    elif not(is_royal(temp_previous2)) and is_royal(temp_previous) and is_royal(temp_current):
        rules.append("""and(and(not(is_royal(previous2)), is_royal(previous)), and(is_royal(previous), is_royal(current)))""")
        simpleRule.append("Royal - nr r r")

    #!R !R R
    elif not(is_royal(temp_previous2)) and not (is_royal(temp_previous)) and is_royal(temp_current):
        rules.append("""and(and(not(is_royal(previous2)), not(is_royal(previous))),and(not(is_royal(previous)), is_royal(current)))""")
        simpleRule.append("Royal - nr nr r")

    # !R R !R
    elif not (is_royal(temp_previous2)) and  is_royal(temp_previous) and not(is_royal(temp_current)):
        rules.append("""and(and(not(is_royal(previous2)), is_royal(previous)), and(is_royal(previous), not(is_royal(current))))""")
        simpleRule.append("Royal - nr r nr")

    # R !R !R
    elif is_royal(temp_previous2) and not (is_royal(temp_previous)) and not(is_royal(temp_current)):
        rules.append("""and(and(is_royal(previous2), not(is_royal(previous))), and(not(is_royal(previous)), not(is_royal(current))))""")
        simpleRule.append("Royal - r nr nr")

    # !R !R !R
    elif not(is_royal(temp_previous2)) and not (is_royal(temp_previous)) and not (is_royal(temp_current)):
        rules.append("""and(and(not(is_royal(previous2)), not(is_royal(previous))), and(not(is_royal(previous)), not(is_royal(current))))""")
        simpleRule.append("Royal - nr nr nr")

    #print(rules)

    return rules