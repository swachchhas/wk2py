numbers = [10, 12, 15, 35, 48, 52, 20, 25]

for num in numbers:
    if num > 50:
        break
    if num % 5 == 0:
        continue
    print(num)
  