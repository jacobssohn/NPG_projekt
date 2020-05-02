
def Add_Result(Name, Time):
    string =Name + " " + str(Time) + "\n"
    open("statistics.txt","a+").write(string)
    if len(open("statistics.txt","r").readlines())>1:
        Sorting()

def Sorting():
    file = open("statistics.txt", "r+").readlines()
    open("statistics.txt","w").close()
    result_tuples=[]
    for word in file:
        list = word.split()
        tuple=(list[0],float(list[1]))
        result_tuples.append(tuple)
    sorted_results = sorted(result_tuples, key= lambda tuple: tuple[1])
    'sorted_results.reverse()'  'Odkomentowanie tej linii zamieni kolejnosc wypisywania'
    sorted_list=[]
    for results in sorted_results:
        line = results[0] + " " + str(results[1]) +"\n"
        sorted_list.append(line)
    file = open("statistics.txt","r+").writelines(sorted_list)

def Get_Results():
    file = open("statistics.txt","r").readlines()
    list = []
    new_list = []
    for words in file:
        line = words.split()
        array = [line[0], float(line[1])]
        list.append(array)
    if len(list) > 10:
        for i in range(0,10):
            new_list.append(list[i])
        return new_list
    else:
        for i in range(0,len(list)):
            new_list.append(list[i])
        return new_list

