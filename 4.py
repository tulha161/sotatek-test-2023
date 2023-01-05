"""
4. Bob cầm n đồng đi mua kẹo. Giá của 1 viên kẹo là c đồng. Cửa hàng lại có chương trình
khuyến mại cứ m tờ giấy gói kẹo thì đổi được 1 viên kẹo mới. Viết mã giả thể hiện thuật toán
xác định tổng số kẹo Bob có thể mua được từ các tham số n, c, m như đã mô tả ở trên.
Ví dụ:
●n=10, c=2, m=5: Bob mua được 5 viên kẹo, sau đó đổi 5 tờ giấy gói lấy 1 viên kẹo
nữa, tổng cộng đáp án là 6.
●n=12, c=4, m=4: Bob mua được 3 viên kẹo, số giấy gói kẹo không đủ đổi thêm nữa,
đáp án cuối cùng là 3.
●n=6, c=2, m=2: Bob mua được 3 viên kẹo, lấy 2 trong 3 tờ giấy gói kẹo đổi được
thêm 1 viên. Sau đó dùng tiếp 1 tờ giấy gói dư ở lần đổi thứ nhất + tờ giấy gói của
viên kẹo ở lần đổi thứ 2, đổi được thêm 1 viên kẹo nữa. Đáp án tổng cộng là 5.
"""

def bob_can_buy(n,c,m):
    if n <= 0 or c <= 0 or m <=0  :
        print ("Wrong Input")
    if n < c :
        print ("Bob khong du tien mua 1 vien keo rui :( xin me them nhe ! ")
    if n == c : 
        print ("Bob du tien mua 1 vien keo duy nhat, enjoy ~!")
    if n > c and m == 1 :
        print ("Bob an keo forever :D ")
        
    if n > c and m >1 :     
        candy_can_buy =  int(n/c)
        candy_can_trade = int(candy_can_buy/m)
    
        leftover_wrappers = candy_can_buy % m

        if (candy_can_trade + leftover_wrappers) < m :
            total_candy = candy_can_buy + candy_can_trade

        if (candy_can_trade + leftover_wrappers ) >= m :
            total_wrappers = leftover_wrappers + candy_can_trade
            candy_can_trade += int(total_wrappers/m)
            total_candy = candy_can_buy + candy_can_trade

        print ("Bob co the mua {} vien keo".format(total_candy) )
bob_can_buy(10,2,2)