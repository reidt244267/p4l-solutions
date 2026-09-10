# Insert your prefixes() function here.
def prefixes(s: str) -> list[str]:
    """
    Return a list of all prefixes of the string s.

    Parameters:
        s (str) - The input string.

    Returns:
        list[str] - A list of prefixes of s, starting with the empty string ""
                    and ending with s itself.
    """
    lst=[]
    for i in range(0,len(s)+1):
        lst.append(s[0:i])

    return lst
