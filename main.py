import sys

from module import DList


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("incorrect command line! \n"
              "Waited: command in_file out_file")
        sys.exit(1)

    try:
        input_file = open(sys.argv[1], "r")
    except OSError:
        print(f"File opening error ({sys.argv[1]})")
        sys.exit(1)

    try:
        output_file = open(sys.argv[2], "w")
    except Exception:
        input_file.close()
        print(f"File opening error ({sys.argv[2]})")
        sys.exit(1)

    print("Start")

    container = DList()
    container.read_from(input_file)

    print("Filled container.")

    container.compare_films()
    print("Compare films done")

    container.sort()
    container.write_to(output_file)
    container.write_game_film_to(output_file)
    container.clear()

    print("Empty container.")
    container.write_to(output_file)

    print("Stop.")

    input_file.close()
    output_file.close()
