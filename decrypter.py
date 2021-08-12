#program for decryption
def decrypt():
     print("Enter message you want to encrpyt")
     mess = input()
     acssi_value = []
     for character in mess:
         acssi_value.append(ord(character))
    

     encrypted_acssi_value = []
     encrypted_acssi_value = acssi_value
     length = len(acssi_value)

     for i in range( len(encrypted_acssi_value)):
        encrypted_acssi_value[i] = encrypted_acssi_value[i] - 1  
        

     res = ""
     for val in encrypted_acssi_value:
         res = res + chr(val)
     print(res)
