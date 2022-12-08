def write_results(filepath, part1: str, part2: str) -> None:
    with open((filepath.rstrip("code.py")+"output.txt"), 'w') as output_file:
        output_file.writelines(part1)
        output_file.writelines('\n')
        output_file.writelines(part2)

    with open((filepath.rstrip("code.py")+"output.txt"), 'r') as output_file:
        content = output_file.read()
        print(content)

