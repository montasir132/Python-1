def check_palindrome_with_reversed(str_n):
    text = str_n
    revers_str = "".join(reversed(str_n))
    if text == revers_str:
        return "palindrome"
    return "Not palindrome"
n = str(input())
res = check_palindrome_with_reversed(n.lower())
print(res)