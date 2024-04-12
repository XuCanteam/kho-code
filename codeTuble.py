#câu 1: 1.	Viết chương trình nhập thông tin của sinh viên gồm: Mã số sinh viên, họ và tên, năm sinh, điểm; lưu các thông tin này trong một từ điển. Nhập mã số sinh viên, nếu tồn tại sinh viên có mã số sinh viên cần tìm thì in ra thông tin tương ứng của sinh viên, ngược lại thông báo không có sinh viên cần tìm.
# n = int(input("Nhập số lượng muốn thêm sinh viên: "))
# sinh_vien = {}
# for i in range(n):
#     Ma_so_SV = input("Nhập mã số sinh viên: ")
#     ho_ten = input("Nhập họ tên sinh viên: ")
#     nam_sinh = input("Nhập năm sinh sinh viên: ")
#     tuoi = input("Nhập tuổi sinh viên: ")
#     diem = input("Nhập điểm: ")
#     sinh_vien[Ma_so_SV] = {"Họ Tên sv": ho_ten,"Năm Sinh":nam_sinh,"Tuổi":tuoi,"Điểm ":diem}


# ma_so_tim = input("Nhập mã số sv cần tìm: ")
# if ma_so_tim in sinh_vien:#Tìm mã sinh viên vừa nhập có nằm trong dict sinh_vien hay không, nếu có thì thực hiện in hết tất cả dữ liệu có trong dict sinh_vien ra, nếu không thì trả về không có sinh viên trong dict sinh_vien
#     print("Thông tin sinh viên có mã số là: ",ma_so_tim)
#     print("Mã số tìm: ",ma_so_tim)
#     for key,value in sinh_vien[ma_so_tim].items():#trả về các phần tử trong Dictionary
#         print(key+":",value)
# else:
#     print("Không có sinh viên có mã số ",ma_so_tim)



#Câu 2: 2.	Viết chương trình nhập thông tin của Tivi gồm: Số hiệu tivi, kích thước, độ phân giải, hãng sản xuất, năm sản xuất; lưu các thông tin này trong một từ điển. Nhập số hiệu tivi, nếu tồn tại Tivi có số hiệu cần tìm thì in ra thông tin  tương ứng của Tivi, ngược lại thông báo không có Tivi cần tìm.
# n = int(input("Nhập số lượng muốn thêm Tivi: "))
# Tivi = {}
# for i in range(n):
#     so_hieu_tivi = input("Nhập số hiệu tivi: ")
#     kich_thuoc = input("Nhập kích thước: ")
#     do_phan_giai = input("Nhập độ phân giải: ")
#     hang_san_xuat = input("Nhập hảng sản xuất: ")
#     nam_san_xuat = input("Nhập năn sản xuất: ")
#     Tivi[so_hieu_tivi] = {"Kích thước":kich_thuoc ,"Độ phân giải":do_phan_giai,"Hãng sản Xuất":hang_san_xuat,"Năm sản xuất":nam_san_xuat}


# ma_so_tim = input("Nhập số hiệu cần tìm: ")
# if ma_so_tim in Tivi:
#     print("Thông tin Tivi có mã số hiệu là: ",ma_so_tim)
#     print("Mã số tìm: ",ma_so_tim)
#     for key,value in Tivi[ma_so_tim].items():#trả về các phần tử trong Dictionary
#         print(key+":",value)
# else:
#     print("Không có không có tivi có mã ",ma_so_tim)

#câu 3: 3.	Viết chương trình nhập thông tin của máy quạt gồm: Số hiệu quạt, loại quạt (bàn, trần, treo tường,...), công suất (kW), đơn giá; lưu các thông tin này trong một từ điển. Nhập số hiệu quạt, nếu tồn tại quạt có số hiệu cần tìm thì xóa quạt này khỏi từ điển. Sau đó thêm một phần tử (máy quạt mới) vào từ điển đã có.
# n = int(input("Nhập số lượng muốn thêm Quạt: "))
# Quat = {}
# for i in range(n):
#     so_hieu_quat = input("Nhập số hiệu Quạt: ")
#     loai_quat = input("Nhập loại Quạt: ")
#     cong_suat = float(input("Nhập công suất: "))
#     don_gia = float(input("Nhập đơn giá Quạt: "))
#     Quat[so_hieu_quat] = {"Loại Quạt":loai_quat ,"Công xuất":cong_suat,"Đơn giá":don_gia}


# ma_so_tim = input("Nhập số hiệu cần tìm: ")
# if ma_so_tim in Quat:
#     del Quat[ma_so_tim]
#     print("Đã xóa máy quạt có số hiệu", ma_so_tim)
# else:
#     print("Không có máy quạt có số hiệu ",ma_so_tim)

# so_hieu_quat_moi = input("Nhập số hiệu Quạt: ")
# loai_quat_moi = input("Nhập loại Quạt: ")
# cong_suat_moi = float(input("Nhập công suất: "))
# don_gia_moi = float(input("Nhập đơn giá Quạt: "))
# Quat[so_hieu_quat_moi] = {"Loại Quạt":loai_quat_moi ,"Công xuất":cong_suat_moi,"Đơn giá":don_gia_moi}

# print("Thông tin máy quạt mới khi được thêm vào")
# for so_hieu_quat,thong_tin in Quat.items():
#     print("Số hiệu quạt:", so_hieu_quat)
#     for key,value in thong_tin.items():#trả về các phần tử trong Dictionary
#         print(key+":",value)

#Câu 4.	Viết chương trình nhập vào một từ điển có các phần tử có key là số nguyên, value là số nguyên, tìm và trả về key có value lớn nhất.
# n = int(input("Nhập số lượng muốn thêm key: "))
# dict = {}
# for i in range(n):
#     key = int(input("Nhập key (key là số nguyên): "))
#     value = int(input("Nhập giá trị của key(là số nguyên):"))
#     dict[key]= value
# if dict:
#     max_key = max(dict,key=dict.get)
#     print("Key có value lớn nhất là: ",max_key)
# else:
#     print("Phần tử không có từ điển")
#Câu 5.	Viết chương trình nhập vào một từ điển có các phần tử có key là chuỗi, value là số nguyên. Tìm và trả về value của key có độ dài lớn nhất. 
# n = int(input("Nhập số lượng muốn thêm key: "))
# dict = {}
# for i in range(n):
#     key = str(input("Nhập key (key là chuỗi): "))
#     value = int(input("Nhập giá trị của key(là số nguyên):"))
#     dict[key]= value
# if dict:
#     max_length_key = max(dict,key=len)
#     print("Value có key lớn nhất là: ",max_length_key)
# else:
#     print("Phần tử không có từ điển")



