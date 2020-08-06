import pygame
import random




class word_base: #klasa do otwierania bazy słów i losowania nowego słowa
    @staticmethod
    def words_reload(mode: str, language: str) -> list:
        if mode == "easy" and language == "polish":
            return open("word_base/easy_pol.txt", "r", encoding='utf8').readline().split(" ")
        elif mode == "medium" and language == "polish":
            return open("word_base/medium_pol.txt", "r", encoding='utf8').readline().split(" ")
        elif mode == "hard" and language == "polish":
            return open("word_base/hard_pol.txt", "r", encoding='utf8').readline().split()
        elif language != "polish":
            return ["ERROR"]


    @staticmethod
    def get_randWord(word_base: list, previous_word: str) -> str:
        rand = random.randint(0, len(word_base)-1)
        if previous_word is None:
            return word_base[rand]
        else:
            while word_base[rand] == previous_word:
                rand = random.randint(0, len(word_base) - 1)
            previous_word = word_base[rand]
            return word_base[rand]



