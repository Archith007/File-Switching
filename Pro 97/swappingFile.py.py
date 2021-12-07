file1 = input("Enter The Name of the First File:-")
file2 = input("Enter The Name of the Second File:-")

def swap():
    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as a:
        data_b = a.read()

    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file2, 'w') as a:
        a.write(data_a)

swap()

