'''
#problem3.py
word frequency analyzer
a company wants to analyze the text
write a python program:
1.read content from data.txt
2.count the frequency of each word
3.display the most repeated word
4.handle the exception
'''

try:
    with open("newfiles.txt", "r") as file:
        words = file.read().lower().split()
    freq ={}
    for word in words:
        freq[word] = freq.get(word,0) + 1
    word = max(freq, key = freq.get)

    print("most repeated word:",word)
    print("freq:",freq[word])
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print("Error:", e)


        
