'''
files helps store data permanently

File Handling:
The process of
1.Creating files
2.reading the files
3.writing files
4.updating files
using python

Why file handling?
Data disappears after the program ends
with files:
1.store data perm
2.data sharing possible
3.reports/logs can be generated

TYPES of FILES:
#1.Text files:
1..txt
2..csv
3..py
4..json

#2.Binary files:
1.images
2.videos
3.pdf's

'''
#opening the files
#Syntax:

#file = open("Filename","mode")


#r will tell python that line don't have any escapling characters
from csv import excel
from optparse import Values
from os import name


file = open(r"file handling/main.py","r")
print(file)
'''
File Models
Mode      Meaning
r         read
w         write
a         append
x         create
r+        read+write
w+        write+read
a+        append+read
rb        read binary
wb        write binary

'''
try:

   file = open(r"c:\Users\venka\OneDrive\Desktop\summer training\File Handling\main.py", "r")
   data =file.read()
   print(file)
   file.close()
except FileNotFoundError as e:
   print("No file found")

#write mode - w

file = open(r"c:\Users\venka\OneDrive\Desktop\summer training\File Handling\main.py", "r")
#file.write("Hello students")
file.close()

#create files if not exist
#deletes the old and new content

#append - mode
#file = open(r"c:\Users\venka\OneDrive\Desktop\summer training\File Handling\data.txt","r")
#file.write(" \nHow are you")
#file.close()
'''
#create mode:x
#file = open("newfile.txt","x")

#gives fileExistsError if alread exists

#read()
file = open("newfile.txt","r")
print(file.read())
file.close()

#read lines()
file = open("newfile.txt","r")
print(file.readline())
file.close()
'''
'''
#3.readlines()-reads multiple lines
file = open("newfile.txt","r")
lines = file.readlines()
print(lines)
file.close()
#write() -->writes the data to file
file = open("newfile.txt","w")
file.write("loki\n")
file.write("lokesh\n")
file.close()

#writelines():writes list data
names =[
    "loki\n",
     "anas"
]
file = open("newfiles.txt","w")
file.writelines(names)
file.close()

#pointer methods:
#returns the current cursor position
#tell()
file = open("newfiles.txt","r")
print(file.tell())
file.read(5)
print(file.tell())
file.close()
'''
'''
#seek():moves the cursor position
file = open("newfiles.txt","r")
file.seek(3)
print(file.read())
file.close()


#with open()

with open("newfiles.txt","r") as file:
   print(file.read())
''
#automatic closing 

#student record system
name = input("enter student name:")
marks = input("enter marks")
with open("newfile.txt","a") as file:
   file.write(name + ""+ marks + "\n")
   print("record saved")

'''
#CSV: Comma Seperated Values
#used:excel,reports,databases

#Example:
#name,age,branch
#akhil,21,ds
#lokesh,20,ds
#Anas,20,ds


 
import csv
with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age","Branch"])
    writer.writerow(["Rahul","23","CSE"])
    writer.writerow(["Lokesh","21","DS"])


#Read CSV
with open("students.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Binary file handling
file = open("hamster.jpg","rb")
data = file.read()
print(data)
file.close( )


#task1:count words in a file
with open("newfiles.txt","r") as file:
    data = file.read()
    words = data.split()
    print("Number of words:", len(words))

#task2:count lines in a file
with open("newfiles.txt","r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

#task3:search a word in a file
search_word = input("Enter a word to search: ")
with open("newfiles.txt","r") as file:
    data = file.read()
    if search_word in data:
        print(f"{search_word} found in the file.")
    else:
        print(f"{search_word} not found in the file.")
#task4:copy one file to another
with open("newfiles.txt","r") as source_file:
    data = source_file.read()
    with open("copy.txt","w") as dest_file:
        dest_file.write(data)

#task5:count characters in a file
with open("newfiles.txt","r") as file:
    data = file.read()
    print("Number of characters:", len(data))
    

