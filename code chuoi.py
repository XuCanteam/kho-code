#Câu 1:
# str = " "
# str1 = input("Nhập chuỗi thứ 1: ")
# str2 = input("Nhập chuỗi thứ 2: ")
# sep = (str1,str2)
# print ("Chuỗi sau khi được nối là :", str.join(sep))


# #Câu 2:
# str = input("Nhập vào 1 chuỗi: ")
# s = str.lower()
# print("Chuỗi sau khi đổi là: ", s)


#Câu 3:
# str = input("Nhập vào 1 chuỗi: ")
# so_luong_hoa = 0
# so_luong_thuong = 0
# so_luong_so = 0

# # Duyệt qua từng ký tự trong chuỗi
# for ky_tu in range(0,len(str)):
#     if str[ky_tu].isupper():  # Kiểm tra ký tự hoa
#         so_luong_hoa += 1
#     elif str[ky_tu].islower():  # Kiểm tra ký tự thường
#         so_luong_thuong += 1
#     elif str[ky_tu].isdigit():  # Kiểm tra chữ số
#         so_luong_so += 1
# print("Số lượng ký tự hoa:", so_luong_hoa)
# print("Số lượng ký tự thường:", so_luong_thuong)
# print("Số lượng chữ số:", so_luong_so)


#Câu 4:
# str = input("Nhập vào 1 chuỗi: ")

# s = str[::-1]
# print("Chuỗi sau khi đảo ngược là:",s)


#Câu 5:
# str1 = input("Nhập chuỗi cần kiểm tra: ")
# str2 = input("Nhhập chuỗi kiểm tra: ")

# str1 = str1[::-1]
# if str1 == str2:
#     print("Chuỗi đối xứng")
# else:
#     print("Chuỗi không đối xứng")

#Câu 6:
# str = input("Nhập vào 1 chuỗi kí tự (có kèm số): ")
# sum = 0
# for x in range(len(str)):
#     if str[x].isdigit():
#         sum += int(str[x])
# print("Tổng các số có trong chuỗi là: ", sum)


#Câu 7:
# str = input("Nhập vào 1 chuỗi: ")
# s = str.upper()
# print("Chuỗi sau khi đổi là: ", s)


#Câu 8:
# s1 = input("Nhập chuỗi 1: ")
# s2 = input("Nhập vào chuỗi 2: ")
# str = " "
# if len(s1) > len(s2):
#     sep = (s1,s2)
#     print ("Chuỗi sau khi được nối là :", str.join(sep))
# else:
#     sep2 = (s2,s1)
#     print ("Chuỗi sau khi được nối là :", str.join(sep2))



#Câu 9:

# str = input("Nhập vào 1 chuỗi; ")
# s1 = str.title()
# print ("Chuỗi sau khi chuyển đổi là: ",s1)


#Câu 10;
# str = input("Nhập họ và tên, ngày sinh của bạn: ")
# so_luong_hoa = 0
# so_luong_thuong = 0
# so_luong_so = 0
# so_luong_khoang_trang = 0
# for ky_tu in range(0,len(str)): #Duyệt theo độ dài của chuỗi
# #a) Đếm số kí tự hoa có trong chuỗi
#     if str[ky_tu].isupper():  # Kiểm tra ký tự hoa
#         so_luong_hoa += 1
# # b) Đếm số kí tự thường có trong chuỗi
#     elif str[ky_tu].islower():  # Kiểm tra ký tự thường
#         so_luong_thuong += 1
# # c)Đếm số kí tự chữ số có trong chuỗi
#     elif str[ky_tu].isdigit():  # Kiểm tra chữ số
#         so_luong_so += 1
# # d)Đếm số kí tự khoảng trắng có trong chuỗi
#     elif str[ky_tu].isspace():
#         so_luong_khoang_trang += 1
# # e)Đổi tất cả các kí tự đầu tiên của mỗi từ thành kí tự in hoa
# s1 = str.title()
# # f)Tìm họ của sinh viên
# s2 = str
# ho = s2.split()
# hosv = ho[0]
# #====Xuất=================================================
# print ("Số kí tự hoa có trong chuỗi la: ",so_luong_hoa)
# print ("Số kí tự thường có trong chuỗi la: ",so_luong_thuong)
# print ("Số kí tự số có trong chuỗi là: ",so_luong_so)
# print ("Chuỗi sau khi chuyển đổi là: ",s1)
# print("Họ của tên vừa nhập là:", hosv)



# # Câu 11;
# str = input("Nhập vào 1 chuỗi (lưu ý không có chữ số): ")
# if str.stisdigit():
    


# cau 12:
# str = input("nhập chuỗi dãy số nguyên (mỗi số cách nhau dấu phẩy ,): ")
# danh_sach_so = [int(so) for so in str.split(',')]
# tong = sum(danh_sach_so)     
# print ("Tổng các số nguyên có trong chuỗi là: ", tong)


# Câu 13:
# import re

# # Nhập mật khẩu từ người dùng
# mat_khau = input("Nhập mật khẩu: ")

# # Kiểm tra chiều dài của mật khẩu
# if len(mat_khau) < 6:
#     print("Mật khẩu quá ngắn. Vui lòng nhập mật khẩu có ít nhất 6 ký tự.")
# else:
#     # Kiểm tra có ít nhất 1 ký tự đặc biệt, 1 ký tự in hoa, 1 chữ số, 1 chữ thường
#     if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", mat_khau) or \
#        not re.search(r"[A-Z]", mat_khau) or \
#        not re.search(r"[0-9]", mat_khau) or \
#        not re.search(r"[a-z]", mat_khau):
#         print("Mật khẩu không đủ mạnh. Vui lòng kiểm tra lại các yêu cầu.")
#     else:
#         print("Mật khẩu mạnh!")

#================CẤU TRÚC ĐIỀU KHIỂN=======================
# #Câu 14:

# n = int(input("Nhập n: "))

# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=' ')

# #Câu 15
# n = int(input("Nhập n: "))
# sum = 0
# for i in range(1,n+1):
#     if n%i==0:
#         sum +=i
# print(sum, end=" ")
# #Câu 16:
# n = int(input("Nhập n: "))
# dem =0
# for i in range(1,n+1):
#     if n%i==0:
#         dem+=1
# print(dem,end=' ')
# #Câu 17:
# n = int(input("Nhập n: "))
# dem =0
# for i in range(1,n+1):
#     if n % i == 0 and i % 2 != 0:
#         print("Ước Số Lẻ = ",i,end=' ')

# #Câu 18:
# n = int(input("Nhập n: "))
# s=0
# for i in range(1,n+1):
#     if n % i == 0 and i % 2 == 0:
#         s+=i
# print("Tổng các ước Số Chẵn là = ",s)
# #Câu 19:
# n = int(input("Nhập n: "))
# sum = 0
# for i in range(1,n):
#     if n%i==0:
#         sum +=i
# print("Tổng các ước số nhở hơn",n,"là: ",sum, end=" ")
# #Câu 20
# n = int(input("Nhập n: "))
# max = 0
# for i in range(n,0,-1):
#     if (n % i == 0 and i % 2 != 0):
#         max = i
#         break
# print("Ước số lẻ lớn nhất của",n,"là: ",max, end=" ")

#Câu 21
# from math import sqrt
# n = int(input("Nhập n: "))
# if n<=1:
#     ngto= False
# else:
#     ngto =True
#     for i in range(2,int(sqrt(n))+1):
#         if n % i == 0:
#             ngto = False
#             break
# if ngto:
#     print(n,"Là số nguyên tố") 
# else:
#     print("Không là số nguyên tố")
#Câu 22: 
# n = int(input("Nhập n: "))
# s=0
# for i in range(1,n):
#     if n%i==0:
#         s+=i

# if s == n:
#     print(n,"là số hoàn thiện")
# else:
#     print(n,"không là số hoàn thiện")

#Câu 23: cân n mà bằng n là số chính phương
# from math import sqrt

# n = int(input("Nhập n:"))

# if (int(sqrt(n))*int(sqrt(n)))==n:
#     print(n,"là số chính phương")
# else:
#     print(n,"không là số chính phương")

        
#Câu 24:
# n = int(input("Nhập n: "))
# while n!=0:
#     n=n//10
#     dem+=1
# print ("Số vừa nhập có ",dem," chữ số",end=" ")

# #Câu 25:
# n = int(input("Nhập n: "))
# tong =0
# while n!=0:
#     tam=n%10
#     tong += tam
#     n=n//10
# print ("Tổng các chữ số là: ",tong,end=" ")

#Câu 26:

# n = int(input("Nhập n: "))
# tong =0
# while n!=0:
#     tam=n%10
#     if tam% 2!=0:
#         tong += tam
#     n=n//10
# print ("Tổng các chữ số lẻ là: ",tong,end=" ")
#Câu 27:
# n = int(input("Nhập n: "))
# tong =0
# while n!=0:
#     tam=n%10
#     if tam% 2==0:
#        tong += tam
#     n=n//10
# print ("Tổng các chữ số chẵn là: ",tong,end=" ")
#Câu 28
# n = int(input("Nhập n: "))
# tong =0
# while n!=0:
#     tam=n%10
#     n=n//10
# print ("Chữ số đầu tiên của n là: ",tam,end=" ")
#Câu 29:
# n = int(input("Nhập n: "))
# min = n
# while n!=0:
#     tam=n%10
#     if tam < min:
#         min = tam
#     n=n//10
# print ("Chữ số nhỏ nhất của n là: ",min,end=" ")
#Câu 30: dùng 2 if
# n = int(input("Nhập n: "))
# min = n
# dem =0
# while n!=0:
#     tam=n%10
#     if tam <= min:
#         min = tam
#         dem +=1
#     n=n//10
# print ("Chữ số nhỏ nhất của n có",dem,"chữ số",end=" ")
#Câu 31: Dùng break
# n = int(input("Nhập n: "))
# min = n
# dem =0
# while n!=0:
#     tam=n%10
#     if tam%2!=0:
#         break
#     n=n//10
# if tam%2!=0:
#     print("n không có toàn chẵn")
# else:
#     print("n toàn chẵn")
#Câu 32:
# n= int(input("Nhập n:"))
# s = 0
# for i in range(1,n+1):
#     s = s + i
# print("Tổng S = ", s, end=" ")
# #Câu 33;
# n= int(input("Nhập n:"))
# s = 0
# for i in range(1,n+1):
#     if i%2!=0:
#         s+=i
# print("Tổng S = ", s, end=" ")
#Câu 34:
# n= int(input("Nhập n:"))
# s = 0
# p = 1
# for i in range(1,n+1):
#     p = p*i
#     s = s + p
# print("Tổng S = ", s, end=" ")
#Câu 35
# n= int(input("Nhập n:"))
# s = 0
# for i in range(1,n+1):
#     s = s + (i*i)
# print("Tổng S = ", s, end=" ")
#Câu 36:
# n= int(input("Nhập n:"))
# s=0

# for i in range(1,n+1):
#     s+=1/(i)
# print("Tổng S = ", round(s,2), end=" ")
#Câu 37:
# n= int(input("Nhập n:"))
# s = 0
# for i in range(1,n+1):
#     if i%2!=0:
#         s = s + 1/(i)
# print("Tổng S = ", round(s,2), end=" ")
#Câu 38:
# n= int(input("Nhập n:"))
# s = 0
# for i in range(1,n+1):
#     if i%2==0:
#         s = s + 1/(i)
# print("Tổng S = ", round(s,2), end=" ")
#Câu 39:
# n= int(input("Nhập n:"))
# s = 0
# for i in range(1,n+1):
#     s+= i**i
# print("Tổng S = ", s, end=" ")
#câu 40
# n= int(input("Nhập n:"))
# s = 0
# for i in range(1,n+1):
#     s+= (i/(i+1))
# print("Tổng S = ", round(s,2), end=" ")
#Câu 41: sử dụng factorial(x)
# import math
# n= int(input("Nhập n:"))
# s = 0
# for i in range(1,n+1):
#     s+= (1/(math.factorial(i)))
# print("Tổng S = ", round(s,2), end=" ")
#Câu 42:
# import math
# n= int(input("Nhập n:"))
# s = 0
# tong = 0
# for i in range(1,n+1):
#     tong +=i
#     s+= (tong/(math.factorial(i)))
# print("Tổng S = ", round(s,2), end=" ")
#Câu 43:
# import math
# n= int(input("Nhập n:"))
# s = 0
# for i in range(1,n+1):
#     s = math.sqrt(2+s)
# print("Tổng S = ", round(s,2), end=" ")
#Câu 44:
# dem=0
# for i in range(2,1000):
#     nto = True
#     for j in range(2,i):
#         if i % j==0:
#             nto= False
#             break
#     if nto == True:
#         dem += 1
# print("Có ",dem," các số nguyên tố trong khoảng từ 0 < 1000 : ")
#Câu 45:
# dem = 0
# for i in range(1, 1000):
#     s = 0
#     for j in range(1, i):
#         if i % j == 0:
#             s += j
#     if s == i:
#         dem += 1
# print("Có",dem,"số hoàn thiện trong khoảng từ 0 < 1000")