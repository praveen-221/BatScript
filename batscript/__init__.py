"""BatScript"""
from . import ast, lexer, parser, runner, utils

__all__ = ["parser", "ast", "lexer", "runner", "utils"]

__version__ = "0.1"
__version_str__ = (
    f"BatScript v{__version__}."
    + "\nBatScript is a programming language based on the dialogues of Batman Triology."
    + "\nCreated by LoneWolf."
)

bts = runner.BatScriptRunner()
