
def main():
    result = 0

    try:
        with open('/Users/klr/Projects/adventPython/resources/day4input.txt') as f:
            array = f.readlines()

    except FileNotFoundError:
        print(f"The file was not found.")
    except ValueError:
        print("Found non-integer values in the file.")

    y = 0
    for (index, line) in enumerate(array):
        for(char_index, char) in enumerate(line):
            if char == 'X':
                result = result + find_xmas(char_index, index, array, 1, 0)
                result = result + find_xmas(char_index, index, array, -1, 0)
                result = result + find_xmas(char_index, index, array, 1, 1)
                result = result + find_xmas(char_index, index, array, 1, -1)
                result = result + find_xmas(char_index, index, array, -1, 1)
                result = result + find_xmas(char_index, index, array, -1, -1)
                result = result + find_xmas(char_index, index, array,  0, -1)
                result = result + find_xmas(char_index, index, array,  0, 1)



    print(f"Result: {result}")


def find_xmas(x, y, array, x_dir, y_dir):
    found = 1
    xmas = "MAS"
    for i, char in enumerate(xmas):
        newx = x + (i+1) * x_dir
        newy = y + (i+1) * y_dir
        if newx < 0 or newy < 0 or newx >= len(array[0]) or newy >= len(array):
            return 0
        if array[newy][newx] != char:
            found = 0
            break

    return found




if __name__ == "__main__":
    main()