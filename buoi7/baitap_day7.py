#1. Cho hai tập hợp (set)
art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

#Tìm những người bạn học cả vẽ lẫn toán
art_and_math_students =  art_students.intersection(math_students)
print("Những bạn học chung Toán và Vẽ: ",art_and_math_students)

#Tìm những người bạn học vẽ nhưng không học toán
art_not_math_students = art_students.difference(math_students)
print("Những bạn học Vẽ nhưng không học chung Toán: ",art_not_math_students)

#Tìm những người bạn học toán nhưng không học vẽ
math_not_art_students = math_students.difference(art_students)
print("Những bạn học Toán nhưng không học Vẽ: ",math_not_art_students)

#Tìm những người bạn học vẽ hay toán không phải cả hai
art_or_math_students = art_students.symmetric_difference(math_students)
print("Những bạn chỉ học Vẽ hoặc chỉ học Toán: ",art_or_math_students)

#Tìm tất cả những người bạn
all_students = art_students.union(math_students)
print("Tất cả học sinh của 2 môn Vẽ và Toán: ",all_students)

print("-"*50)

#2. Cho dict sau:
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}

#Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
#Cách 1:
print(f"Tên của album là {album_info['album_name']} và phát hành vào năm {album_info['release_year']}")

#Cách 2:
print(f"Tên của album là {album_info.get('album_name')} và phát hành vào năm {album_info.get('release_year')}")

#Thay đổi giá trị của key: release_year từ 1973 thành 1971
import json

album_info["release_year"] = 1971
print(json.dumps(album_info, indent=4))

#Xóa phần tử với key là track_list
del album_info["track_list"]
print(json.dumps(album_info, indent=4))

#Thêm một key mới là amount = 2000 bằng hai cách
#Cách 1:
album_info["amount"] = 2000
print(json.dumps(album_info, indent=4))

#Cách 2:
album_info.update(amount = 2000)
print(json.dumps(album_info, indent=4))

#Làm trống dict: album_info
album_info.clear()
print(album_info)