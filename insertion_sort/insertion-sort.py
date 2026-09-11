# Recitation 2: Sorting I. Zero points.
#
# Insertion sort works the way most people sort the cards already in their
# hand: take the next unsorted card and slide it left past every card that is
# bigger than it, until it sits in the right place among the sorted cards.
#
# Python compares strings alphabetically with <, so "ACG" < "ACT" is True.

def insertion_sort(items: list[str]) -> list[str]:
    """
    Sort a list of strings into alphabetical order using insertion sort.

    Parameters:
    - items (list[str]): The strings to sort.

    Returns:
    - list[str]: A list containing the same strings in ascending
      alphabetical order. The original list is not changed.
    """
    #loop through array
    for i in range(0,len(items)):
        
        for p in range(i,0,-1):
            current=items[p]
            one_before=items[p-1]
            #check if number is sorted compared to one before
            #if not sorted, swap
            if current<one_before:
                temp=items[p]
                items[p]=items[p-1]
                items[p-1]=temp
            #if sorted, break out of loop
            else:
                break

    return items
