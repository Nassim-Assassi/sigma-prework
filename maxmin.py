# maxmin.py

def is_int(string):
    """
    Returns True if the string represents an integer or False if it doesn't
    """
    if string:
        if string[0] in ["-", "+"]:
            return string[1:].isdigit()
    return string.isdigit()


def maxmin(array):
    """
    Returns a list with the minimum and maximum values from the parameter array.

    Parameter array must be a list containing only integers.
    """
    max = array[0]
    min = array[0]
    # iterates through the list editing the max and min objects as necessary
    for value in array[1:]:
        if value > max:
            max = value
        if value < min:
            min = value
    return [min, max]


def user_array_input():
    """
    Asks the user for an array of integers in the format '[a,b,...]' and returns a matching list object 

    If the input is not in the format '[a,b,...]' an error message is printed and the user is asked again.
    """
    user_input = input(
        "Please input an array of integers in the format '[a,b,...]': ")
    user_input = user_input.replace(" ", "")
    if not user_input:
        print("You have not entered anything")
        return user_array_input()
    elif [user_input[0], user_input[-1]] != ["[", "]"] or sum(map(user_input.count, ("[", "]"))) != 2 or "," not in user_input:
        print("Your input doesn't match the required array format")
        return user_array_input()
    # remove first and last character, "[" and "]"
    user_input = user_input[1:-1]
    array = user_input.split(",")
    try:  # tries to turn list items into integers
        array = list(map(int, array))
    except:  # if it fails an error is printed and the function is restarted via return
        print("Your input doesn't match the required array format")
        return user_array_input()
    return array  # if no errors are found the array is returned


def main():
    list = user_array_input()
    print(maxmin(list))


main()
