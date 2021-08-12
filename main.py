from encrypter import encrpyt
from decrypter import decrypt
while(True):
    print("HI, Do you want to encrpyt(e) or decrypt(d) or exit(ex) ")
    choice = input()
    if choice == "e" :
        encrpyt()
    elif choice == "d" :
        decrypt()
    elif choice == "ex" :
        exit()
    else :
        print("Wrong Choice")
