print("=== NHẬP DỮ LIỆU ĐẦU VÀO CHO HỆ THỐNG ===")
code_patient = input("Nhập Mã bệnh nhân (ví dụ: BN999): ").strip()
temp = float(input("Nhập Nhiệt độ cơ thể (°C): "))
heart_rate = int(input("Nhập Nhịp tim (nhịp/phút): "))

print("\n" + "."*50 + "\n")

print("--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print(f"Mã bệnh nhân: {code_patient}")
print(f"Nhiệt độ cơ thể: {temp} độ C")
print(f" => Kiểu dữ liệu hệ thống ghi nhận: {type(temp)}")
print(f"Nhịp tim: {heart_rate} nhịp/phút")
print(f" => Kiểu dữ liệu hệ thống ghi nhận: {type(heart_rate)}")
print("-" * 75)
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")
print("-" * 75)

#Input là nhập vào nhiệt độ cơ thể ( kiểu dữ liệu: float ) - mã bênh nhân là string - nhịp tim là int
#Output là sẽ xuất hiện thông tin vừa nhập vào và trả kiểu dữ liệu cuối cùng của nó là gì cho nhịp tim và nhịp đồ cơ thể 
# So sánh về chưa ép kiểu(1) và đã ép kiểu(2)
# (1) và (2) tương đương nhau về số lượng biến cần dùng
# Độ ngắn gọn của code thì (1) ngắn ít hơn (2)
# khả năng dò lỗi thì (1) kém hơn (2) nhiều , chính vì vậy phải kiểm soát ngay từ ban đầu
# --> (2) nên lựa chọn hơn