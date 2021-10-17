# compares each char in the string and returns False if there is a dangerous character
def check_string(text):
    for char in text:
        if char == "'":
            return False
        elif char == '"':
            return False
        elif char == "=":
            return False

    return True
