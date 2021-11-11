# Password Generator
#USING DASHES MAY SHORTEN THE LENGTH

from os import startfile
import tkinter
import random
from random import shuffle
import math

def add_dash(pwstr):
    temp_list = list(pwstr)
    temp_list = list(''.join(l + '-' * (n % 4 == 3) for n, l in enumerate(temp_list)))
    pwstr = ''.join(temp_list)
    if pwstr.endswith('-'):
        temp_list = list(pwstr)
        temp_list.pop()
        pwstr = ''.join(temp_list)
    return(pwstr)
def find_chars(strChars, chars):
    useable_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2',
                     '3', '4', '5', '6', '7', '8', '9', '0', "!", "@", "#", "$", "%", "^", "&", "*", "_", "=", "+", "(", ")", "{", "}", "[", "]", ";", ":", "<", ">", "?", "."]
    vals_to_remove = []
    if strChars == "none":
        return(useable_chars)
    elif strChars == "alphabet":
        for character in range(len(useable_chars)):
            if useable_chars[character].isalpha():
                vals_to_remove.append(useable_chars[character])
        for vals in vals_to_remove:
            if vals in useable_chars:
                useable_chars.remove(vals)
        return(useable_chars)
    elif strChars == "numbers":
        for integer in useable_chars:
            if integer.isdigit():
                vals_to_remove.append(integer)
        for vals in vals_to_remove:
            if vals in useable_chars:
                useable_chars.remove(vals)
        return(useable_chars)
    elif strChars == "alnum":
        for integer in useable_chars:
            if not integer.isalnum():
                vals_to_remove.append(integer)
        for vals in vals_to_remove:
            if vals in useable_chars:
                useable_chars.remove(vals)
        return(useable_chars)
    else:
        for i in range(len(chars)):
            if chars[i] in useable_chars:
                useable_chars.remove(chars[i])
        return(useable_chars)


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

size = int(input("Approximate length to make Password: "))
chars = input("What chars cannot be used? ").lower().split()
strChars = ''.join(chars)
amnt_upper = int(input("How many upercase letters: "))
dashes = input("Do you want dashes? ")

useable_chars = find_chars(strChars, chars)

num_list = []
for i in range(size):
    num_list.append(math.floor(random.randrange(0, size)))

pw_list = []

temp_list = [i * size for i in useable_chars]
temp_str = ''
for l in temp_list:
    temp_str += l
useable_chars.clear()
useable_chars = list(temp_str)
random.shuffle(useable_chars)
for i in range(len(num_list)):
    pw_list.append(useable_chars[num_list[i]])

pwstr = ''.join(pw_list)

if amnt_upper > 0:
    upper_places = []
    for i in range(amnt_upper):
        upper_places.append(math.floor(random.randrange(0, amnt_upper)))

    char_amnt = 0
    for i in pwstr:
        if char_amnt < amnt_upper:
            if i.isalnum():
                char_amnt += 1
            else:
                for char in range(len(pwstr)):
                    if not pwstr[char].isalpha():
                        replace = pwstr[char]
                        new = useable_chars[random.randrange(
                            0, len(useable_chars))]
                        pw_list = list(pwstr)
                        if replace in pw_list:
                            pw_list[char] = new
                            pwstr = "".join(pw_list)

    edit_string = list(pwstr)
    for i in range(len(upper_places)):
        edit_string.append(
            alphabet[random.randrange(0, len(alphabet))].upper())
    for i in edit_string:
        if not i.isupper():
            edit_string.remove(i)

    random.shuffle(edit_string)

    pwstr = "".join(edit_string)

    starts_with_bad_char = True
    while starts_with_bad_char:
        if pwstr.startswith(".") or pwstr.startswith("-"):
            edit_string = pwstr
            random.shuffle(edit_string)
            pwstr = "".join(edit_string)
        starts_with_bad_char = False
    
    if dashes == "yes":
        pwstr = add_dash(pwstr)
        print(f"Here is your password: {pwstr}")
    elif dashes == "no":
        print(f"Here is your password: {pwstr}")
else:
    if dashes == "yes":
        pwstr = add_dash(pwstr)
        print(f"Here is your password: {pwstr}")
    elif dashes == "no":
        print(f"Here is your password: {pwstr}")
