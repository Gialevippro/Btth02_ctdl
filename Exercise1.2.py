def count_words_in_file(file_path):
    # Khởi tạo một từ điển để lưu trữ số lần xuất hiện của mỗi từ
    word_count = {}

    # Mở tệp và đọc các câu
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Duyệt qua từng câu
    for line in lines:
        # Chuyển đổi các từ trong câu thành chữ thường và tách chúng thành danh sách các từ
        words = line.lower().split()

        # Duyệt qua từng từ và tăng số lần xuất hiện của từ đó trong từ điển
        for word in words:
            # Loại bỏ ký tự đặc biệt như dấu câu, nếu có
            word = ''.join(char for char in word if char.isalnum())

            # Kiểm tra xem từ có phải là từ rỗng không
            if word:
                word_count[word] = word_count.get(word, 0) + 1

    return word_count

# Ví dụ sử dụng
file_path = 'P1_data.txt'  # Đường dẫn tới tệp văn bản
word_counts = count_words_in_file(file_path)
print(word_counts)
