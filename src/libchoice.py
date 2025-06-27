import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--question', type=str, required=True)
    parser.add_argument('-ot', '--option_type', type=str, choices=['s', 'm'], required=True)
    parser.add_argument('-o', '--options', type=str, default='')  # Comma-separated for -ot m
    parser.add_argument('-f', '--file', type=str, default='libchoice_result.txt')  # Optional output file

    args = parser.parse_args()
    result = None

    if args.option_type == 's':
        print(args.question)
        result = input("> ").strip()

    elif args.option_type == 'm':
        options = [opt.strip() for opt in args.options.split(',')]
        print(args.question)
        for idx, opt in enumerate(options, start=1):
            print(f"[{idx}] {opt}")
        while True:
            choice = input("> ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                result = options[int(choice)-1]
                break
            else:
                print("Invalid choice. Try again.")

    # Write result to file
    if result is not None:
        filePath = args.file
        with open(filePath, "w", encoding="utf-8") as f:
            f.write(result)

main()