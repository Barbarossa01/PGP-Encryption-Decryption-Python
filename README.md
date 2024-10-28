<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>PGP Encryption and Decryption with Python-GnuPG</h1>
    <h2>Introduction</h2>
    <p>This project demonstrates the use of the <code>python-gnupg</code> module for encrypting and decrypting files using GnuPG. To get started, you need to set up the GnuPG interface by initializing it with the following command:</p>
    <pre><code>gpg = gnupg.GPG(gnupghome='/path/to/home/directory')</code></pre>
    <ol>
        <li>
            <strong>Key Generation</strong>: 
            <ul>
                <li>Generate a passphrase-protected private key and a public key.</li>
                <li>Define the <code>name_email</code> which represents the public key and will be used in the encryption phase.</li>
                  <br><img src="https://github.com/Barbarossa01/PGP-Encryption-Decryption-Python/blob/main/images/gen_admin_keyScript.PNG" alt="Script for generate keys">
                <li>Assign a passphrase that will be essential for decrypting the encrypted files.</li>
                <li>Specify the <code>key_type</code> and <code>key_length</code> as needed.</li>
                <li>Use <code>key = gpg.gen_key(input_data)</code> to generate the key locally in the <code>.gnupg</code> folder.</li>
                <li>To share the key with another person, you will need to export it.</li>
            </ul>
              <h2>Generated Public Key</h2>
    <p>The generated public key is stored in the file <code>admin_pub_key.asc</code>. This file contains the public key that can be shared with others to allow them to encrypt files that only the corresponding private key can decrypt.</p>
<br><img src="https://github.com/Barbarossa01/PGP-Encryption-Decryption-Python/blob/main/images/generatedPublicKey.PNG" alt="generating public key">
        <h4>Key Fingerprint</h4>
    <p>The key fingerprint is a unique identifier for the generated public key. It is a shorter representation of the public key, typically consisting of 40 hexadecimal characters. You can find the fingerprint of your public key by the following line in python:</p>
    <pre><code># Print the key ID (this is what `key` should represent)
print(key)  # This will print the key ID

key_info = gpg.list_keys(secret=True)  # Get a list of all secret keys
for k in key_info:
    if key.fingerprint == k['fingerprint']:
        print("Key Fingerprint:", k['fingerprint'])
</code></pre>
    <p>This fingerprint can be shared with others to verify the authenticity of your public key.</p>
<br><img src="https://github.com/Barbarossa01/PGP-Encryption-Decryption-Python/blob/main/images/KeyFingerprint.PNG" alt="fingerprint">

  </li>
        </li>
        <li>
            <strong>File Encryption</strong>: 
            <ul>
                <li>To encrypt files using the generated key, define the path of the unencrypted file.</li>
                <li>Open the file in Python and encrypt it using:</li>
                <pre><code>status = gpg.encrypt_file(...)</code></pre>
                <li>In the <code>recipients</code> parameter, use the <code>name_email</code> from the previous step.</li>
<br><img src="https://github.com/Barbarossa01/PGP-Encryption-Decryption-Python/blob/main/images/encryptFolderScript.PNG" alt="fingerprint">
                            <p>Here are the results after running a script encrypt.py to encrypt all the files in a target folder</p>
              <br><img src="https://github.com/Barbarossa01/PGP-Encryption-Decryption-Python/blob/main/images/encryptingFolder.PNG" alt="fingerprint">
                              <p>Note that all the files in a given folder encrypted with an output name name.txt.encrypted, how the encrypted file looks like where it's unreadable</p>
<br><img src="https://github.com/Barbarossa01/PGP-Encryption-Decryption-Python/blob/main/images/encryptedFiles.PNG" alt="fingerprint">
            </ul>
        </li>
        <li>
            <strong>File Decryption</strong>: 
            <ul>
                <li>Similar to the encryption step, read the encrypted file in Python but use the following method:</li>
                <pre><code>status = gpg.decrypt_file(...)</code></pre>
                <li>Note that this phase requires the passphrase associated with your private key. Without the private key, decryption is not possible.</li>
              <br><img src="https://github.com/Barbarossa01/PGP-Encryption-Decryption-Python/blob/main/images/DecryptionFileScript.PNG" alt="fingerprint">
              <p>Here are the results of decrypting file successfully </p>
<br><img src="https://github.com/Barbarossa01/PGP-Encryption-Decryption-Python/blob/main/images/decryptingEncryptedFile.PNG" alt="fingerprint">
              <p>And now we would be able to read it successfully, of course with the generated private key</p>
              <br><img src="https://github.com/Barbarossa01/PGP-Encryption-Decryption-Python/blob/main/images/generatedDecryptedFile.PNG" alt="fingerprint">
            </ul>
        </li>
        <li>
            <strong>Batch File Encryption</strong>: 
            <ul>
                <li>Encrypting multiple files can be achieved by looping through all the files in a folder and using the same encryption method:</li>
                <pre><code>status = gpg.encrypt_file(...)</code></pre>
            </ul>
        </li>
        <li>
            <strong>Importing Public Keys for Encryption</strong>: 
            <ul>
                <li>If you have a public key from another person and want to encrypt a file using that key, you need to import it first.</li>
                <li>This can be done by reading the key and importing it with:</li>
                <pre><code>gpg.import_keys(...)</code></pre>
                <li>Set the trust level of the imported keys to <code>ULTIMATE</code>, which is the highest level of trust.</li>
              import gnupg
   <pre><code>
gpg = gnupg.GPG(gnupghome='/home/alice/.gnupg')  # Fixed path
key_data = open('bob_pub_key.asc').read()
import_result = gpg.import_keys(key_data)

# Setting the trust level of the imported keys to ULTIMATE
gpg.trust_keys(import_result.fingerprints, 'TRUST_ULTIMATE')
mykeys = gpg.list_keys()
print(mykeys)
 </code></pre>
            </ul>
        </li>
    </ol>
    <h2>Requirements</h2>
    <ul>
        <li>Python</li>
        <li>python-gnupg module</li>
    </ul>
</body>
</html>
