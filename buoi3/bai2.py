#Dự đoán kết quả của các biểu thức so sánh sau:
#'a' > 'b'
#3.0 > 3
#'' <= ' '
#.5 > 1

print("a" > "b") #False vì ta tra trong bảng mã ACSII ta thấy a = 97 và b = 98 nên a > b là sai
print(3.0 > 3) #False vì giá trị 3.0 vẫn bằng 3
print('' <= ' ') 
print(.5 > 1) #False vì .5 là 0.5 mà 0.5 < 1 => False