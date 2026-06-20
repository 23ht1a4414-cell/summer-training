'''
A company stores server logs in a files:
write a python program:
1.read log.txt:
2.count:
total lines
Error messages
Warning messages
Info Messages
display analysis report

'''

try:
            with open("log.txt", "r") as file:
                lines = file.readlines()
                total_lines = len(lines)
                error_count = 0
                warning_count = 0
                info_count = 0

                for line in lines:
                    if "ERROR" in line:
                        error_count += 1
                    elif "WARNING" in line:
                        warning_count += 1
                    elif "INFO" in line:
                        info_count += 1

                    print("Log Analysis Report:")
                    print("Total Lines:", total_lines)
                    print("Error Messages:", error_count)
                    print("Warning Messages:", warning_count)
                    print("Info Messages:", info_count)
                else:
                      print("no data")
   
except FileNotFoundError:
            print("File was not existed")
      
            