x = 10
y = 3.14
name = "John"
is_true = True


print("1: ", True)
print("2: ", False)

print(abs(-12.5), f"!== {abs(12.5)}")
print(abs(20), f"=== {abs(20)}")

letters = ["с", "s", "s"]
for i in range(len(letters)):
    print(f"буква {i}  {letters[i]}")

numbers = [1, 2, 3]
for i in range(len(numbers)):
    print(f"На позиції {i} знаходиться номер {numbers[i]}")
    


sth = True
print("Значить sth=True" if sth else "Значить sth=False")
number = 42
print(f"Number is {number}. It is {'even' if number % 2 == 0 else 'odd'}.")


numerator = 10
denominator = 0

try:
    result = numerator / denominator
    print(f"The result is: {result}")
except ZeroDivisionError as e:
    print(f"Error: {e} - Cannot divide by zero.")
finally:
    print("This block always executes, regardless of whether there was an error or not.")

# Assume there is a file named "example.txt" with some content
file_path = "example.txt"

# Using a context manager to open and read the file
with open(file_path, "r") as file:
    for line_number, line_content in enumerate(file, 1):
        print(f"Line {line_number}: {line_content.strip()}")

# The file is automatically closed outside the 'with' block

this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda('Настя', 'Крижанівська'))

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Помилка: {e}")
else:
    print("Все в порядку")
finally:
    print("Цей блок завжди виконується")


def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print(result) 