import re

inputf = open('./diary.txt', 'r')
outputf = open('./diary_new.txt', 'w')

# ------------------------------------------------------------------------------
def process_line(line):
    """
    This function splits a long line into several lines of MAX_CHARS or less.
    It will not behave as expected in the following situation:
        - 4 spaces, then 80 characters straight.
        - 84 characters, all together.
    """
    new_line = list(line)
    idx = 80 
    line_length = len(new_line)
    while idx < line_length and idx >= 0:
        c = new_line[idx]
        if (c == " " or c == "\t"):
            new_line[idx] = "\n"
            idx = idx + 80
        else:
            idx = idx - 1
    new_line.append("\n")
    return "".join(new_line)

# ------------------------------------------------------------------------------
MAX_CHARS = 80

for line in inputf:
    if len(line) > MAX_CHARS:
        new_line = process_line(line.rstrip())
    else:
        new_line = line
    # print(new_line)
    outputf.write(new_line)

inputf.close()
outputf.close()
