/**
Giới thiệu một số hàm built in
1. Console
2. Confirm
3. Prompt
4. Set timeout
5. Set interval
*/

console.log('Day la thong bao')

console.warn(123)


var fullName = 'Duong Manh Cuong'

console.log(fullName)

// hiển thị cái thông báo kêu xác nhận
confirm('Xac nhan ban du 18 tuoi')

// hiện cái box kêu nhập rùi bấm xác nhận
prompt("xac nhan gioi tinh")


// thằng này chạy 1 lần
setTimeout(function() {
    alert("hello")
}, 3000);


// thằng này sẽ chạy lại cứ sau 1 khoảng thời gian nhất định được thiết lập ở tham số thứ 2
setInterval(function() {
    console.log("Day la random: " + Math.random())
}, 2000)