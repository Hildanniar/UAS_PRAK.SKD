import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES #import kriptografi AES

#mengambil nilai Key
def getKey(keysize):
    key = os.urandom(keysize)
    return key

def getIV(blocksize):
    iv = os.urandom(blocksize)
    return iv

#fungsi enkripsi gambar
def encrypt_image(filename, key, iv):
    BLOCKSIZE = 16 
    #enkripsi nama file gambar dengan menambah encypted_ pada filenya
    encrypted_filename = "encrypted_" + filename 
    #open gambar
    with open(filename, "rb") as file1: 
        data = file1.read()

#program untuk enkripsi gambar dengan AES
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(data, BLOCKSIZE))
        #membuka file encrypted_filename tadi sebagai file 2
        with open(encrypted_filename, "wb") as file2: 
            file2.write(ciphertext)
    return encrypted_filename

# tahap dekripsi sama seperti enkripsi tapi berbeda di proses dekripsi dari file gambar tsb
def decrypt_image(filename, key, iv):
    BLOCKSIZE = 16
    decrypted_filename = "decrypted_" + filename

    with open(filename, "rb") as file1:
        data = file1.read()
        cipher2 = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher2.decrypt(data), BLOCKSIZE) #proses Deskripsi
    with open(decrypted_filename, "wb") as file2:
        file2.write(decrypted_data)

    return decrypted_filename


KEYSIZE = 16 #key yang digunakan
BLOCKSIZE = 16 #panjang blok 
filename = "Spongebob.jpeg" #file foto yang ingin di enkripsi dan deskripsi

key = getKey(KEYSIZE) #variable untuk pengambilan dari nilai KEYSZISE
iv = getIV(BLOCKSIZE) #variable untuk pengambilan dari nilai BLOCKSIZE

encrypted_filename = encrypt_image(filename, key, iv)
decrypted_filename = decrypt_image(encrypted_filename, key, iv)