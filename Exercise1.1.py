def count_letters(word):
    # Khởi tạo một từ điển để lưu trữ số lần xuất hiện của mỗi chữ cái
    letter_count = {}

    # Duyệt qua từng ký tự trong từ
    for char in word:
        # Chuyển đổi ký tự thành chữ thường để đảm bảo tính nhất quán
        char_lower = char.lower()

        # Kiểm tra xem ký tự có phải là chữ cái không
        if char_lower.isalpha():
            # Tăng số lần xuất hiện của ký tự trong từ điển
            letter_count[char_lower] = letter_count.get(char_lower, 0) + 1

    return letter_count

# Ví dụ sử dụng
word = "Hello"
print(count_letters(word))
