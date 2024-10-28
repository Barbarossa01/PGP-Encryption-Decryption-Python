import gnupg 
import os
gpg = gnupg.GPG(gnupghome='/home/admin/.gnupg')
path = '/home/admin/secrect_files/original/encrypted'
ptfile = '/seasons.txt.encrypted'

with open(path + ptfile, 'rb') as f:
    status = gpg.decrypt_file(f, passphrase='admin123', output=path + "/password.txt.decrypted")  # Fixed syntax

print(status.ok)
print(status.stderr)
