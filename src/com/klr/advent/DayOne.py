
def main():
    list1 = []
    list2 = []
    map1 = {}
    map2 = {}

    try:
        with open('/Users/klr/Projects/adventPython/resources/Advent1input.csv') as f:
            for line in f:
                numbers = line.split(',')
                for index, num in enumerate(numbers):
                    val = int(num.strip())
                    if index == 0:
                        list1.append(val)
                        if map1.get(val):
                            map1[val] += 1
                        else:
                            map1[val] = 1
                    else:
                        list2.append(val)
                        if map2.get(val):
                            map2[val] += 1
                        else:
                            map2[val] = 1
    except FileNotFoundError:
        print(f"The file was not found.")
    except ValueError:
        print("Found non-integer values in the file.")

    list1.sort()
    list2.sort()
    diff = 0
    for i, num in enumerate(list1):
        diff += abs(num - list2[i])

    print(f"Answer Part 1: {diff}")

    sum = 0
    for key, value in map1.items():
        if map2.get(key):
            sum += value * (map2[key] * key)

    print(f"Answer Part 2: {sum}")


if __name__ == "__main__":
    main()
