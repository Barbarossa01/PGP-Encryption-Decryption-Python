import gnupg
import os
gpg = gnupg.GPG(gnupghome='/home/admin/.gnupg')
path = '/home/admin/secrect_files/original'  # Folder containing files to encrypt

for f in os.listdir(path):
    if os.path.isfile(os.path.join(path, f)):
        with open(os.path.join(path, f), 'rb') as efile:
            status = gpg.encrypt_file(efile, recipients=['admin@admin.org'], output=path + "/" + f + ".encrypted")
            print(f"Encryption status for {f}: {status.ok}")
            print(status.stderr)
