#Задача H
def is_palindrome(n):
    return str(n) == str(n)[::-1] if isinstance(n, int) else n == n[::-1]