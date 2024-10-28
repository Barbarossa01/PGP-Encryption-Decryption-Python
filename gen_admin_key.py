import os
import gnupg

gpg = gnupg.GPG(gnupghome='/home/admin/.gnupg')
gpg.encoding = 'utf-8'

input_data = gpg.gen_key_input(
    name_email='admin@admin.org',
    passphrase='admin123',
    key_type='RSA',
    key_length=1024
)

# Generate the key
key = gpg.gen_key(input_data)

# Print the key ID (this is what `key` should represent)
print(key)  # This will print the key ID

# Use the key ID to fetch the fingerprint
key_info = gpg.list_keys(secret=True)  # Get a list of all secret keys
for k in key_info:
    if key.fingerprint == k['fingerprint']:
        print("Key Fingerprint:", k['fingerprint'])

# Export the public key
public_key = gpg.export_keys(str(key))

# Save the public key to a file
with open('admin_pub_key.asc', 'w') as f:
    f.write(public_key)
