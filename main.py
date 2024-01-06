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
    
