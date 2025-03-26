from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message.encode('utf-8'))
    return sha3_hash.digest()

def main():
    text = input("Nhập dữ liệu để hash bằng SHA-3: ")
    hash_value = sha3(text)


    print("chuỗi văn bản đã nhập: ", text.encode('utf-8'))
    print("SHA-3 Hash: ", hash_value.hex())

if __name__ == "__main__":
    main()    