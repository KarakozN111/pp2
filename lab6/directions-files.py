#ex1
import os
path = 'g:\\testpath\\'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])
#ex2
import os
print('Exist:', os.access('c:\\Users\\Public\\C programming library.docx', os.F_OK))
print('Readable:', os.access('c:\\Users\\Public\\C programming library.docx', os.R_OK))
print('Writable:', os.access('c:\\Users\\Public\\C programming library.docx', os.W_OK))
print('Executable:', os.access('c:\\Users\\Public\\C programming library.docx', os.X_OK))
#ex3
import os
print("Test a path exists or not:")
path = r'g:\\testpath\\a.txt'
print(os.path.exists(path))
path = r'g:\\testpath\\p.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))
#ex4
def file_lengthy(filename):
        with open(filename) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines: ",file_lengthy("test.txt"))
#ex5
fruits = ['apple', 'banana', 'cherry', 'papaya']
with open('abc.txt', "w") as myfile:
        for c in fruits:
                myfile.write("%s\n" % c)
content = open('abc.txt')
print(content.read())
#ex6
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)
#ex7
from shutil import copyfile
copyfile('test.py', 'some.py')
#ex8
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
