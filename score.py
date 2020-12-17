import os

class Score():
    
    #creates an array of scores stored in Highscores.txt
    def read_score(self):
        f = open(os.path.join('assets/', 'highscores.txt'),'r')
        lines = f.readlines()
        f.close() 
        scores =[]
        for line in lines:
            scores.append(int(line))
        return scores
            
    #Writes current score in txt file
    def write_score(self,value):
        f = open(os.path.join('assets/', 'highscores.txt'),'a+')
        f.write('\n' + str(value))
        f.close()
        
    #Returns largest score found in txt file    
    def highscore(self):
        scores = self.read_score()
        return max(scores)