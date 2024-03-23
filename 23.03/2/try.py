try:
    result = int('1')
    print(result)
except (TypeError, ValueError):
    print("Oshibka")
else:
    print("Oshibki net")
finally:
    print("I vipolnayu vsegda")
print("Konex")