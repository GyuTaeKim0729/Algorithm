def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: (x, len(x)))
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return answer


if __name__ == '__main__':
    result = False
    phone_book = ["119", "97674223", "1195524421"]
    solution_result = solution(phone_book)
    print("Success" if result == solution_result else "Fail")
