# задача O
hours = int(input())
minutes = int(input())
delivery_time = int(input())
delivery_minutes = hours * 60 + minutes + delivery_time
delivery_hours = (delivery_minutes // 60) % 24
delivery_minutes = delivery_minutes % 60
print(f"{delivery_hours:02d}:{delivery_minutes:02d}")
    