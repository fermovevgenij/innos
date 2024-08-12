def my_generator():
    yield [2, 13, 0.0026028575468141258]

# Example of using the generator
generator = my_generator()
for item in generator:
    print(item)
