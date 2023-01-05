"""
Cho định nghĩa sau: số hoàn hảo là số có giá trị bằng tổng các ước nhỏ hơn nó.
Ví dụ: 6=1+2+3; 28=1+2+4+7+14.
Viết mã giả mô tả thuật toán kiểm tra 1 số n cho trước có phải là số hoàn hảo hay không.
"""

def perfect_number(n):
    if (n <= 0) or ( type(n) is not int) : 
        print (" {} khong phai so nguyen duong duong, moi nhap lai ! ".format(n))
    else:
        list_uoc = []
        for i in range(1,n-1):
            if n % i == 0 :
                list_uoc.append(i)
        sum_uoc = 0
        for j in list_uoc:
            sum_uoc += j
    if sum_uoc == n :
        print (" {} la so hoan hao ! ".format(n))
    if sum_uoc != n :
        print (" {} khong phai so hoan hao, try again :3 ".format(n))
perfect_number(28)