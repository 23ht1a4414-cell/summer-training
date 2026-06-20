'''
A university wants to automate student result processsing
The program should accept:
1.marks of 5 subjects
2.raise exeception
if
1.marks are negative
2.marks exceed 100
3.non-numeric input
4.calculate average and grade
rules:
avg >=75-->distinction
avg >=65 -->first class
avg >=40 -->pass

'''
class InvalidMarksError(Exception):
    pass
class StudentResult:
    def __init__(self):
        self.marks =[]

    def input_marks(self):
        try:
            for i in range(5):
                mark =int(
                    input(f"enter subject {i+1} marks:")
                    )

                if mark < 0 or mark > 100:
                    raise InvalidMarksError("Marks should be b/w 0 and 100")
                self.marks.append(mark)
            avg =sum(self.marks)/5
            print("avg:",avg)
            if avg >=75:
                print("Distinction")
            elif avg >=60:
                print("frist class")
            elif avg>=40:
                print("pass")
            else:
                print("fail")
        except ValueError:
            print("only numerics are allowed")
        except InvalidMarksError as e:
            print(e)
s1 =StudentResult()
s1.input_marks()

       
