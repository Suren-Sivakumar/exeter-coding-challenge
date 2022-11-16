import csv
import shutil
import pandas as pd
import psutil
import time

input_txt_file = open ('t8.shakespeare.txt','r')
txtreader1 = input_txt_file.readlines()

word_list_txt_file = open('find_words.txt','r')
txtreader2 = word_list_txt_file.readlines()

shutil.copyfile('t8.shakespeare.txt','t8.shakespeare.translated.txt')

dict_csv = open("./french_dictionary.csv",'rt')
csvreader = csv.reader(dict_csv)

upd = 1
for j in txtreader2:
    df = pd.read_csv("frequency.csv")
    count = 0
    temp = count
    df.loc[upd, 'English word'] = j.rstrip()
    for k in txtreader1:
        for word1 in k.split():
            if (word1.rstrip()==j.rstrip()):
                count = count + 1
                if (count>temp):
                    temp = count
    df.loc[upd, 'Frequency'] = temp
    df.to_csv("frequency.csv", index=False)
    upd = upd+1

        
upd = 0
for a in csvreader:
    df = pd.read_csv("frequency.csv")
    search_text = a[0]
    replace_text = a[1]
    with open('t8.shakespeare.translated.txt', 'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)
    with open('t8.shakespeare.translated.txt', 'w') as file:
        file.write(data)
    df.loc[upd, 'French word'] = a[1]
    df.to_csv("frequency.csv", index=False)
    upd = upd+1
    

t1 = int(time.process_time())
t2= int(t1/60)
t3= t1%60
t= "Time to process: " + str(t2) + " minutes " + str(t3) + " seconds"
m = "Memory used: " + str(int(psutil.Process().memory_info().rss / (1024 * 1024))) + " MB"

txt = t + "\n" + m
with open('performance.txt', 'w') as file:
    file.write(txt)