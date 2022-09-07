"""
Each CodeSignal Company Bot is trained by engineers from that specific company. 
The way it works is that a representative group of engineers from each company is identified as trainers before the bot goes live, and they CodeFight against the bot during a training phase. 
The current training algorithm is definitely more complex, but let's assume it works this way:

For each trainer we collect two pieces of information per task [answerTime, correctness], where correctness is 1 if the answer was correct, -1 if the answer was wrong, and 0 if no answer was given. 
In this case, the bot's correct answer time for a given task would be the average of the answer times from the trainers who answered correctly. 
Given all of the training information for a specific task, calculate the bot's answer time.
"""

from numpy import mean

def solution(trainingData):
    final = []
    for i in range(len(trainingData)):
        for j in range(1):
            if(trainingData[i][1] == 1):
                final.append(trainingData[i][0])
                
    # if list is empty
    if not final:
        return 0
        
    return mean(final)