#Password Generator 

from os import startfile
import tkinter
import random
from random import shuffle
import math

useable_chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
                "o","p","q","r","s","t","u","v","w","x","y","z","1","2","3",
                "4","5","6","7","8","9","0","!","@","#","$","%","^","&","*",
                "-","_","=","+","(",")","{","}","[","]",";",":","<",">","?","."]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

size = int(input("Length to make Password: "))
chars = input("What chars cannot be used? ").lower().split()
amnt_upper = int(input("How many upercase letters: "))

for i in range(len(chars)):
    if chars[i] in useable_chars:
        useable_chars.remove(chars[i])

num_list = []
for i in range(size):
    num_list.append(math.floor(random.randrange(0,size)))

pw_list = []
random.shuffle(useable_chars)
for i in range(len(num_list)):
    pw_list.append(useable_chars[num_list[i]])

pwstr = ''.join(pw_list)

if amnt_upper > 0:
    upper_places = []
    for i in range(amnt_upper):
        upper_places.append(math.floor(random.randrange(0,amnt_upper)))
    
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
        edit_string.append(alphabet[random.randrange(0,len(alphabet))].upper())
        pwstr.removeprefix
    
    random.shuffle(edit_string)

    pwstr = "".join(edit_string)

    starts_with_bad_char = True
    while starts_with_bad_char:
        if pwstr.startswith(".") or pwstr.startswith("-"):
            edit_string = pwstr
            random.shuffle(edit_string)
            pwstr = "".join(edit_string)
        starts_with_bad_char = False
    
    print(pwstr)
else:
    print(pwstr)
