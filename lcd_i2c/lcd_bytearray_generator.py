def main():
    custom_char = [
        '.....',
        '@@.@@',
        '@@.@@',
        '.....',
        '@...@',
        '@@.@@',
        '.@.@.',
        '..@..'
    ]

    bytearray_output = []
    succes = True
    for i in custom_char:
        if (len(i) != 5):
            print(f"Wrong size in column ({len(i)}). Expected 5.")
            succes = False
            break
        row_string = i.replace('@', '1')
        row_string = row_string.replace('.', '0')
        for j in row_string:
            if j not in ['0', '1']:
                print(f"Wrong char in column ({j}). Expected @ or .")
                succes = False
                break
        else:  # only executed if the inner loop did NOT break
            row_bin = int(row_string, 2)
            bytearray_output.append(hex(row_bin))

    if succes:
        output = str(bytearray_output).replace("'", "")  # easier copy/paste from terminal
        print(output)


if __name__ == "__main__":
    main()
