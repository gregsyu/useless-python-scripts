import tempfile
import csv
import re

""" This script processes a text file containing lines with website information and descriptions, 
    transforms the data, and prints it in a formatted manner. """


def with_tempfile():
    txt_file_path = "/path/to/file.txt"
    # the content of the file must be something like this:
    # ```
    # example.com       -- This website does something...
    # other.example.com -- This website does a lotta stuff...
    # ...
    # ```
    #
    # It's based on a file i got with some websites that i found interesting..

    # optional variable `delete` is True by default
    with tempfile.NamedTemporaryFile(mode='w+') as temp_file, open(txt_file_path) as in_file:
        for line in in_file:
            if not line == "\n":
                modified_line = re.sub(r'\s+--\s+', ',', line)
                temp_file.write(modified_line)
        temp_file.seek(0)  # Rewind the modified file to the beginning before reading

        for website, description in csv.reader(temp_file):
            print(f"Website: \x1b[32m{website}\x1b[0m\nDescription: \x1b[34m{description}\x1b[0m\n")


# def without_tempfile():
#     txt_file_path = "/home/greg/stuff/sites.txt"
#     csv_file_path = "/home/greg/stuff/sites.csv"

#     with open(txt_file_path) as in_file, open(csv_file_path, 'w') as out_file:
#         for line in in_file:
#             if not line == "\n":
#                 modified_line = re.sub(r'\s+\-\-\s+', ',', line)
#                 out_file.write(modified_line)

#     with open(csv_file_path) as file:
#         reader = csv.reader(file)
#         for website, description in reader:
#             print(f"Website: \x1b[32m{website}\x1b[0m\nDescription: \x1b[34m{description}\x1b[0m\n")


if __name__ == "__main__":
    with_tempfile()
