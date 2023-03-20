# -----------------------------
# -- Goffy encryption system --
# -----------------------------
# Please note that this encryption system is mine and it is not allowed to modify it at all or attribute it to another person, and violating that exposes you to legal accountability
# You can send this code to your friends and use it to encrypt and translate messages between you (:

ar_en = {"أ": "h", "ب": "f", "ت": "j", "ث": "e", "ج": "[", "ح": "p", "خ": "o", "د": "]",
         "ذ": "`", "ر": "v", "ز": ".", "س": "s", "ش": "a", "ص": "w", "ض": "q", "ط": "'", "ظ": "/",
         "ع": "u", "غ": "y", "ف": "t", "ق": "r", "ك": ";", "ل": "g", "م": "l", "ن": "k", "ه": "i", "و": ",",
         "ي": "d",    "ا": "h", "ئ": "z", "ء": "x", "ؤ": "c", "ى": "n", "ة": "m", }

en_ar = {"a": "ش", "b": "لا", "c": "ؤ", "d": "ي", "e": "ث", "f": "ب", "g": "ل", "h": "ا", "i": "ه", "j": "ت", "k": "ن",
         "l": "م", "m": "ة", "n": "ى", "o": "خ", "p": "ح", "q": "ض", "r": "ق", "s": "س", "t": "ف", "u": "ع", "v": "ر",
         "w": "ص", "x": "ء", "y": "غ", "z": "ئ"}


def Encryption():
    while True:
        print("Choose the language:-")
        print("- AR to EN [1]")
        print("- EN to AR [2]")
        select = input("> Choose: ")
        cum = []
        if select == "1":
            sentence1 = input("Enter the Arabic sentence: ")
            for i in sentence1:
                if i in ar_en:
                    cum.append(ar_en[i])
                else:
                    cum.append(i)
            print("".join(cum))
        elif select == "2":
            sentence2 = input("Enter the English sentence: ")
            for i in sentence2:
                if i in en_ar:
                    cum.append(en_ar[i])
                else:
                    cum.append(i)
            print("".join(cum))
        else:
            print("Wrong choice, please try again..")
        print("---------------------------------------")

        c_r = input(
            "To continue press 1, and to return to the main menu press 0: ")
        if c_r == "0":
            print("---------------------------------------")
            break


def Translation():
    print("Please type the text you want to translate")
    sentence = input("> ")
    cum = []
    keys = []
    values = []

    for i in sentence:
        if i in ar_en:
            keys = list(en_ar.keys())
            values = list(en_ar.values())
            break
        if i in en_ar:
            keys = list(ar_en.keys())
            values = list(ar_en.values())
            break

    for i in sentence:
        if i in values:
            cum.append(keys[values.index(i)])
        else:
            cum.append(i)

    print("".join(cum))
    print("---------------------------------------")


print("---------------------------------------")
print("Welcome to the Goffy encryption system")
print("Version: 1.2v")
print("---------------------------------------")
while True:
    print("- Encryption [1]")
    print("- Translation [2]")
    print("- Exit [3]")
    sel = input("> Choose: ")
    print("---------------------------------------")
    if sel == "1":
        Encryption()
    elif sel == "2":
        Translation()
    elif sel == "3":
        print("Thanks for using Goffy's encryption system..")
        print("---------------------------------------")
        exit()
    else:
        print("Wrong choice, please try again..")
        print("---------------------------------------")
