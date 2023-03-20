# ---------------------
# -- Password player --
# ---------------------

print("Welcome to the password player:- (Version: 1.4)")
print("""- Password must contain at least 8 characters and not more than 12 characters.
- It cannot start with a number and end with a number.
- It must contain at least one uppercase letter and at least one lowercase letter.
- Password must contain numbers
- Cannot contain spaces.
- Password must contain at least one sigma character.
- There should be no duplicate characters in the password.
- Password must start with a capital letter.
- Password must not contain (") or (')
- Password must not contain parentheses""")

tr = "1"
while(tr == "1"):
    password = input("Enter a password: ")

    num = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    sp = " "
    bndsym1 = '"'
    bndsym2 = "'"
    bndsym3 = "("
    bndsym4 = ")"

    # passmora12 = True
    # passless8 = True
    # passendnum = True
    # passstartnum = True
    passupper = True
    passlower = True
    passspace = True
    passsigma = True
    passtekrar = True
    passstartup = False
    passbid = True
    passnum = True

    if len(password) <= 12:
        passmora12 = True
    else:
        passmora12 = False
 
    if len(password) >= 8:
        passless8 = True
    else:
        passless8 = False

    if password.endswith(num):
        passendnum = False
    else:
        passendnum = True

    if password.startswith(num):
        passstartnum = False
    else:
        passstartnum = True

    if sp in password:
        passspace = False

    if True:
        if bndsym1 in password:
            passbid = False
        if bndsym2 in password:
            passbid = False
        if bndsym3 in password:
            passbid = False
        if bndsym4 in password:
            passbid = False

    for i in password:
        if i.isupper():
            passupper = True
            if password.startswith(i):
                passstartup = True
            break
        else:
            passupper = False

        if i.islower():
            passlower = True
            break
        else:
            passlower = False

        if not i.isalnum():
            passsigma = True
            break
        else:
            passsigma = False

        if password.count(i) >= 2:
            passtekrar = False
            break
        else:
            passtekrar = True

        if i.isdigit():
            passnum = True
            break
        else:
            passnum = False

    # for i in password:
    #     if i.islower():
    #         passlower = True
    #         break
    #     else:
    #         passlower = False

    # for i in password:
    #     if not i.isalnum():
    #         passsigma = True
    #         break
    #     else:
    #         passsigma = False

    # for i in password:
    #     if password.count(i) >= 2:
    #         passtekrar = False
    #         break
    #     else:
    #         passtekrar = True

    # for i in password:
    #     if i.isdigit():
    #         passnum = True
    #         break
    #     else:
    #         passnum = False

    #
    passgrup = [passmora12, passless8, passendnum,
                passstartnum, passupper, passlower,
                passspace, passsigma, passtekrar,
                passstartup, passbid, passnum]

    if False in passgrup:
        print("Your password does not match these terms:-")

        if passmora12 == False:
            print("- Password cannot be more than 12 characters")
        if passless8 == False:
            print("- Password cannot be less than 8 characters")
        if passendnum == False:
            print("- Password cannot end in numbers")
        if passstartnum == False:
            print("- Password cannot start with numbers")
        if passupper == False:
            print("- Password must contain at least one capital letter")
        if passlower == False:
            print("- Password must contain at least one lowercase letter")
        if passspace == False:
            print("- Password cannot contain spaces")
        if passsigma == False:
            print("- The password must contain at least one sigma character")
        if passtekrar == False:
            print("- Password must not contain duplicate characters")
        if passstartup == False:
            print("- Password must start with a capital letter")
        if passbid == False:
            print("""- Password must not contain () or ' or " """)
        if passnum == False:
            print("- Password must contain numbers")

        print("Try again..")
    else:
        print("Your password matches the conditions.")
        tr = input("If you want to try another password, press 1 or 0 to exit: ")
