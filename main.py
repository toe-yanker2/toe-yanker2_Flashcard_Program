import os
import json
import random

dog = [
    {
        "This": "is",
        "a": "dictionary",
    },
    {
        "This": "is",
        "a": "nother",
    },
]

flashcards = {
    "1": ["1+1", "2"],
    "2": ["5*6", "30"],
    "3": ["19*7", "133"],
    "4": ["17-180", "-163"],
    "5": ["x + 6 = 7", "1"],
    "6": ["3(x + 4) = 18", "2"],
    "7": ["x(x - 5) = -6", "2, 3"],
    "8": ["2^5", "32"],
    "9": ["5^x = 125", "3"],
    "10": ["x^3 = 64", "4"],
    "11": ["log4(32)", "5/2"],
    "12": ["log(100)", "2"],
    "13": ["6*9+6+9", "69"],
    "14": ["8+7*(6+4)", "78"],
    "15": ["30% of 1080", "324"],
    "16": ["5!", "120"],
    "17": ["442/26", "17"],
    "18": ["96*37", "3552"],
    "19": ["1987+777", "2764"],
    "20": ["2024-365", "1759"],
}

if os.path.isfile("data.json"):
  with open("data.json", "r") as data_json:
    data = json.load(data_json)
    print(data)
else:
  data = []


def test():
  result = {i: ["Incorrect", ""] for i in range(20)}
  order = list(range(len(flashcards)))
  random.shuffle(order)
  for i in order:
    answer = input(flashcards[i])
    
  return result


data.append(test())
print(data)



# with open("data.json", "w") as data_json:
#   json.dump(data, data_json)
