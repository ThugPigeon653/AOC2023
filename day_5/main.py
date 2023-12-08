class AlmamacReader():
    __seeds:list[int]=[]
    __maps:list[list[list[int]]]=[]
    def __init__(self):
        plaintext:str=self.get_input()
        maps=plaintext.split(':')
        del maps[0]
        seeds=maps[0].strip(' ').split(' ')
        for seed in seeds:
            try:
                self.__seeds.append(int(seed))
            except Exception as e:
                self.show_warning(f"non-numerical character detected in seeds.\n{e}")
        del maps[0]
        for m in maps:
            lines:list[str]=m.strip().split('\n')
            numlines:list[list[int]]=[]
            for line in lines:
                numline:list[int]=[]
                units:list[str]=line.strip().replace('  ', ' ').split(' ')
                for unit in units:
                    try:
                        numline.append(int(unit))
                    except Exception as e:
                        self.show_warning(e)
                numlines.append(numline)
            self.__maps.append(numlines)
        print("22222")
        print(len(self.__maps))
        for map in self.__maps:
            print('penis')
            seeds=self.remap(map, self.__seeds)
            print(min(seeds))

    @staticmethod
    def show_warning(warning:str):
        print(f"--WARNING-- {warning}")

    @staticmethod
    def get_input(path:str="input.txt")->str:
        with open(path, "r") as file:
            return file.read()
    
    @staticmethod
    def remap(map:list[list[int]], seeds:list[int])->list[int]:
        destination:list[int]=[]
        for line in map:
            if len(line)==3:
                for seed in seeds:
                    if seed>=line[1] and seed<line[1]+line[2]:
                        destination.append(seed+(line[0]-line[1]))
        print(destination)
        return destination

AlmamacReader()