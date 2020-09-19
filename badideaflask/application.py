from flask import Flask, redirect, url_for, render_template
import time
import sys
import random

application = app = Flask(__name__)

@app.route("/")
def home():
    # Random first verb
    firstVerbs = ["Hack ", "Innovate ", "Monetize ", "Create "]
    firstVerbRandom = random.randint(0, 3)

    # Random Noun
    f = open("nounlist.txt")
    nounLines = f.readlines()
    lineCount = len(open("nounlist.txt").readlines())
    randomNoun1 = random.randint(0, lineCount)
    randomNoun2 = random.randint(0, lineCount)
    randomNoun3 = random.randint(0, lineCount)

    fullSentence = firstVerbs[firstVerbRandom] + nounLines[randomNoun1] + \
                   " with " + nounLines[randomNoun2] + " and " \
                   + nounLines[randomNoun3]

    return render_template("index.html", fullSentence=fullSentence)


if __name__ == "__main__":
    app.run()
