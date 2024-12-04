from operator import truediv


def main():
    safe_count = 0
    try:
        with open('/Users/klr/Projects/adventPython/resources/day2input.txt') as f:
            for line in f:
                numbers = line.split(' ')
                levels = []
                for index, num in enumerate(numbers):
                    val = int(num.strip())
                    levels.append(val)
                is_safe, bad_level = check_levels(levels)
                if not is_safe:
                    that_level = bad_level + 1
                    new_list = levels.copy()
                    new_list.pop(bad_level)
                    is_safe, bad_level = check_levels(new_list)
                    if not is_safe:
                        new_list = levels.copy()
                        new_list.pop(that_level)
                        is_safe, bad_level = check_levels(new_list)
                if is_safe:
                    safe_count = safe_count + 1

    except FileNotFoundError:
        print(f"The file was not found.")
    except ValueError:
        print("Found non-integer values in the file.")

    print(f"Safe levels: {safe_count}")


def check_levels(a_list):
    safe = True
    index = 0
    increasing = (a_list[-1] - a_list[0]) > 0
    for index, num in enumerate(a_list):
        if index == len(a_list)-1:
            break
        diff = a_list[index+1] - num
        safe = 0 < abs(diff) < 4
        safe = safe and ((increasing and diff>0) or (not increasing and diff <0))
        if not safe:
            return safe, index

    return safe, -1

if __name__ == "__main__":
    main()