import string as s
import time as t

#texk = "xvkzFWjgzcitzmvcEvibvi"
#texk after = "capeKBolehnyerahJangan"
#sip = 21

#texk = "helloworld!"
#texk after = "spwwzhzcwo!"
#sip = 11

dek = """
dekripsi----------1
enkripsi----------2
keluar------------3
"""

def dekripsi():
    try:
        texk = input("text: ")
        sip = int(input("angka: "))
        a = []

        for dec in texk:
            if dec.islower():
                tek = chr((ord(dec)- ord('a') - sip) %26 + ord('a'))
            elif dec.isupper():
                tek = chr((ord(dec)- ord('A') - sip) %26 + ord('A'))
            elif dec.isdigit():
                tek = chr((ord(dec)- ord('1') - sip) %9 + ord('1'))
            else:
                tek = dec
            
            a.append(tek)  
            tik = ''.join(a)
            t.sleep(0.1)
            print(tik)
        print(f"hasil: {tik} dengan jumlah shift: {sip}")
        print(f"kata sebelum di dekripsi: {texk} ")
        
    except:
        print("rispek")
        print("pokoknya ada yang salah la")

def enkrpsi():
    try:
        texk = input("text: ")
        sip = int(input("angka: "))
        a = []

        for dec in texk:
            if dec.islower():
                tek = chr((ord(dec)- ord('a') + sip) %26 + ord('a'))
            elif dec.isupper():
                tek = chr((ord(dec)- ord('A') + sip) %26 + ord('A'))
            elif dec.isdigit():
                tek = chr((ord(dec)- ord('1') + sip) %9 + ord('1'))
            else:
                tek = dec
            
            a.append(tek)
            tik = ''.join(a)
            t.sleep(0.1)
            print(tik)
        print(f"hasil: {tik} dengan jumlah shift: {sip}")
        print(f"kata sebelum di enkripsi: {texk}")

    except:
        print("rispek")
        print("pokoknya ada yang salah la")
    
def Jalankan():
    print("hai Rakha")

    while True:
        texk = input(f"{dek}enter: ")
        
        if texk == "1":
           a = dekripsi()
           print(a)
        
        elif texk == "2":
          a = enkrpsi()
          print(a)

        elif texk == "3":
          print("dadah")
          break

        else:
            print("takbisala")

if __name__ == "__main__":
    Jalankan()
