def read_row(file):
    next_line = file.readline()

    if len(next_line) > 0:
        return parse_row(next_line)

    return None

def parse_row(next_line):
    return ''

