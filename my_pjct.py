import csv
import pandas as pd
import shutil
import psutil
import time

txtreader = open('find_words.txt','r').readlines()
shutil.copyfile('t8.shakespeare.txt','t8.shakespeare.translated.txt')
csvreader = csv.reader(open("french_dictionary.csv",'r'))

df = pd.read_csv("frequency.csv")
upd = 0
for a in csvreader:
    for j in txtreader:
        if (j.rstrip() == a[0]):
            df.loc[upd, 'English word'] = a[0]
            df.loc[upd, 'French word'] = a[1]
            with open('t8.shakespeare.translated.txt', 'r') as file:
                data = file.read()
                df.loc[upd, 'Frequency'] = data.count(a[0])
                data = data.replace(a[0], a[1])
            with open('t8.shakespeare.translated.txt', 'w') as file:
                file.write(data)
            
            df.to_csv("frequency.csv", index=False)  
    upd = upd+1

t1 = 0
t1 = time.process_time()

with open('performance.txt', 'w') as file:
    file.write("Time to process: " + str(int(t1/60)) + " minutes " + str(int(t1%60)) + " seconds" + "\n" + "Memory used: " + str(int(psutil.Process().memory_info().rss / (1024 * 1024))) + " MB")