def find_common_elements(num_list1, num_list2):
    index_received = []  # Danh sách chứa chỉ số của các phần tử đã được khớp từ danh sách khác
    result = []  # Danh sách kết quả chứa các phần tử chung

    # Duyệt qua từng phần tử trong num_list1
    for i, ele1 in enumerate(num_list1):
        # Duyệt qua từng phần tử trong num_list2
        for j, ele2 in enumerate(num_list2):
            # Kiểm tra nếu ele1 và ele2 giống nhau và chỉ số của ele2 chưa được sử dụng
            if ele1 == ele2 and j not in index_received:
                # Thêm ele1 vào danh sách kết quả
                result.append(ele1)
                # Thêm chỉ số của ele2 vào danh sách index_received
                index_received.append(j)
                # Đã tìm thấy phần tử khớp, thoát khỏi vòng lặp trong
                break

    return result

# Ví dụ sử dụng
num_list1 = [1, 2, 3, 4, 5]
num_list2 = [3, 4, 5, 6, 7]
print(find_common_elements(num_list1, num_list2))
