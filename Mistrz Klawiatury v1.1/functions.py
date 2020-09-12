import pygame


def str_to_bool(s: str) -> bool:
    if s == 'True':
        return True
    elif s == 'False':
        return False


def get_player_nick(win, input_text):
    font = pygame.font.Font('freesansbold.ttf', 32)  # jakaś domyślna czcionka i rozmiar
    text = font.render(input_text, True, (100, 100, 150), pygame.SRCALPHA)  # renderowanie wpisywanego tekstu
    textRect = text.get_rect()  # pole z wpisywanym tekstem i jego środek
    textRect.center = (540, 360)
    win.blit(text, textRect)  # nałożenie zrenderowanego tekstu na jego pole tekstowe


def add_result(Player_Name: str, score: int,
               Difficulty: str):  # funkcja jako argumenty przyjmuje nick gracza, czas w sekundach oraz
    Player_File = "players/" + str(Player_Name) + "_player.txt"  # poziom trudnosci na ktorym byla rozgrywana gra
    string = str(Difficulty) + " " + str(int(score)) + "\n"
    open(Player_File, "a+").write(string)
    if len(open(Player_File, "r").readlines()) > 1:
        sorting(Player_File)  # funkcja Sorting wywolywana jest automatycznie po dodaniu nowego wyniku do
        # pliku tekstowego


def sorting(Player_File: str):  # Funkcja sortujaca statystyki w pliku tekstowym
    file = open(Player_File, "r+").readlines()
    open(Player_File, "w").close()
    if file is not None:
        result_tuples = []
        for word in file:
            list = word.split()
            tuple = (list[0], float(list[1]))
            result_tuples.append(tuple)
        sorted_results = sorted(result_tuples, key=lambda tuple: tuple[1])
        # sorted_results.reverse()                            #Odkomentowanie tej linii zamieni kolejnosc wypisywania
        sorted_list = []
        for results in sorted_results:
            line = results[0] + " " + str(results[1]) + "\n"
            sorted_list.append(line)
        file = open(Player_File, "r+").writelines(sorted_list)



def get_results(Player_Name: str,
                Difficulty: str):  # funkcja przyjmuje jako argumenty nick gracza, oraz poziom trudnosci, ktory ma zostac
    Player_File = "players/" + str(
        Player_Name) + "_player.txt"  # odczytany (oba typu string) i zwraca tablice 5 najwyzszych wynikow uzyskanych na
    file = open(Player_File, "r+").readlines()  # danym poziomie trudnosci zaczynajac od najlepszego czasu
    Result = []
    for words in file:
        line = words.split()
        array = [str(line[0]), float(line[1])]
        if array[0] == Difficulty:
            Result.append(array[1])
    Result.sort()
    Result.reverse()
    if len(Result) > 5:
        Result = Result[0:5]
    return Result
