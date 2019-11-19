# yields are used in generators
# yield returns the value and resumes the function where it is left off

def generate(number):
    for i in range(0, number):
        yield i
        # resumes here after returning i

for num in generate(10):
    print(num)

