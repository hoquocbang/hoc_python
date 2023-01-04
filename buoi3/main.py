# Hàm print để in kết quả ra ngoài màn hình
# Muốn hiển thị emojis (biểu tượng cảm xúc) nhấn tổ hợp phím Win + . (dấu chấm)
print("❤️😊😂🤣😍😒👌😘💕😁👍🐍")

# In các giá trị 1 2 3 4 trên một dòng và ngăn cách nhau bởi dấu | (xổ)
print(1, 2, 3, 4, sep=" | ")

# Hàm input để nhận đầu vào từ bàn phím
# Kết thúc nhập bằng phím Enter 
# hàm input - luôn trả về một chuỗi ký tự (string - str)
# Tab Output không thể nhập nên sẽ làm như sau
user_name = input("Nhập tên người dùng: ")
print(user_name)

# Các kiểu dữ liệu trong Python: int (số nguyên), float (số thực), str (chuỗi ký tự), bool (True/False - Đúng Sai)
# Muốn xác định kiểu sử dụng hàm type(value)
print(type(1)) # giá trị 1 - kiểu số nguyên (int)
print(type(1.25)) # giá trị 1.25 thuộc kiểu float (số thực)
print(type(True)) # bool
print(type("Hello")) # str
print(1+2)