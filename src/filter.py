def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()


def filter_lines(lines, keyword):
    return [line for line in lines if keyword in line]


def write_file(file_path, lines):
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)


def process_file(input_path, keyword, output_path="filtered.txt"):
    lines = read_file(input_path)
    filtered = filter_lines(lines, keyword)
    write_file(output_path, filtered)
