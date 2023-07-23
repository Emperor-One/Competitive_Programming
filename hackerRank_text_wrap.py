import textwrap
def wrap(string, max_width):
    filler = " " * (max_width - len(string) % max_width)
    string += filler
    lines = len(string) // max_width
    index = 0
    new_string = ""
    for _ in range(lines):
        for _ in range(max_width):
            new_string += string[index]
            index += 1
        new_string += '\n'

    return new_string
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
