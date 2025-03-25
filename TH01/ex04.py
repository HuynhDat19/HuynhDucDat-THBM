#Tạo 1 danh sách rỗng để lưu kết quả
j=[]
#Duyệt tất cả số từ 2000 đến 3200, kiểm tra i có chia hết cho 7 và không là bội số của 5 không
for i in range(2000, 3200+1):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print(','.join(j))