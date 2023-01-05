"""
Giai thừa của 1 số nguyên dương n là tích của tất cả các số nguyên dương nhỏ hơn hoặc
bằng n. Công thức như sau:
Viết mã giả mô tả thuật toán tính giai thừa của một số n cho trước.
"""

def giai_thua(n):
    if n < 0 or type(n) is not int :
        print ("n khong phai so nguyen duong , nhap lai n")

    else :
        result = 1 
        for i in range(1,n+1):
            result = result *i
        
        print ("{}! = {}".format(n,result))

giai_thua(10)
    

