#!/usr/bin/env python

import re
from sys import argv

def parse(INPUT, OUTPUT):
    INPUT = list(open(INPUT,'r'))
    questions = []
    answers = []
    for i,line in enumerate(INPUT):
        line = line.strip("\n")
        if "Result:" not in line and line != '':
            line = line.replace(".\"", "\".")
            line = line.replace(",\"", "\",")
            line = re.sub(r'\(.*\)','',line)
            line = re.sub(r'\[.*\]','',line)
            line = re.sub(r'\{.*\}','',line)
            if "Question: " in line:
                line = line.replace("Question: ", "")
                questions.append(line)
            elif "ANSWER: " in line:
                line = line.replace("ANSWER: ", "")
                answers.append(line)
    
    out = open(OUTPUT, "w")
    for i,clue in enumerate(questions):
    	cards = clue.split(".")
    	for card in cards:
    		if card != "":
    			card = re.sub(r'^\s', '', card)
    			out.write(card + "\t" + answers[i] + "\n")

if __name__ == "__main__":
    parse(argv[1],argv[2])