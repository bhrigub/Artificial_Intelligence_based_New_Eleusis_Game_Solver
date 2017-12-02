

atomic_dict = {'R': 'equal(color(current), R)',
               'B': 'equal(color(current), B)',

               'odd': 'equal(odd(current), T)',
               'even': 'equal(even(current), T)',

               'C': 'equal(suit(current), C)',
               'D': 'equal(suit(current), D)',
               'H': 'equal(suit(current), H)',
               'S': 'equal(suit(current), S)',

               'royal': 'equal(is_royal(current), T)',
               '!royal': 'equal(is_royal(current), F)',

               'IV': 'and(greater(value(previous), value(previous2)), greater(value(current), value(previous)))',
               'DV': 'and(greater(value(previous2), value(previous)), greater(value(previous), value(current)))',
               'IDV': 'and(greater(value(previous), value(previous2)), greater(value(previous), value(current)))',
               'DIV': 'and(greater(value(previous2), value(previous)), greater(value(current), value(previous)))',
               'EV': 'and(equal(value(previous2), value(previous)), equal(value(current), value(previous)))',

               'IS': 'and(greater(suit(previous), suit(previous2)), greater(suit(current), suit(previous)))',
               'DS': 'and(greater(suit(previous2), suit(previous)), greater(suit(previous), suit(current)))',
               'IDS': 'and(greater(suit(previous), suit(previous2)), greater(suit(previous), suit(current)))',
               'DIS': 'and(greater(suit(previous2), suit(previous)), greater(suit(current), suit(previous)))',
               'ES': 'and(equal(suit(previous2), suit(previous)), equal(suit(current), suit(previous)))',

               'IC': 'and(greater(previous, previous2), greater(current, previous))',
               'DC': 'and(greater(previous2, previous), greater(previous, current))',
               'IDC': 'and(greater(previous, previous2), greater(previous, current))',
               'DIC': 'and(greater(previous2, previous), greater(current, previous))',
               'EC': 'and(equal(previous2, previous), equal(current, previous))'

               }


def atomic_rule(val):           #Returns an atomic rule pertaining to a given attribute value
    global atomic_dict
    value = atomic_dict.get(val)
    #print(value)
    return value



