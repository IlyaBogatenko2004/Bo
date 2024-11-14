# задача D
start = int(input())
end = int(input())
if start <= end:
    numbers = [i for i in range(start, end + 1)]
else:
    numbers = [i for i in range(start, end - 1, -1)]
print(" ".join(map(str, numbers)))
