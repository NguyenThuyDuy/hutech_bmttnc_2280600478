import rsa, os

if not os.path.exists('cipher/rsa/keys'):
    os.makedirs('cipher/rsa/keys')

class RSACipher:
    def __init__(self):
        pass
    
    def generate_keys(self):
        # Generate 2048-bit RSA keypair
        (pubkey, privkey) = rsa.newkeys(2048)
        
        # Save keys to files
        with open('cipher/rsa/keys/privateKey.pem', 'wb') as p:
            p.write(privkey.save_pkcs1('PEM'))
        with open('cipher/rsa/keys/publicKey.pem', 'wb') as p:
            p.write(pubkey.save_pkcs1('PEM'))
    
    def load_keys(self):
        with open('cipher/rsa/keys/privateKey.pem', 'rb') as p:
            privkey = rsa.PrivateKey.load_pkcs1(p.read())
        with open('cipher/rsa/keys/publicKey.pem', 'rb') as p:
            pubkey = rsa.PublicKey.load_pkcs1(p.read())
        return privkey, pubkey
    
    def encrypt(self, message, key=None):
        if key is None:
            _, pubkey = self.load_keys()
            key = pubkey
        return rsa.encrypt(message.encode('utf-8'), key)
    
    def decrypt(self, ciphertext, key=None):
        if key is None:
            privkey, _ = self.load_keys()
            key = privkey
        return rsa.decrypt(ciphertext, key).decode('utf-8')
    
    def sign(self, message, key=None):
        if key is None:
            privkey, _ = self.load_keys()
            key = privkey
        return rsa.sign(message.encode('utf-8'), key, 'SHA-1')
    
    def verify(self, message, signature, key=None):
        if key is None:
            _, pubkey = self.load_keys()
            key = pubkey
        try:
            return rsa.verify(message.encode('utf-8'), signature, key) == 'SHA-1'
        except rsa.VerificationError:
            return False