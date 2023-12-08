import os
import math


os.chdir(os.path.dirname(os.path.abspath(__file__)))
total:int=0

class solver():
    def load_file(self)->str:
        with open("input.txt", "r") as file:
            text= file.read()
        return text
    
    @staticmethod
    def score(linear:int):
        if linear!=0:
            newscore=math.pow(2,(linear-1))
            return newscore
        else:
            return 0
    
text=solver().load_file()
lines:list[str]=text.split('\n')
for card in lines:
    card_score:int=0
    sets:list[str]=card.split('|')
    # sets: winning, ours
    sets[0]=sets[0].split(':')[1].strip(' ').replace('  ', ' ')
    sets[1]=sets[1].strip(' ').replace('  ', ' ')
    wns=sets[0].split(' ')
    ons=sets[1].split(' ')
    winning_numbers:list[int]=[]
    our_numbers:list[int]=[]
    for num in wns:
        winning_numbers.append(int(num))
    for num in ons:
        our_numbers.append(int(num))
    for num in our_numbers:
        if num in winning_numbers:
            card_score+=1
    total+=solver.score(card_score)
    print(card_score, solver.score(card_score))

print(total)