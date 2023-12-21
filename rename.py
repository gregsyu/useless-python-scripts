from glob import glob
from pathlib import Path

""" This script rename all the files in a given directory, replacing a comma with a single dash """


def main():
    files = glob("path/to/dir/**/*")

    for file in files:
        # if basename(__file__) in file:
        if not isfile(file) or "," not in file:
            continue
        print(f" => {file!r};")
        Path(file).rename(file.replace(",", "-"))


if __name__ == "__main__":
    main()
