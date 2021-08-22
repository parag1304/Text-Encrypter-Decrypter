import encrypter
import decrypter
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
