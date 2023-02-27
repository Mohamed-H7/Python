# -------------------------------
# -- System (binary - decimal) --
# -------------------------------

while(True):

    print("""Welcome to "TABAN DEĞİŞTİRME"
- İkilik tabandan onluk tabana çevirme için [1]
- Onluk tabandan ikilik tabana çevirme için [2]
- Çıkış için [3]""")
    s = input("\nseçiniz: ")

    if s == "1":
        print("- Not: Girilen sayı yalnızca 0 ve 1'i içermelidir")
        s1 = "1"
        while(s1 == "1"):
            L = input("İkili sistemde bir sayı giriniz: ")
            valid = True

            for n in L:
                if n != "0" and n != "1":
                    valid= False

            if valid:
                O = int(L)
                i = res = 0
                while O != 0:
                    res = res+(O % 10)*(2**i)
                    O = O//10
                    i += 1
                    G = 1
                print("Ondalık sistemdeki sayı eşittir = ", res)
                s1 = input("""
- İkili sistemle devam etmek için [1]
- Ana menüye dönmek için [2]
seçiniz: """)
            else:
                print("Girilen değer yanlış, lütfen tekrar deneyin")

##########################################
    elif s == "2":
        s2 = "1"
        while s2 == "1":
            N = int(input("Ondalık sistemde bir sayı giriniz : "))
            i = hes = 0
            while N != 0:
                hes = hes + (N % 2)*(10**i)
                N = N//2
                i += 1
            print(f"Sayı ikili sistemde eşittir = {hes}")
            s2 = input("""
- Ondalik sistemle devam etmek için [1]
- Ana menüye dönmek için [2]
seçiniz: """)

    elif s == "3":
        print("Teşekkür ederiz")
        break

    else:
        print("yanlış giriş, Lütfen tekrar giriniz\n")
