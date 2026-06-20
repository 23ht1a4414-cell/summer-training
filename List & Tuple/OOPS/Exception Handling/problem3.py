'''
a company wants to create a file anazyler 
1.Accept filename from
1.file not found
2.permission denied
3.empty file
Display:
number of lines
number of word

'''
filename = input("Enter file name: ")

try:
    with open(filename, "r") as f:
        data = f.read()

        if len(data.strip()) == 0:
            raise Exception("Empty file")

        lines = data.splitlines()
        words = data.split()

        print("Number of lines:", len(lines))
        print("Number of words:", len(words))

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")

except Exception as e:
    print(e)


