import os
import string
#--------------------------------------------1
def inf_about_path():
    path = 'C:\Users\koshi\Documents\python'
    print("Directories:")
    print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
    print("Files:")
    print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
    print("Directories and files :")
    print([ name for name in os.listdir(path)])
#--------------------------------------------2
def check_for_access():
    print('Exist:', os.access("C:\Users\koshi\Documents\Книги\Data Science from Scratch First Principles with Python, 2nd edition [2019] Grus J..epub", os.F_OK))
    print('Readable:', os.access("C:\Users\koshi\Documents\Книги\Data Science from Scratch First Principles with Python, 2nd edition [2019] Grus J..epub", os.R_OK))
    print('Writable:', os.access("C:\Users\koshi\Documents\Книги\Data Science from Scratch First Principles with Python, 2nd edition [2019] Grus J..epub", os.W_OK))
    print('Executable:', os.access("C:\Users\koshi\Documents\Книги\Data Science from Scratch First Principles with Python, 2nd edition [2019] Grus J..epub", os.X_OK))
#--------------------------------------------3
def check_path_exist():
    print("Test a path exists or not:")
    path = r'g:\\testpath\\a.txt'
    print(os.path.exists(path))
    path = r'g:\\testpath\\p.txt'
    print(os.path.exists(path))
    print("File name of the path:")
    print(os.path.basename(path))
    print("Dir name of the path:")
    print(os.path.dirname(path))
#--------------------------------------------4
def readlines_count():
    with open(r"myfile.txt", 'r') as file:
        lines = len(file.readlines())
        print('Total Number of lines:', lines)
#--------------------------------------------5
def write_list_to_file():
    items = ['a ', 'b ', 'c ', 'd ', 'e ']
    file = open('letters.txt','w')
    file.writelines(items)
    file.close()
#--------------------------------------------6
def generate_26_text_files():
    if not os.path.exists("letters"):
       os.makedirs("letters")
    for letter in string.ascii_uppercase:
       with open(letter + ".txt", "w") as f:
           f.writelines(letter)
#--------------------------------------------7
def append_of_files():
    with open('first.txt', 'r') as firstfile, open('second.txt', 'a') as secondfile:
        for line in firstfile:
            secondfile.write(line)
#--------------------------------------------8
def del_file():
    if os.path.exists("demofile.txt"):
      os.remove("demofile.txt")
    else:
      print("The file does not exist")

