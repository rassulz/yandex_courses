hours = int(input())
minutes = int(input())
delivery = int(input())

# Общие минуты
total_minutes = minutes + delivery

# Считаем новые часы и минуты
extra_hours = total_minutes // 60
new_minutes = total_minutes % 60

new_hours = (hours + extra_hours) % 24

print(f"{new_hours:02d}:{new_minutes:02d}")
