def multiply(a, b):
    return a * b
 # Run some example multiplications and print results
if __name__ == "__main__":
    numbers = [(1, 1), (2, 2), (3, 3), (4, 4), (23, 45)]
    for a, b in numbers:
        print(f"{a} x {b} = {multiply(a, b)}")