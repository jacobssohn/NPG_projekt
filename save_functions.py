def Add_Result(Player_Name:str, Time:float, Difficulty:str): #funkcja jako argumenty przyjmuje nick gracza, czas w sekundach oraz
    Player_File = str(Player_Name) + ".txt"    #poziom trudnosci na ktorym byla rozgrywana gra
    string = str(Difficulty) + " " + str(float(Time)) + "\n"
    open(Player_File,"a+").write(string)
    if len(open(Player_File,"r").readlines())>1:
        Sorting(Player_File)                   #funkcja Sorting wywolywana jest automatycznie po dodaniu nowego wyniku do
                                               #pliku tekstowego

def Sorting(Player_File:str):                      #Funkcja sortujaca statystyki w pliku tekstowym
    file = open(Player_File, "r+").readlines()
    open(Player_File,"w").close()
    if file != None:
        result_tuples=[]
        for word in file:
            list = word.split()
            tuple=(list[0],float(list[1]))
            result_tuples.append(tuple)
        sorted_results = sorted(result_tuples, key= lambda tuple: tuple[1])
        #sorted_results.reverse()  #Odkomentowanie tej linii zamieni kolejnosc wypisywania
        sorted_list=[]
        for results in sorted_results:
            line = results[0] + " " + str(results[1]) +"\n"
            sorted_list.append(line)
        file = open(Player_File,"r+").writelines(sorted_list)

def Get_Results(Player_Name:str, Difficulty:str):      #funkcja przyjmuje jako argumenty nick gracza, oraz poziom trudnosci, ktory ma zostac
    Player_File = str(Player_Name) + ".txt"    #odczytany (oba typu string) i zwraca tablice 5 najwyzszych wynikow uzyskanych na
    file = open(Player_File,"r+").readlines()  #danym poziomie trudnosci zaczynajac od najlepszego czasu
    Result = []
    for words in file:
        line = words.split()
        array = [str(line[0]),float(line[1])]
        if array[0] == Difficulty:
            Result.append(array[1])
    if len(Result) > 5:
        Result = Result[0:5]
    return Result


