# PGP Encryption and Decryption with Python

This repository contains Python scripts for generating PGP keys, encrypting files, and decrypting them using the `python-gnupg` library.

## Features

- Generate a passphrase-protected private key and a public key.
- Encrypt multiple files in a specified directory.
- Decrypt files using the private key.

## Requirements

- Python 3.x
- `python-gnupg` library

You can install the required library using pip:

```bash
``` ``` 
pip install python-gnupg
```

Usage
1. Generating Keys
    <br><img src="https://github.com/Barbarossa01/PGP-Encryption-Decryption-Python/blob/main/images/gen_admin_keyScript.PNG
" alt="Generating Keys">

In the script above :
- Setting Up GnuPG :
<code> gpg = gnupg.GPG(gnupghome='/home/alice/.gnupg')
gpg.encoding = 'utf-8'
</code>
