<h1>PGP Encryption and Decryption</h1>

<h2>Overview</h2>
<p>This project demonstrates how to generate PGP keys, encrypt files, and decrypt them using the GnuPG library in Python. It includes scripts for key generation, file encryption, and decryption, showcasing secure data handling practices. The project is suitable for anyone interested in learning about encryption methods and implementing them in Python.</p>

<h2>Features</h2>
<ul>
  <li><strong>Key Generation</strong>:  
    <ul>
      <li>Generate a public/private key pair for secure communication.</li>
      <li>Export the public key for sharing with others.</li>
    </ul>
  </li>

  <li><strong>File Encryption</strong>:
    <ul>
      <li>Encrypt files in a specified directory using the generated public key.</li>
      <li>Support for batch encryption of multiple files.</li>
    </ul>
  </li>

  <li><strong>File Decryption</strong>:
    <ul>
      <li>Decrypt files using the corresponding private key and passphrase.</li>
      <li>Output the decrypted files for access.</li>
    </ul>
  </li>
</ul>

<h2>Test GIFs</h2>
<p>Below are demonstrations of the main functions of the application:</p>

<ul>
<h2>Key Generation Script</h2>
<p>This section showcases the script used to generate the public/private keys:</p>
![gen_admin_keyScript](https://github.com/user-attachments/assets/2af1b7a8-6092-4a6b-98de-6b95da75f365)


  <li><strong>File Encryption</strong>:
![Description of the image](https://raw.githubusercontent.com/Barbarossa01/PGP-Encryption-Decryption-Python/main/images/gen_admin_keyScript.PNG)
  </li>

  <li><strong>File Decryption</strong>:
    <br><img src="link_to_your_file_decryption_gif" alt="File Decryption Test">
  </li>
</ul>

<h2>Technology Stack</h2>
<ul>
  <li><strong>Programming Language</strong>: Python</li>
  <li><strong>Library</strong>: GnuPG (python-gnupg)</li>
</ul>

<h2>Installation</h2>
<ol>
  <li>Clone the repository: <code>git clone https://github.com/yourusername/pgp-encryption-decryption</code></li>
  <li>Navigate to the project directory: <code>cd pgp-encryption-decryption</code></li>
  <li>Install required dependencies: <code>pip install python-gnupg</code></li>
  <li>Run the key generation script: <code>python gen_keys.py</code></li>
  <li>Follow the prompts to create and export your public key.</li>
  <li>Use the encryption script to encrypt files: <code>python encrypt.py</code></li>
  <li>Decrypt files using the decryption script: <code>python decrypt.py</code></li></li>
</ol>
