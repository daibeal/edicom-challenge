#!/user/bin/env python3 -tt


# Imports
import sys
####º##############################################################################
def check_times(arr, ntimes):
    chars = "abcdefghijklmnopqrstuvwxyzñ"
    for char in chars:
        count = arr.count(char)
        if count == ntimes:
            return True
    return False
###############################################################################
def read_file(file):
    a_file = open(file)
    file_contents = a_file.read()
    contents_split = file_contents.splitlines()
    return contents_split
###############################################################################
def main():
    three_global = 0
    four_global = 0
    input_file = sys.argv[1]
    arr = read_file(input_file)

    for i in arr:
        three_global += 1  if check_times(i, 3) else 0
        four_global  += 1  if check_times(i, 4) else 0

    print("Result:",str(three_global) + " - " + str(four_global) + " = " + str( three_global-four_global))
    if not input_file:
        print('usage: [input file] ')
        sys.exit(1)
# Main body
if __name__ == '__main__':
    main()