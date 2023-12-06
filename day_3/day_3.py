import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class solver():
    lines:list[str]
    valid_nums:list[int]

    def get_content(self)->list[str]:
        with open("input.txt", "r") as file:
            self.lines:list[str]=file.read().split('\n')
        return self.lines

    def is_valid_neighbour(self, line_index, min, max)->bool:
        is_valid:bool=False
        if(line_index>=0 and line_index<len(self.lines)):
            i=min-1
            characters:list[str]=list(self.lines[line_index])
            while i<=max+1:
                try:
                    int(characters[i])
                except:
                    if i>=0 and i<len(characters) and characters[i]!='.':
                        is_valid=True
                i+=1
        return is_valid

    def is_number_valid(self, line_index:int, min:int, max:int)->bool:
        is_valid:bool=False
        try:
            characters:list[str]=list(self.lines[line_index])
        except:
            pass
        else:
            if(characters[min-1]!='.'):
                try:
                    int(characters[min-1])
                except:
                    is_valid=True
                try:
                    int(characters[max+1])
                except:
                    is_valid=True
            if(max<len(characters)-1 and characters[max+1]!='.'):
                try:
                    int(characters[min-1])
                except:
                    is_valid=True
                try:
                    int(characters[max+1])
                except:
                    is_valid=True
            if(is_valid==True):
                print(line_index, min, max, "on")
                is_valid=True
            elif(self.is_valid_neighbour(line_index+1, min, max)==True):
                print(line_index, min, max, "up")
                is_valid=True
            elif(self.is_valid_neighbour(line_index-1, min, max)==True):
                is_valid=True
                print(line_index, min, max, "down")
            else:
                is_valid=False
        return is_valid

    def get_aggregate(self):
        t=0
        for n in self.valid_nums:
            t+=n
        return t
                    
    def find_numbers(self) -> int:
        content=self.get_content()
        self.valid_nums=[]
        k=0
        for line in content:
            i=0
            prev_char:str
            for char in line:
                try:
                    int(char)
                except:
                    pass
                else:
                    print('--------')
                    
                    num_fragment:str=char
                    is_trailing_num:bool=True
                    j=i
                    while is_trailing_num:
                        j+=1
                        try:
                            int(line[j])
                        except:
                            is_trailing_num=False
                        else:
                            num_fragment+=line[j]
                    agg_num:int=int(num_fragment)
                    try:
                        int(prev_char)
                    except:
                        #print(agg_num, i, j)
                        if(self.is_number_valid(k, i, j-1)):
                            self.valid_nums.append(int(num_fragment))
                            print(12345, agg_num)
                i+=1
                prev_char=char
            k+=1
        print(self.valid_nums)
        return self.get_aggregate()

solution:int=solver().find_numbers()
print(solution)

