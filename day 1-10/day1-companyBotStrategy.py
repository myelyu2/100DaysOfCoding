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