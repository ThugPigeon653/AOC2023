
total:int=0

with open("C:\\users\\lneil\\documents\\programming\\aoc2023\\input.txt", "r") as file:
    _text=file.read()
text=_text.split('\n')
for line in text:
    first:int
    last:int
    has_a_f:bool=False
    for character in line:
        try:
            int(character)
        except:
            pass
        else:
            if has_a_f==False:
                first=last=int(character)
                has_a_f=True
            else:
                last=int(character)
    total+=int(str(first)+str(last))

print("-------------------")
print(total)
print("-------------------")