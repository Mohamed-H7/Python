# -------------------------------
# -- Count letters and numbers --
# -------------------------------
# يستعمل هذا الكود لمعرفة عدد الاحرف او الارقام الموجودة داخل الملف
# يوجد دالة ايضا لمعرفة كم سطر داخل الملف
# يجب استدعاء الدالة ووضع اسم الملف ولكن بدون صيغة الملف فقط الاسم

def num_of_characters(file_name): 

    letters_big = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                   "S", "T", "Y", "V", "W", "X", "Y", "Z"]

    letters_small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                     "s", "t", "y", "v", "w", "x", "y", "z"]

    file_r = open(f"{file_name}.txt", "r")
    line = file_r.read()
    count_letter = 0

    for i in line:
        if i in letters_small or i in letters_big:
            count_letter += 1

    print("Character count: ", count_letter)
    file_r.close()


def num_of_digits(file_name):
    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    file_r = open(f"{file_name}.txt", "r")
    line = file_r.read()
    count_number = 0

    for i in line:
        if i in number:
            count_number += 1

    print("number of digits: ", count_number)
    file_r.close()


def line(file_name):
    file_r = open(f"{file_name}.txt", "r")
    line = file_r.readlines()

    print("The number of lines: ", len(line))
    file_r.close()


num_of_characters("file_name")
num_of_digits("file_name")
line("file_name")
# Put the file name in place of "file_name".
