# TEXT FILE HANDLING
# --------------------------------------------------------------------------------------------------------------------
# C:\Python\File_handling.py\First.txt
# Print File:-
# f = open(r"C:\Python\File_handling.py\First.txt", 'r')
# print(f.name)

# f = ("C:\Python\File_handling.py\First.txt")
# print(f)

# file = (r"C:\Python\File_handling.py\First.txt")
# print(file)                          # print file path

# f = open("C:\Python\File_handling.py\First.txt", "r")
# print(f.mode)                # print file mode

# f = open("C:\Python\File_handling.py\First.txt", "r")
# res = f.read()
# print(res)          # print all lines from file

# f = open("C:\Python\File_handling.py\First.txt", 'r')
# print(f.readable())                        # it check whether user can read the file or not- True or False

# file_path = "C:\Python\File_handling.py\First.txt"
# f = open("C:\Python\File_handling.py\First.txt")
# print(f.readline())          # it print first line
# op-
# Files are very common permanent storage areas to store our data.

# f = open("C:\Python\File_handling.py\First.txt", 'r')
# print(f.readline(10))            # File are

# f = open("C:\Python\File_handling.py\First.txt", "r")
# print(f.readlines())                    # print all lines in a list

# f = open("C:\Python\File_handling.py\First.txt", 'r')
# print(f.readlines(3))                  # if pass any argument in it print first line


# f = open("C:\Python\File_handling.py\First.txt", 'r')
# print(f.seekable())             # True

# f = open("C:\Python\File_handling.py\First.txt", "r")
# print(f.writable())            # Flase

# f = open("C:\Python\File_handling.py\First.txt", 'r')
# print(f._checkClosed())                        # None

# f = open("C:\Python\File_handling.py\First.txt", 'r')
# print(f.fileno())                      # 3

# f = open("C:\Python\File_handling.py\First.txt", 'r')
# print(f.closed)         # False

# f = open("C:\Python\File_handling.py\First.txt", 'r')
# print(f.closed)
# f.close()
# print(f.closed)
# -------------------------------------------------------------------------------------------------------
# Read Example:-

# ***********************************************************
# FILE_PATH =r"C:\Python\File_handling.py\First.txt"
# f = open(FILE_PATH, "r")
# # # ************************************************************

# def get_sum_of_numbers():
#     data = f.read().split()
#     total = 0
#     for word in data:
#         if word.isdigit():
#             total += int(word)
#             print(word)
#     print(total)

# get_sum_of_numbers()
# # op- 
# # 1
# # 2
# # 3
# # 6
# ----------------------------------------------------------------

# def get_line_by_word(word):
#     lines = f.readlines()
#     for index in range(0, len(lines)):
#         if word in lines[index]:
#             print(index+1)

# get_line_by_word("operation")

# # op-
# # 3
# # 4
# # 5
# ---------------------------------------------------------------------

# def get_word_occ_with_count(word, case_sensetive=False):
#     data = f.read()
#     if case_sensetive:
#         print(data.split().count(word))
#     else:
#         final = data.lower()
#         print(final.split().count(word.lower()))

# print(get_word_occ_with_count("operation.", False))

# # op-
# # 3
# # None
#------------------------------------------------------------------------- 

# def get_word_occ_without_count(word, case_sensetive=False):
#     data = f.read()
#     if case_sensetive:
#         splitted_data1 = data.split()
#         count = 0
#         for w in splitted_data1:
#             if word == w:
#                 count += 1
#         return count
#     else:
#         splitted_data2 = data.lower().split()
#         count = 0
#         word = word.lower()
#         for w in splitted_data2:
#             if word == w:
#                 count += 1
#         return count

# print(get_word_occ_without_count("operation.", False))

# op-
# 3
# ---------------------------------------------------------------------------

# def get_word_occ_without_count(word, case_sensetive=False):
#     data = f.read()
#     if case_sensetive:
#         splitted_data = data.split()
#     else:
#         splitted_data = data.lower().split()
#         word = word.lower()
#     count = 0
#     for w in splitted_data:
#         if word == w:
#             count += 1
#     return count

# print(get_word_occ_without_count("file", False))

# # op-4
# ---------------------------------------------------------------------

# def get_no_of_words():
#     # return len(f.read().split())
#     data = f.readlines()
#     total = 0
#     for line in data:
#         splitted_line = line.split()
#         total += len(splitted_line)
#     return total

# print(get_no_of_words())

# # op-47
# ---------------------------------------------------------------

# def no_of_lines():
#     return len(f.readlines())

# print(no_of_lines())

# # op- 5
# ------------------------------------------------------------------

# data = f.readline()[::-1]
# print(data)

# data = f.readline()
# print(data)

# op-
# .atad ruo erots ot saera egarots tnenamrep nommoc yrev era seliF

# op-
# Types of files are text file and binary files.
# ---------------------------------------------------------------------

# data = f.read()[::-1]
# print(data)


# # op-
# # .noitarepo dneppa rof elif gnitsixe na nepo a 3
# # .noitarepo etirw rof elif gnitsixe na nepo w 2
# # .noitarepo daer rof elif gnitsixe na nepo r 1
# # .selif yranib dna elif txet era selif fo sepyT
# # .atad ruo erots ot saera egarots tnenamrep nommoc yrev era seliF
# -----------------------------------------------------------------------
# def get_opened_file(FILE_PATH):
#     try:
#         f = open(FILE_PATH, "r")
#         return f
#     except FileNotFoundError:
#         return "File is not present."

# f = get_opened_file(FILE_PATH)
# print(f)
# ----------------------------------------------------------------------------------------------------------
# Write Example:-


# f = open("C:\Python\File_handling.py\second.txt", 'w')
# f.write("Abhishek")
# ---------------------------------------------------------------

# f = open("C:\Python\File_handling.py\second.txt", "w")
# print(f.writable())             # True
# --------------------------------------------------------------

# f = open("C:\Python\File_handling.py\second.txt","w")
# print(f.fileno())            # 4
# ---------------------------------------------------------------

# f = open("C:\Python\File_handling.py\second.txt", 'w')
# print(f.mode)                # w
# ---------------------------------------------------------------

# f = open("C:\Python\File_handling.py\second.txt", 'w')
# print(f.name)                    # print file name
# ---------------------------------------------------------------

# f = open("C:\Python\File_handling.py\second.txt","w")
# print(f.write("abc\n"))
# print(f.write("pqr\n"))
# print(f.write("xyz"))
# ---------------------------------------------------------------

# f = open("C:\Python\File_handling.py\second.txt", 'w')
# l1 = ["Read\n", "Write\n", "Append"]
# f.writelines(l1)
# ---------------------------------------------------------------

# f = open("C:\Python\File_handling.py\second.txt", "a")
# f.write("Read")
# f.write("Seek")
# ----------------------------------------------------------------
# *************************************************************
# f = open("C:\Python\File_handling.py\second.txt", "a")
# *************************************************************

# while True:
#     user_inp = input("Enter ur name:- ")
#     if user_inp.lower() in ["exit"]:
#         print("Thanks..!")
#         break
#     else:
#         f.write(user_inp + "\n")


# print(f.writable())
# -----------------------------------------------------------------
# class Employee:
#     def __init__(self, eid, ename, esal):
#         self.EmpID = eid
#         self.EmpName = ename
#         self.EmpSalary = esal

# e1 = Employee(101, "ABC", 25000)
# e2 = Employee(102, "XYZ", 15000)
# e3 = Employee(103, "PQR", 58000)
# e4 = Employee(104, "JKL", 45000)

# emp_list = [e1, e2, e3, e4]

# f.write("EmpID\t\tEmpName\t\tEmpSalary\n")

# for emp in emp_list:
#     f.write(f"{emp.EmpID}\t\t\t{emp.EmpName}\t\t\t{emp.EmpSalary}\n")

# ----------------------------------------------------------------------

# seek- to move cursor(file pointer) to specified location.
# f = open("C:\Python\File_handling.py\First.txt", 'r')
# print(f.seek(90))
# print(f.read())
# print(f.seek(2))
# print(f.read())

# tell- to return current position of the cursor from beginning of the line.
# f = open("C:\Python\File_handling.py\First.txt",'r')
# print(f.tell())
# print(f.read(4))
# print(f.tell())
# print(f.read(6))
# op-
# 0
# File
# 4
# s are
# -----------------------------------------------------------------------

# context management

# with open(r"C:\Python\File_handling.py\First.txt", "r") as file:
    # print(file.read())
    # print(file.closed)

# --------------------------------------------------------
# user defined context manager  -- __enter__, __exit__
# ---------------------------------------------------------
# class ContextManager:
#     def __init__(self):
#         print('init method called')
         
#     def __enter__(self):
#         print('enter method called')
#         return self
     
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         print('exit method called')
 
# with ContextManager() as manager:
#     print('with statement block')

# --------------------------------------------------------------
# class FileManager():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
         
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
     
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         self.file.close()
# ----------------------------------------------------------------
# pickling and unpickling


# import pickle

# class Employee:
#     def __init__(self, eid, ename, esal):
#         self.EmpID = eid
#         self.EmpName = ename
#         self.EmpSalary = esal

# e1 = Employee(101, "ABC", 25000)
# e2 = Employee(102, "XYZ", 15000)
# e3 = Employee(103, "PQR", 58000)
# e4 = Employee(104, "JKL", 45000)



# f = open(r"C:\Python\File_handling.py\emp_objs_data.dat", "wb")
# pickle.dump(e1, f)  

# f = open(r"C:\Python\File_handling.py\emp_objs_data.dat", "rb")
# data = pickle.load(f)
# print(data.__dict__)
# -------------------------------------------------------------------
# import pickle
  
# def storeData():
#     Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 'age' : 21, 'pay' : 40000}
#     Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak', 'age' : 50, 'pay' : 50000}
#     db = {}
#     db['Omkar'] = Omkar
#     db['Jagdish'] = Jagdish
#     # print(db)
#     # Its important to use binary mode
#     dbfile = open(r"C:\Python\File_handling.py\geeks_data.txt", 'ab')
      
#     pickle.dump(db, dbfile)                     
#     dbfile.close()
  
# def loadData():
#     dbfile = open(r'C:\Python\File_handling.py\geeks_data.txt', 'rb')     
#     db = pickle.load(dbfile)  # python
#     for keys in db:
#         print(keys, '=>', db[keys])
#     dbfile.close()
  
# # if __name__ == '__main__':
# #     storeData()
# #     loadData()

