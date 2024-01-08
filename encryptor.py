import pyAesCrypt
import os


# File encryption func
def encryption(file, password):
    # buffer size setting
    buffer_size = 512 * 1024
    # call encrypt method
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + '.crp',
        password,
        buffer_size,
    )

    # successfull execution message
    print('[Файл "' + str(os.path.splitext(file)[0]) + '" зашифрован]')
    
    # removing source file
    os.remove(file)
    

# directories scan function 
def walking_by_dirs_encryptor(dir, password):
    # get over all the subdirectories
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # if we've found file then encrypt it
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # else continue searching files
        else:
            walking_by_dirs_encryptor(path, password)
            

password = input("Enter password to encrypt file: ")
walking_by_dirs_encryptor(r"YOUR_PATH", password)