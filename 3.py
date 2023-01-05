"""
3. Với chuỗi cho trước có độ dài lớn hơn 1, viết mã giả thể hiện thuật toán xác định vị trí của
1 kí tự trong chuỗi sao cho khi xoá kí tự đó đi thì chuỗi còn lại là nhỏ nhất có thể.
Ví dụ: chuỗi `231` sau khi xoá đi 1 kí tự có thể trở thành `31`, `21`, `23`. Chuỗi nhỏ nhất là
`21`, đáp án đúng là xoá đi kí tự `3` trong chuỗi ban đầu.
"""

def tim_vi_tri_can_xoa(n):
    if len(str(n)) == 1 :
        print ("chuoi co do dai nho hon 1, moi nhap lai ! ")
    else : 
        do_dai = len(str(n))
        list_cutted = []
        for i in range(0,do_dai):
            n_list = list(str(n))
            n_list.pop(i)
            new_str = "".join(n_list)
            list_cutted.append(int(new_str))
        smallest_num = list_cutted[0]
        for num in list_cutted:
            if smallest_num >= num:
                smallest_num = num
                index = list_cutted.index(num) +1
                deleted_number = str(n)[index-1]
        print('Xoa ki tu co vi tri thu {} - tuong ung so "{}" de duoc so nho nhat co gia tri {}'.format(index,deleted_number,smallest_num))
tim_vi_tri_can_xoa(231)
        


    