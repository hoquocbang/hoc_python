#Dự đoán kết quả của các biểu thức logic sau:
#0 and 1
#'' or None
#3 and 4 or 0
#'a' or '1'
#not None
#not 0

print(bool())
print(0 and 1) # 0 vì bool(0) = False mà trong and nếu giá trị đầu tiên là False thì sẽ trả về giá trị đầu là 0
print('' or None) #None vì bool('') = False mà trong or nếu giá trị đầu tiên là False thì sẽ trả về giá trị thứ 2 là None
print(3 and 4 or 0) # 4 vì bool(3) = True mà trong and nếu giá trị đầu tiên là True thì sẽ trả về giá trị 2 là 4
                    # mà bool(4) = True mà trong or nếu giá trị đầu tiên là True thì sẽ trả về giá trị thứ 1 là 4
print('a' or '1') # a vì bool('a') = True mà trong or nếu giá trị đầu tiên là True thì sẽ trả về giá trị thứ 1 là a
print(not None) #True vì bool(None) = False mà not False  = True
print(not 0) #True