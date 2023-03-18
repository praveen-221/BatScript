import sys

from loguru import logger
from typer import Typer

from . import __version__, __version_str__, bts

app = Typer()


@app.command()
def version():
    """prints version and exits."""
    print(__version_str__)


@app.command()
def tokenize(file_path: str):
    """prints the tokens from the program."""
    logger.remove()
    logger.add(sys.stderr, level="ERROR")

    with open(file_path, "r") as f:
        code_str = f.read()

    tokens = bts.tokenize(code=code_str)
    for token in tokens:
        print(token)


@app.command()
def run(file_path: str, debug: bool = False):
    """executes a BatScript program."""
    level = "DEBUG" if debug else "ERROR"
    logger.remove()
    logger.add(sys.stderr, level=level)

    with open(file_path, "r") as f:
        code_str = f.read()

    bts.exec(code=code_str, log_level=level)


@app.command()
def shell():
    print(f"BatScript v{__version__}")
    while True:
        code_line = input("batscript>> ")
        output = bts.eval(code_line)
        if output is not None:
            print(output)


@app.callback()
def main():
    """
    BatScript is a hobby programming language based on the dialogues of Batman Triology.
    """


if __name__ == "__main__":
    app()
