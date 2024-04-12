# class SinhVien:
#     '''Lop chung mo ta'''
#     ten = 'Nam'
#     def inSinhVien(self):
#         print(self.ten)
# print(SinhVien.__doc__)


# class DEV:
#     def __init__(self) -> None:
#         pass

# #VD1:
# class point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# p = point(10,20)
# print("p.x = ", p.x)
# print("p.y = ", p.y)

#VD2: không có tham số
# class point:
#     def __init__(self):
#         self.x = 5
#         self.y = 3
# #tạo đối tượng p kểu point
# p = point()
# print("p.x = ", p.x)
# print("p.y = ", p.y)


#VD3: Tham số bắt buộc
# class point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# p = point(10,20)
# print("p.x = ", p.x)
# print("p.y = ", p.y)


#VD4: Tham số mặc định
# class point:
#     def __init__(self,x = 0,y = 0):
#         self.x = x
#         self.y = y
# p = point(10,20)
# print("p.x = ", p.x)
# print("p.y = ", p.y)
# p1 = point()
# print("p.x = ", p1.x)
# print("p.y = ", p1.y)
# p2 = point(10)
# print("p.x = ", p2.x)
# print("p.y = ", p2.y)

# #kế thừa
# class parentClass:
#     #lớp cha:
# class childClass(parentClass):
#     #lớp con


#ví dụ

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def infor(self):
#         print("Name: ",self.name)
#         print("Age: ",self.age)
# class studen(Person):
#     def __init__(self, name, age,year):
#         Person.__init__(self,name, age)
#         self.graduation = year
#         def infor(self):
#             Person.infor(self)
#             print("Graduation year: ", self.graduation)
# p = studen("Nguyen Van A", 19, 2022)
# p.infor()

#Ví dụ tính đa hình
# class chim:
#     def flight(self):
#         print("Đa số chim có thể bay")
# #Tạo lớp kế thừa
# class chimSe(chim):
#     def flight(self):
#         print("Chim Sẻ có thể bay")
# class DaDieu(chim):
#     def flight(self):
#         print("Đà Điểu không thể bay")
# obj1 = chim()
# obj2 = chimSe()
# obj3 = DaDieu()
# obj1.flight()
# obj2.flight()
# obj3.flight()

#=============================================Bài Tập========================================
#Câu 1:
# class HocSinh:
#     def __init__(self,hoten = '',gioiTinh='',age=0,DiaChi=''):
#         self.hoten = hoten
#         self.gioiTinh = gioiTinh
#         self.age = age
#         self.DiaChi = DiaChi
#         print()
#     def NhapThongTin(self):
#         self.hoten = input("Nhập Tên Học Sinh: ")
#         self.gioiTinh = input("Nhập Giới Tính: ")
#         self.age = int(input("Nhập tuổi: "))
#         self.DiaChi = input("Nhập địa chỉ: ")
#         print()
#     def InThongTin(self):
#         print("Họ Tên Học Sinh: ",self.hoten)
#         print("Giới Tính Học Sinh: ",self.gioiTinh)
#         print("Tuổi Học Sinh: ",self.age)
#         print("Địa Chỉ Học Sinh: ",self.DiaChi)
#Câu 2:
# class SinhVien:
#     def __init__(self, ma_sv = '', diem_tb = 0, tuoi = 0, lop = ''):
#         self.ma_sv = ma_sv
#         self.diem_tb = diem_tb
#         self.tuoi = tuoi
#         self.lop = lop

#     def NhapThongTin(self):
#         self.ma_sv = input("Nhập mã sinh viên: ")
#         while len(self.ma_sv) > 10:
#             print("Tên Chỉ được nhập tối đa 10 ký tự!!! ")
#             self.ma_sv = input("Nhập lại mã sinh viên: ")
#         #Nhập điểm trung bình :        
#         while True:
#             self.diem_tb = float(input("Nhập điểm trung bình: "))
#             if self.diem_tb <= 10 and self.diem_tb >= 0:
#                 break
#             else:
#                 print("Nhập Sai điểm!!!")
#         #Nhập tuổi     
#         while True:
#             self.tuoi = int(input("Nhập tuổi: "))
#             if self.tuoi >= 18:
#                 break
#             else:
#                 print("Em chưa 18 :[[ ")
#                 self.tuoi = input("Nhập tuổi lại ok: ")

#         #Kiểm Tra xem  vị trí đàu tiên của ký tự nhập từ bàn phím có phải là A or C hay không       
#         while True:
#             self.lop = input("Nhập lớp (bắt đầu bởi 'A' hoặc 'C'): ")
#             if self.lop[0] == 'A' or self.lop[0] == 'C':
#                 break
#             else:
#                 print("Lớp phải bắt đầu bởi ký tự 'A' hoặc 'C'. Vui lòng nhập lại!!")

#     def InThongTin(self):
#         print("Thông tin sinh viên:")
#         print("Mã sinh viên:", self.ma_sv)
#         print("Điểm trung bình:", self.diem_tb)
#         print("Tuổi:", self.tuoi)
#         print("Lớp:", self.lop)

#     def CoHocBong(self):
#         if self.diem_tb > 8.0:
#             return True
#         else:
#             return False

# # Sử dụng lớp SinhVien
# sv = SinhVien()
# sv.NhapThongTin()
# sv.InThongTin()
# if sv.CoHocBong():
#     print("Sinh viên được học bổng.")
# else:
#     print("Sinh viên không được học bổng.")

#Câu 3:
# class SoHoc:
#     def __init__(self,number1, number2):
#         self.number1 = number1
#         self.number2 = number2
#     def Inthongtin(self):
#         print("Số thứ 1: ",self.number1)
#         print("Số thứ 2: ",self.number2)
#     def Cong(self):
#         tong = 0
#         tong = self.number1 + self.number2
#         return print("Tổng = " ,tong)
#     def Tru(self):
#         Hieu = 0
#         Hieu = self.number1 - self.number2
#         return print("Hiệu = " ,Hieu) 
#     def Nhan(self):
#         thuong = 1
#         thuong = self.number1 * self.number2
#         return print("Thuơng = " ,thuong)
#     def Chia(self):
#         tich = 1
#         tich = float(self.number1 // self.number2)
#         return print("Tích = " ,tich)

# sohoc = SoHoc(6,3)
# sohoc.Inthongtin()
# sohoc.Cong()
# sohoc.Nhan()
# sohoc.Tru()
# sohoc.Chia()

# Câu 4: 4.	Viết chương trình định nghĩa một lớp có 4 phương thức: 
# a.	getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
# b.	printStringUpper: in chuỗi vừa nhập sang chữ hoa. 
# c.	printStringLower: in chuỗi vừa nhập sang chữ thường. 
# d.	printStringTitle: in chuỗi vừa nhập sang đầu mỗi từ viết hoa, các ký tự còn lại viết thường.

# class String:
#     def __init__(self):
#         self.chuoi = ""

#     def getString(self):
#         self.chuoi = input("Nhập chuỗi: ")

#     def printStringUpper(self):
#         print("Chuỗi in hoa:", self.chuoi.upper())

#     def printStringLower(self):
#         print("Chuỗi in thường:", self.chuoi.lower())

#     def printStringTitle(self):
#         print("Chuỗi in tiêu đề:", self.chuoi.title())


# # Sử dụng lớp để thực thi chương trình
# chuoi = String()
# chuoi.getString()
# chuoi.printStringUpper()
# chuoi.printStringLower()
# chuoi.printStringTitle()

#Câu 5:5.	Viết chương trình xây dựng một lớp có tên Hinhchunhat lưu thông tin về một hình chữ nhật. Có thuộc tính lưu chiều dài và chiều rộng, có phương thức tính chu vi và diện tích hình chữ nhật.
class Hinhchunhat:
    def __init__(self):
        self.chieu_dai = 0
        self.chieu_rong = 0
    #Nhập
    def get(self):
        self.chieu_dai = float(input("nhập chiều dài hình chữu nhật: "))
        self.chieu_rong = float(input("nhập chiều rộng hình chữu nhật: "))
    #Tìm chu vi hình chữ nhật
    def ChuVi(self):
        s = 0
        s = (self.chieu_dai+ self.chieu_rong)*2
        return print("Chuy vi của hình chữ nhât là: ", s)
    #Tìm diện tích hình chữ nhật
    def DienTich(self):
        s = 0
        s =self.chieu_dai* self.chieu_rong
        return print("Diệnn tích hình chữ nhật là: ", s)
HCN = Hinhchunhat()
HCN.get()
HCN.ChuVi()
HCN.DienTich()

#Câu 6: 6.	Viết chương trình xây dựng một lớp có tên Hinhvuong là lớp con của lớp Hinhchunhat (bài 5). Tính chu vi và diện tích hình vuông

# class HinhVuong:
#     def __init__(self):
#         self.canh = 0
#     def get_canh(self):
#         self.canh = float(input("Nhập cạnh của hình vuông: "))
#     def ChuviHV(self):
#         s = 0
#         s = self.canh *4
#         return print("Chu vi của hình vuông là: ", s)
#     def DienTichHV(self):
#         s = 0
#         s = self.canh * self.canh
#         return print("Diện tích của hình vuông là: ", s)

# hv = HinhVuong()
# hv.get_canh()
# hv.ChuviHV()
# hv.DienTichHV()


# Câu 7.	Viết chương trình xây dựng một lớp person có các thuộc tính là name, age, và phương thức hiển thị thông tin của các thuộc tính. Xây dựng lớp student là lớp con của lớp person và có thêm thuộc tính scholarship (học bổng)
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def print_person(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
# class student(person):
#     def __init__(self, name, age,scholarship):
#             person.__init__(self,name, age)
#             self.hocbong = scholarship
#     def print_student(self):
#         person.print_person(self)
#         print("Scholarships: ", self.hocbong)
# p = student("Hiền Tóc Xù",18,"Có học Bổng")
# p.print_student()
            
            