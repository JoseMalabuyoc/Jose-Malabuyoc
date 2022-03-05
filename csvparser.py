def read_row(file):
    next_line = file.readline()
    if len(next_line) > 0:
        return parse_row(next_line)

    return None
    print(f'{row[0]} - {row[1]} - {row[2]}')

def parse_row(next_line):
    newLine = next_line.replace(',', ' - ').replace('\n','')
    print(newLine)
    return newLine



