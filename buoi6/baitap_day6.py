#1. Cho một list chứa các tuple như sau: friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]

#a. Cho biết chiều dài của friends
amount = len(friends)
print("Chiều dài của friends là: ", amount)
# hoặc có thể làm như sau : print(f"Chiều dài của {friends} là {len(friends)}")

#b. Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng
element_first = friends[0]
element_last = friends[-1]
element_mid = friends[1]
print(f"""Phần tử đầu của {friends} là : {element_first} 
và kiểu của phần tử đầu là {type(element_first)}
Phần tử cuối của {friends} là : {element_last}
và kiểu của phần tử cuối là {type(element_last)}
Phần tử giữa của {friends} là : {element_mid}
và kiểu của phần tử giữa là {type(element_mid)}
""")

#c. Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó append vào friends tuple
#   gồm hai giá trị (name, gender)
friend_name = input("Nhập vào tên người bạn: ")
gender = input("Nhập vào giới tính người bạn: ")
friend_tuple = (friend_name, gender)
friends.append(friend_tuple)
print("Danh sách hiện có là:", friends)

print("-----------------------------------------------------------------")

#2. Tạo một set trống có tên là set_a
set_a = set()

#a. Thêm 'Anna' vào set_a
set_a.add("Anna")

#b. Thêm một tuple ('Kenny', 'Jen', 'Danny')
set_a.update(("Kenny", "Jen", "Danny"))

#c. In ra set_a và tính chiều dài của nó
print(set_a)
print(f"Chiều dài của {set_a} là {len(set_a)}")

#d. Xóa 'Jen' ra khỏi set_a
set_a.remove("Jen")

#e. Xóa tất cả các giá trị từ set_a
set_a.clear()
print(set_a)