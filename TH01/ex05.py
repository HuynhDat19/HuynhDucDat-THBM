# nhập số giờ làm việc hàng tuần của nhân viên và mức lương
soGioLam = float(input("Nhập số giờ làm hàng tuần: "))
luongTheoGio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
gioTieuChuan = 44 #Giờ tiêu chuẩn mỗi tuần
gioVuotChuan = max(0, soGioLam - gioTieuChuan) # số giờ làm vượt chuẩn mỗi tuần
#Tính lương
luong = gioTieuChuan*luongTheoGio + gioVuotChuan*luongTheoGio*1.5
#Xuất lương
print("Lương nhận được sau", soGioLam, "giờ/tuần là ", luong*1000, "vnđ")