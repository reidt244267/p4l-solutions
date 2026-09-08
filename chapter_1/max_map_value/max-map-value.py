 

# Insert your max_map_value() function here.
def max_map_value(dict_values: dict) -> int:
    """
    max_map_value finds the maximum value of a given dictionary.

    Parameters:
    - dict_values (dict): A dictionary that has integers as values.

    Retursn:
    - int: The highest value key in the given dictionary.
    """

    m = 0
    firstTime = True
    for pattern,value in dict_values.items():
        if (firstTime == True) or (dict_values[pattern] > m):
            firstTime= False
            m = dict_values[pattern]
    return m
