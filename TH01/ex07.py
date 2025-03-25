print("Nhập các dòng văn bản (Nhập 'done' để kết thúc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
# Chuyển các dòng thành chữ in hoa và xuất ra màn hình 
print("Các dòng đã nhập sau khi chuyển sang chữ in hoa: ")
for line in lines:
    print(line.upper())