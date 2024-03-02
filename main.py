import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    letters_verify = 'abcdefghijklmnopqrstuvwxyz'
    num_verify = '0123456789'
    # check length
    if (len(s) > 6) or (len(s) < 2):
        # print("Word is too long!")
        return False
    elif s[0].lower() not in letters_verify or \
            s[1].lower() not in letters_verify:
        # print("First two characters are not letters!")
        return False
    else:
        start_index = 0
        position = 0
        for letter in s:
            if letter.lower() not in letters_verify and letter not in num_verify:
                # print(f"Letter.lower(): {letter.lower()}Punctuation Found: {letter}")
                return False
            else:
                if letter in num_verify:
                    start_index = position
                    break
            position += 1
        if start_index == 0:
            return True
        elif s[start_index] == '0':
            # print(f"First number cannot be 0! Index is: {start_index}")
            return False
        else:
            for num in range(start_index, len(s)):
                if s[num] not in num_verify:
                    # print("You hit a letter! Fail!")
                    return False
            # print("Great input!")
            return True


main()
