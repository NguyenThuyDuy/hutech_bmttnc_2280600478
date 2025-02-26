so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập tiền lương trên mỗi giờ làm tiêu chuẩn: "))
gio_tieu_chuan = 44  # Số giờ làm chuẩn mỗi tuần

# Số giờ làm vượt chuẩn
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)

# Tính tổng thu nhập thực lĩnh
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5

# In kết quả
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")