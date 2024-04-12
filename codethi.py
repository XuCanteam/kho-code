#Chuyển đổi chuỗi sang list
# string = 'Python'
# my_list = list(string)
# print(my_list)
#====================================
#Sử dụng hàm range():

#VD:
# list1=list(range(10))#Output:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2=list(range(2,10))#Output:[2, 3, 4, 5, 6, 7, 8, 9]
# list3=list(range(2,10,2))#Output:[2, 4, 6, 8]
# print(list1)
# print(list2)
# print(list3)
#====================================
#Thao tác với biến
#VD:
# list = ['Toán','Lý','Sinh']
# print(list[0])#Output: Toán
# print(list[1])#//:Lý
# print(list[2])#//:Sinh

#Trường hợp có list con:
# #VD:
# list2 = ['Toán','Lý','Hóa',['Văn','Anh'],'Sử']
# print(list2[3][1])#Output: Anh
# #Cập Nhật giá trị mới
# list2[2] = 'Địa'
# print(list2[2])#Output: Địa
#==========================================



#===============================================================================================
# list1=[1,2,3]
# list2=[1,2]
# list1.append(list2)
# print(list1)#Output: [1, 2, 3, [1, 2]]
# list3=[1,2,3]
# list4=[1,2]
# list3.extend(list4)
# print(list3)#Output:[1, 2, 3, 1, 2]
#Chèn phần tử ở vị trí nào đó
# list1=[1,2,3]
# list1.insert(1,3)
# print(list1)#Output:[1, 3, 2, 3]
# list1=[1,2,3]
# list1.insert(-1,4)
# print(list1)#Output:[1, 2, 4, 3]

#==================================================
# list1=[1,2,3,4]
# x=list1.pop()
# print(list1)#Output:[1, 2, 3]
# print(x)#Output:4
#==================================================

# list1 = [1,2,3,4,5,6,7,8,9]
# sort_list= sorted(list1)
# print(sort_list)
# list1.sort(reverse=True)
# print(list1)
#============Bài Tập========================
#Caau 1.Nhập một danh sách gồm các phần tử số nguyên, ngưng khi người dùng nhập -1. Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập.
list = []
while True:
    n = int(input("Nhập danh sách gồm các phần tử số nguyên: "))
    if n==-1:
        break
    list.append(n)
print("Danh sách vừa nhập là: " ,list)
print("Số lớn nhất trong list vừa nhập là: ",max(list))
print("Số nhỏ nhất trong list vừa nhập là: ",min(list))
#Caau2.	Nhập một danh sách L gồm các phần tử bao gồm chuỗi và số nguyên. Kiểm tra xem các phần tử trong danh sách L có phải chuỗi và số xen kẽ không.
# list = []
# count_list = False
# while True:
#     L = (input("Nhập danh sách L gồm các phần tử bao gồm chuỗi và số nguyên(Nhập done để kết thúc): "))
#     if L=='done':
#         break
#     list.append(L)
# for i in range(len(list)):
#     if list[i].isdigit() and list[i+1].isalpha():
#         count_list = True
#         break
#     elif list[i].isalpha() and list[i+1].isdigit():
#         count_list = True
#         break
#     else:
#         count_list = False
#         break
# if count_list==True:
#     print("Chuỗi và số nguyên xen kẽ trong danh sách")
# else:
#     print("Chuỗi và số nguyên không xen kẽ trong danh sách")

#Câu 3.	Nhập một chuỗi gồm các từ cách nhau bởi khoảng trắng. Cắt các từ có trong chuỗi và đưa vào danh sách L1. Sau đó tạo một danh sách L2 bằng cách nhập các giá trị từ bàn phím. Ghép danh sách L2 vào sau L1 rồi in ra màn hình.
# chuoi = input("Nhập chuỗi: ")
# L1 = chuoi.split()#hàng split() dùng để cắt các từ thành danh sách
# print("Chuỗi sau khi tách là: " ,L1)

# L2 = []
# n = int(input("Nhập danh sách số lượng để thêm danh sách: "))
# for i in range(n):
#     gia_tri = input(f"Nhập giá trị thứ {i+1}: ")
#     L2.append(gia_tri)
# L1.extend(L2)
# print("Danh sách L1 sau khi ghép L2 vào: " ,L1)

#Câu 4.	Nhập vào một list L có các phần tử là chuỗi (các chuỗi này không có ký tự đặc biệt, dấu câu, ký tự số, chỉ có ký tự chữ cái và khoảng trắng). Hãy tìm ra vị trí của chuỗi có nhiều ký tự nhất
# list_L = input("Nhập vào chuỗi cách nhau bởi dấu : ").split(",")
# vi_tri_max = 0
# max_dai = len(list_L[0])
# for i in range(1,len(list_L)):
#     if list_L[i] > max_dai:
#         vi_tri_max = i
#         max_dai = len(list_L[i])
# print("Vị trí của chuỗi có nhiều ký tự nhất là: ",vi_tri_max)

#Câu 5.	Viết chương trình nhập số nguyên dương n, và tạo danh sách gồm n số nguyên ngẫu nhiên từ 1 đến 100. Thực hiện các công việc sau:
# import random
# n = int(input("Nhập số lượng ký tự: "))
# list_Duong = 0
# list_Am = 0
# list_chan = 0
# list_le = 0
# random_list = [random.randint(1,100) for _ in range(n)]
# print(random_list)
# print("Các số dương trong danh sách:")
# for num in random_list:
#     if num > 0:
#         print(num, end=' ')
# print()

# # In ra các số âm
# print("Các số âm trong danh sách:")
# for num in random_list:
#     if num < 0:
#         print(num, end=' ')
# print()

# # In ra các số chẵn
# print("Các số chẵn trong danh sách:")
# for num in random_list:
#     if num % 2 == 0:
#         print(num, end=' ')
# print()

# # In ra các số lẻ
# print("Các số lẻ trong danh sách:")
# for num in random_list:
#     if num % 2 != 0:
#         print(num, end=' ')
# print()