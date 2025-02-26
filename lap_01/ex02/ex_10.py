# Hàm đảo ngược chuỗi
def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

# Nhận chuỗi từ người dùng và in kết quả
input_string = input("Nhập chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(input_string))