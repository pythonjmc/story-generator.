("&")

import random
import importlib

file = importlib.import_module("stories_variables")

obj = file.get_story

while True:
    print("Do you want a story ?", end="")
    answer = input()
    if answer == "yes":
        print(obj())
    else:
        break
