from glob import glob
import shutil
import os

extensions = [
    (".py", "python"),
    (".jpg", "jpg"),
    (".txt", "text"),
    (".md", "markdown"),
    (".gpg", "gpg"),
]

def main():
    files = glob("./*")

    for file in files:
        if os.path.isfile(file):
            for extension, name in extensions:
                if file.endswith(extension):
                    debug(f"{name} file detected")
                    os.makedirs(f"./{name}", exist_ok=True)
                    shutil.move(file, f"./{name}")


def debug(string: str):
    print(f"\x1b[31mDEBUG: `{string}'\x1b[0m")


if __name__ == "__main__":
    main()
