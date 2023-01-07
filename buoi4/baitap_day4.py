movies_list = ["Thám tử lừng danh co nan", "Doraemon", "Siêu nhân Gao", "Dragon Ball", "Gió"] # khởi tạo danh sách những phim đã xem

#1.Tạo một movies list chứa tên các bộ phim đã xem
print("Phim đã xem: ", movies_list) #in ra những phim có trong danh sách khởi tạo

#2. Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list
movies_list_new = str(input("Mời bạn nhập tên phim: "))

#3. Thêm bộ phim vừa nhập vào cuối của danh sách movies
movies_list.append(movies_list_new)
print("Phim đã xem: ", movies_list)

#4. In ra bộ phim đầu tiên, cuối cùng và ở giữa movies list
print(f"Bộ phim đầu tiên trong danh sách phim là: {movies_list[0]}")
print(f"Bộ phim cuối cùng trong danh sách phim là: {movies_list[-1]}")
amount = len(movies_list)
print(f"Bộ phim ở giữa trong danh sách phim là: {movies_list[amount // 2]}")

#5. Tính tổng bộ phim có trong movies
amount = len(movies_list)
print("Tổng bộ phim đang có trong danh sách là: ", amount)

#6. Xóa bộ phim đầu và cuối trong movies
first_value_in_movies_list = movies_list.remove()
last_value_in_movies_list = movies_list.pop()
print("Tên bộ phim cuối cùng trong danh sách là: ", last_value_in_movies_list)
print("Danh sách sau khi xóa bộ phim cuối cùng là: ", movies_list)

#7. Lấy ra và xóa bộ phim cuối cùng trong movies
print("Tên bộ phim cuối cùng trong danh sách là: ", last_value_in_movies_list)
print("Danh sách sau khi xóa bộ phim cuối cùng là: ", movies_list)

#8. Chèn một bộ phim bất kỳ vào đầu danh sách movies
movies_list.insert(0, "Bạch Tuyết và Bảy chú lùn")
print("Danh sách bộ phim đang có là: ", movies_list)

#9. Đếm số bộ phim có tiêu đề là "One Piece"
amount = movies_list.count("One Piece")
print("Bộ phim có tiêu đề One Piece đang có: ", amount)

#10. Tìm vị trí của bộ phim có tên là "gió"
index_of_gio = movies_list.index("Gió")
print("Vị trí của Gió là: ", index_of_gio)

#11. Thêm một danh sách bộ phim khác vào cuối danh sách movies ban đầu
movies_list.append("Lập trình Python")
print("Danh sách phim hiện có là: ", movies_list)

#12. Xóa tất cả các bộ phim có trong danh sách
movies_list.clear()
print("Danh sách phim hiện có: ", movies_list)