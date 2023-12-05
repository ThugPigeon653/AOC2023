import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

limits:{}={
    "red":12,
    "green":13,
    "blue":14
    }

with open("input.txt", "r") as file:
    games:list[str]=file.read().split('\n')

total:int=0

for i in range(len(games)):
    game=games[i]
    is_game_possible:bool=True
    game_result:str=game.split(':')[1]
    game_statistics:list[str]=game_result.split(';')
    for stat in game_statistics:
        sets:list[str]=stat.lstrip().split(',')
        for set in sets:
            subset=set.lstrip().split(' ')
            actual_value:int=int(subset[0])
            limit:int=int(limits[subset[1]])
            if  actual_value>limit:
                is_game_possible=False
    if is_game_possible==True:
        total+=(i+1)
    i+=1




print(total)