import re

MAX_CHARS = 80

# ------------------------------------------------------------------------------
def process_line(line, line_width):
    """
    This function splits a long line into several lines of MAX_CHARS or less.
    """
    new_line = list(line)
    line_length = len(new_line)
    # Search for the starting index, so that spaces at the beginning of the line
    # are not considered. Plus, if there are `line_width` spaces at the
    # beginning they are removed.
    end_idx = line_width
    start_idx = 0
    while (start_idx < line_length and
           (new_line[start_idx] == " " or 
            new_line[start_idx] == "\t")):
        start_idx = start_idx + 1
        if start_idx == line_width:
            new_line = new_line[:line_width]
            start_idx = 0
    
    idx = end_idx
    counter = 0
    while idx < line_length: 
        c = new_line[idx]
        if (c == " " or c == "\t"):
            new_line[idx] = "\n"
            start_idx = idx + 1
            end_idx = start_idx + line_width
            idx = end_idx
        else:
            idx = idx - 1
        # In case there is a sequence of more than 80 characters, then split it
        # in two lines by inserting a "\n" character, instead of replacing a
        # whitspace by a "\n".
        if idx == start_idx:
            temp_line = new_line[:end_idx]
            if start_idx < line_width:
                start_idx = 0
            temp_line.append("\n")
            temp_line.extend(new_line[end_idx:])
            new_line = temp_line
            # increase the line length by one (the character added)
            line_length = line_length + 1
            temp_line = None

            start_idx = end_idx + 1 
            end_idx = start_idx + line_width
            idx = end_idx
        counter = counter + 1
    new_line.append("\n")
    return "".join(new_line)

# ------------------------------------------------------------------------------
inputf = open("./diary.txt", "r")
# inputf = open('./prueba.txt', 'r')
outputf = open("./diary_new.txt", "w")

for line in inputf:
    # Blank lines are left with just the "\n" character, removing any
    # unnecessary white space, probably left there by mistake.
    if len(line.rstrip()) == 0:
        line = "\n"
    if len(line) > MAX_CHARS:
        new_line = process_line(line.rstrip(), MAX_CHARS)
    else:
        new_line = line
    # print(new_line)
    outputf.write(new_line)

inputf.close()
outputf.close()

# ------------------------------------------------------------------------------
# Check that the new file contains lines at most MAX_CHARS long
inputf = open("./diary_new.txt", "r")

for line in inputf:
    if len(line[:-1]) > MAX_CHARS:
        print("WHAT THE?")
        print(line)
inputf.close()
