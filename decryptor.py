import pyAesCrypt
import os


# File decryption func
def decryption(file, password):
    # buffer size setting
    buffer_size = 512 * 1024
    # call decrypt method
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size,
    )

    # successfull execution message
    print('[Файл "' + str(os.path.splitext(file)[0]) + '" дешифрован]')
    
    # removing source file
    os.remove(file)
    

# directories scan function 
def walking_by_dirs_decryptor(dir, password):
    # get over all the subdirectories
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # if we've found file then decrypt it
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # else continue searching files
        else:
            walking_by_dirs_decryptor(path, password)
            

password = input("Enter password to decrypt file: ")
walking_by_dirs_decryptor(r"YOUR_PATH", password)