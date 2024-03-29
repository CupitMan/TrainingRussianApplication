import csv
import os


# -*- coding: utf-8 -*-
class FileWorker():
    def __init__(self, name1, name2):

        # Documents: All - all words; Hard - only hard words
        # These variables contain names of csv-files
        self.DocumentAll = name1
        self.DocumentHard = name2


    def addition(self, word, name):

        # Choose the name csv-file
        if name == 'all':
            path = self.DocumentAll
        else:
            path = self.DocumentHard

        flag = True
        # Check the word in dictionary
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for i in reader:
                if i[0] == word:
                    flag = False

        # Add new word
        if flag:
            with open(path, 'a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([word])


    def print_document(self, name):
        
        # Choose the name csv-file
        if name == 'all':
            path = self.DocumentAll
        else:
            path = self.DocumentHard
            
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for i in reader:
                print(i)


    def delete(self, word, name):
        # Choose the name csv-file
        if name == 'all':
            path = self.DocumentAll
        else:
            path = self.DocumentHard

        temp = []

        # Temp will contain need words
        with open(path, 'rb', encoding='utf-8') as file:
            reader = csv.reader(file)
            for i in reader:
                if i[0] != word:
                    temp.append(i)

        # Write words from temp
        with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for i in temp:
                writer.writerow(i)


    def get_words(self, name):
        # Choose the name csv-file
        if name == 'all':
            path = self.DocumentAll
        else:
            path = self.DocumentHard

        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            result = []
            if path == 'hard.csv':
                if (os.stat("hard.csv").st_size != 0):
                    for i in reader:
                        result.append(i[0])
            else:
                for i in reader:
                    result.append(i[0])
            return result
    





