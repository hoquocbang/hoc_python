#1. Cho danh sách (list) friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]

#Yêu cầu:
#a. Lấy ra 4 người bạn đầu tiên trong friends
friends_1 = friends[:4]
print("Bốn người đầu tiên trong danh sách là: ", friends_1)

#b. Lấy ra 4 người bạn cuối trong friends
friends_2 = friends[3:]
print("Bốn người cuối cùng trong danh sách là: ", friends_2)

#c. Đảo ngược danh sách friends
friends_3 = friends[::-1]
print("Đảo ngược danh sách friends là: ", friends_3)

#d. Lấy ra những người bạn từ vị trí 1 đến hết
friends_4 = friends[1:]
print("Những bạn từ vị trí 1 đến cuối trong danh sách friends là: ", friends_4)

#e. Copy danh sách ban đầu thành một danh sách mới
friends_copy = friends.copy()
print("Danh sách friends mới là: ", friends_copy)

#f. Lấy ra những người bạn từ vị trí 2 đến sát cuối
friends_5 = friends[2:-1]
print("Danh sách những người bạn từ vị trí 2 đến sát cuối là: ", friends_5)

#2.Cho danh sách các sinh viên chứa thông tin của mỗi sinh viên [id, tên, tuổi] như sau:
students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]

#Yêu cầu:
#a. Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
student1_id = students[0][0]
student1_name = students[0][1]
student1_age = students[0][2]
print(f"ID: {student1_id}, name: {student1_name} - age: {student1_age}")

#b. Lấy ra tuổi của sinh viên thứ hai
student2_age = students[1][2]
print("Tuổi của sinh viên thứ 2 là: ", student2_age)

#c. Lấy ra thông tin hai sinh viên cuối cùng
student3_id = students[2][0]
student3_name = students[2][1]
student3_age = students[2][2]
print(f"ID: {student3_id}, name: {student3_name} - age: {student3_age}")

#d. Lấy ra id của sinh viên thứ ba
print("ID của sinh viên thứ 3 có trong danh sách là: ",student3_id)