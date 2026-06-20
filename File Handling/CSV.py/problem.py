'''
CSV--> Comma Seperated Values
used:excel,reports,databases

Example:
name,age,branch
akhil,21,ds
lokesh,20,ds
Anas,20,ds


 '''
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
with open("newfile.txt","r") as file:
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
