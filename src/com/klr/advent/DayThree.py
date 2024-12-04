import re

def main():
    result = 0
    text=""
    try:
        with open('/Users/klr/Projects/adventPython/resources/day3input.txt') as f:
            text = f.read()

    except FileNotFoundError:
        print(f"The file was not found.")
    except ValueError:
        print("Found non-integer values in the file.")

    findmuls = "mul\((\d+),(\d+)\)"
    ignoreThis = "don't\(\)(.*?)do\(\)"
    text = text.replace("\n", "")
    text = re.sub(ignoreThis, "", text)
    muls = re.findall(findmuls, text)
    for mul in muls:
        result += int(mul[0])*int(mul[1])

    print(f"Result: {result}")

if __name__ == "__main__":
    main()