"""
# BatScript python runner.
The bastscript runner exposes the batscript interpreter
to python scripts.
"""

import os
import sys
import warnings
from pathlib import Path

from loguru import logger

from .lexer import Lexer
from .parser.parser import LineParser, ParserBase, ProgramParser
from .utils import read_yml


class BatScriptRunner:
    """
    The BatScript Runner handles the execution of BatScript code.
    """

    def __init__(self) -> None:

        yml_path = os.path.join(Path(__file__).parent, "token.yml")
        self.tokens_dict = read_yml(yml_path)

        self.__pgm_parser = self.__init_parser(ProgramParser)

        # * we ignore warnings related to unused tokens.
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            logger.warning(
                "LineParser supports only a subset of BatScript features."
            )
            self.__line_parser = self.__init_parser(LineParser)

    def __init_parser(self, Parser: ParserBase):
        parser = Parser(list(self.tokens_dict.keys()))
        parser.parse()
        return parser.get_parser()

    def __eval(self, parser, code):
        parsed_tokens = parser.parse(self.tokenize(code))
        return parsed_tokens.eval()

    def tokenize(self, code: str):
        """
        tokenize tokenizes the input code.

        Args:
            code (str): the batscript code to tokenize.

        Returns:
            LexerStream: a generator of the tokens.
        """
        lexer = Lexer(self.tokens_dict).get_lexer()
        tokens = lexer.lex(code)
        return tokens

    def exec(self, code: str, log_level: str = "INFO"):
        """
        exec executes a complete batscript program.

        Args:
            code (str): the batscript program to execute.
            log_level (str, optional): log level. Defaults to "ERROR".
        """
        logger.remove()
        logger.add(sys.stderr, level=log_level)
        self.__eval(self.__pgm_parser, code)

    def eval(self, code_line: str):
        """
        eval evaluates a batscript statement.

        **NOTE**: eval supports only a subset of batscript features.

        Args:
            code_line (str): batscript statement to evaluate.

        Returns:
            _type_: output of the evaluation.
        """
        logger.remove()
        logger.add(sys.stderr, level="ERROR")
        return self.__eval(self.__line_parser, code_line)
