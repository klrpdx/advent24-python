
def main():
    list1 = []
    list2 = []
    try:
        with open('/Users/klr/Projects/adventPython/resources/Advent1input.csv') as f:
            for line in f:
                numbers = line.split(',')
                for index, num in enumerate(numbers):
                    if index == 0:
                        list1.append(int(num.strip()))
                    else:
                        list2.append(int(num.strip()))
    except FileNotFoundError:
        print(f"The file was not found.")
    except ValueError:
        print("Found non-integer values in the file.")

    list1.sort()
    list2.sort()
    diff = 0
    for i, num in enumerate(list1):
        diff += abs(num - list2[i])

    print(f"Answer: {diff}")

if __name__ == "__main__":
    main()
