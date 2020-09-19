import time
import sys
from tqdm import tqdm
import random

print("Would you like an idea? (Y/N)")
ans = input()
if ans == "Y" or ans == "y":
    print("Generating...")
    # Random first verb
    firstVerbs = ["Hack ", "Innovate ", "Monetize ", "Create "]
    firstVerbRandom = random.randint(0,3)

    # Random Noun
    f = open("nounlist.txt")
    nounLines = f.readlines()
    lineCount = len(open("nounlist.txt").readlines(  ))
    randomNoun1 = random.randint(0,lineCount)
    randomNoun2 = random.randint(0, lineCount)
    randomNoun3 = random.randint(0, lineCount)

    pbar = tqdm(total=100)
    for i in range(10):
        time.sleep(0.1)
        pbar.update(10)
    pbar.close()
    print("")
    print("Here is your great idea:")
    print(firstVerbs[firstVerbRandom] + nounLines[randomNoun1] + " with " + nounLines[randomNoun2] + " and " + nounLines[randomNoun3])
elif ans == "N" or ans == "n":
    print("Thanks for wasting my time")
else:
    print("I don't think I can help you")