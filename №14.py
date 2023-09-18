N = int(input("Введите число N: "))

powers_of_two = []

for i in range(1, N+1):
    if i == 1 or i % 2 == 0:
        powers_of_two.append(i)

print("Целые степени двойки, не превосходящие N:", end=" ")
print(*powers_of_two, sep=", ")