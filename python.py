#Trả về các số bé hơn 10000 và lớn hơn 100
# def check_valid_input(n):
#     return 100 <= n <= 10000
# while True:
#     n = int(input("Nhập vào số nguyên n (100 <= n <= 10000): "))
#     if not check_valid_input(n):
#         print("Số n không nằm trong khoảng [100, 10000]. Vui lòng nhập lại.")
#         continue
#     break
# #Tổng tất cả các ước số lẻ của số nguyên n
# def sum_odd_factors(n):
#     sum_factors = 0
#     for i in range(1, n + 1):
#         if n % i == 0 and i % 2 != 0:
#             sum_factors += i
#     return sum_factors
# # kiểm tra x có xuất hiện trong các ước số lẻ của số nguyên hay không?
# def check_x_in_odd_factors(n, x):
#     for i in range(1, n + 1):
#         if n % i == 0 and i % 2 != 0 and i == x:
#             return True
#     return False
# x = int(input("Nhập giá trị x: "))
# if check_x_in_odd_factors(n, x):
#     print(f"{x} xuất hiện trong các ước số lẻ của số nguyên {n}.")
# else:
#     print(f"{x} không xuất hiện trong các ước số lẻ của số nguyên {n}.")

# #Tính tổng số lượng chữ số của số nguyên n.
# def sum_digits(n):
#     # return sum(int(digit) for digit in str(n))
#     str = input("Nhập vào 1 chuỗi kí tự (có kèm số): ")
#     sum = 0
#     for x in range(len(str)):
#         if str[x].isdigit():
#             sum += int(str[x])
#     return sum
# print("Tổng các số có trong chuỗi là: ", sum_digits(sum))





#==============================



#Câu 2:Viết chương trình nhập một chuỗi từ bàn phím và thực hiện các công việc sau:
# a.	Đếm trong chuỗi vừa nhập có bao nhiêu ký tự chữ cái
# n = input("Nhập một chuỗi: ")
# so_luong_chu = 0
# so_luong_so = 0
# for i in range(len(n)):
#     if n[i].isupper() or n[i].islower() or n[i].isspace():#Kiểm tra hết các ký tự liên quan gồm chữ hoa, chữ thường, khoảng trắng
#         so_luong_chu+= 1
#     else:
#         so_luong_so += 1
# print("Số lượng chữ cái là: ", so_luong_chu)    
# # b.	Đếm trong chuỗi vừa nhập có bao nhiêu ký tự chữ số
# print("Số lượng chữ số là: ", so_luong_so)
# # c.	Chuyển đổi các ký tự trong chuỗi trên thành ký tự chữ hoa
# print("Chuỗi sau khi chuyển tất cả chữ sang chữ hoa là: ",n.upper())

# Câu 3 (2.0 điểm): Viết chương trình nhập từ bàn phím mảng gồm n số nguyên [1;10000] và thực hiện các hàm con sau:
# n = int(input("Nhập số lượng phần tử của mảng: "))
# arr = []
# for i in range(n):
#     num = int(input(f"Nhập phần tử thứ {i+1}: "))
#     arr.append(num)
# #Kiểm tra số hoàng thiện
# def KThoangThien(num):
#     sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum += i
#     return sum == num

# # a.	Viết hàm con đếm số hoàn thiện
# # Hàm đếm số hoàn thiện trong mảng
# def count_perfect_numbers(arr):
#     count = 0
#     for num in arr:
#         if KThoangThien(num):
#             count += 1
#     return print("Có",count,"số hoàng thiện")
    


# #Tổng các số hoàng thiện# 
# # b.	Viết hàm con tính tổng các phần tử là số hoàn thiện
# def sum_numbers(arr):
#     total = 0
#     for num in arr:
#         if KThoangThien(num):
#             total += num
#     return print("Tổng các số hoàng thiện là: ", total)


# # c.	Viết hàm con xuất ra các số hoàn thiện
# #Liệt Kê số hoàng thiện
# def print_perfect_numbers(arr):
#     perfect_nums = []
#     # Duyệt qua từng phần tử trong mảng
#     for num in arr:
#         # Nếu phần tử là số hoàn thiện, thêm vào danh sách perfect_nums
#         if KThoangThien(num):
#             perfect_nums.append(num)
#     # In ra các số hoàn thiện trong mảng
#     print("Các số hoàn thiện trong mảng là:", perfect_nums)
# # d.	In kết quả ra màn hình của 3 hàm trên

# count_perfect_numbers(arr)
# sum_numbers(arr)
# print_perfect_numbers(arr)

#Câu Câu 4 (2.0 điểm): Viết chương trình nhập thông tin của Sách gồm:
# a.	Tạo ra bộ từ điển với các thông số của sách: Mã sách, tên sách, tác giả, năm xuất bản.
# Tạo một từ điển để lưu thông tin của các sách
# books = {
#     "001": {"ten_sach": "Harry Potter", "tac_gia": "J.K. Rowling", "nam_xuat_ban": 1997},
#     "002": {"ten_sach": "The Great Gatsby", "tac_gia": "F. Scott Fitzgerald", "nam_xuat_ban": 1925},
#     "003": {"ten_sach": "To Kill a Mockingbird", "tac_gia": "Harper Lee", "nam_xuat_ban": 1960}
# }
# b.	Nhập mã sách bất kỳ, kiểm tra mã sách này có tồn tại hay không? Nếu có thì in ra thông tin tương ứng, ngược lại thông báo “Không tìm thấy.”.
# Hàm kiểm tra mã sách và hiển thị thông tin tương ứng
# def kiem_tra_ma_sach(ma_sach):
#     if ma_sach in books:
#         print("Thông tin sách:")
#         print(f"Mã sách: {ma_sach}")
#         print(f"Tên sách: {books[ma_sach]['ten_sach']}")
#         print(f"Tác giả: {books[ma_sach]['tac_gia']}")
#         print(f"Năm xuất bản: {books[ma_sach]['nam_xuat_ban']}")
#     else:
#         print("Không tìm thấy sách.")
# # Nhập mã sách từ người dùng
# print("================================================================")
# ma_sach_can_tim = input("Nhập mã sách cần tìm (Gợi ý một số mã có sẵn để kiểm tra 001,002,003): ")
# # Kiểm tra mã sách và hiển thị thông tin tương ứng
# print("================================================================")
# kiem_tra_ma_sach(ma_sach_can_tim)
# print("================================================================")



# #CâuCâu 5 (2.0 điểm): Xây dựng lớp Kim loại gồm 
# a.	Kimloai có các thuộc tính và phương thức
# -	Thuộc tính: ten, gia, congdung. 
# -	Phương thức: 
# 	Khởi tạo__init__: khởi tạo cho giá trị  ten, gia, congdung
# 	thongtinkimloai(): dùng để hiển thị thông tin cần thiết của tên, giá và công dụng
# class KmLoai:
#     def __init__(self,ten,gia,cong_dung):
#         self.ten = ten
#         self.gia = gia
#         self.cong_dung =cong_dung
#     def thongtinkimloai(self):
#         print("Tên Kim Loai: ",self.ten)
#         print("Giá:",self.gia)
#         print("cong_dung:",self.cong_dung)

# # b.	Tạo 2 đối tượng (Vàng, 4.000.000, Trang sức) và (Sắt, 100.000, Xây dựng) để thực thi phương thức thongtinkimloai(). In kết quả ra màn hình.
# print("================================================================")
# k = KmLoai("Vàng", "4.000.000" , "Trang sức")
# k.thongtinkimloai()      
# print("================================================================")  
# k2 = KmLoai("Sắt", "100.000" , "Xây dựng")
# k2.thongtinkimloai() 
# print("================================================================")  
