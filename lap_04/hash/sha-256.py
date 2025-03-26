import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8')) #chuyển đổi dữ liệu thành dạng byte và cập nhât vào đối tượng hash
    return sha256_hash.hexdigest() #trả về giá trị hash dưới dạng chuỗi hexa

data_to_hash = input("Nhập dữ liệu để hash bằng SHA-256: ")
hash_value = calculate_sha256_hash(data_to_hash)
print("Giá trị hash của dữ liệu là: ", hash_value)
