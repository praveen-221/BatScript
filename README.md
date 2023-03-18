# batscript

![banner_thin](https://user-images.githubusercontent.com/6749212/168450764-5ae486d8-8299-4425-b51d-cf3b9538efb2.png)



[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/aadhithya/batscript/Test%20and%20Release?logo=Github%20Actions&logoColor=%23fff&style=flat-square)](https://github.com/aadhithya/batscript/actions/workflows/release.yml)
[![GitHub issues](https://img.shields.io/github/issues/aadhithya/batscript?style=flat-square)](https://github.com/aadhithya/batscript/issues)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/aadhithya/batscript?logo=semantic%20release&style=flat-square)](https://pypi.org/project/batscript/)
![GitHub Release Date](https://img.shields.io/github/release-date/aadhithya/batscript?logo=semantic%20release&style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/batscript?logo=PyPI&logoColor=%23eaeaea&style=flat-square)
![PyPI - License](https://img.shields.io/pypi/l/batscript?style=flat-square)
![GitHub commits since latest release (by SemVer)](https://img.shields.io/github/commits-since/aadhithya/batscript/latest/master?style=flat-square)


[![Twitter Follow](https://img.shields.io/twitter/follow/asankar96?style=social)](https://twitter.com/asankar96)
[![GitHub followers](https://img.shields.io/github/followers/aadhithya?style=social)](https://github.com/aadhithya)


BatScript is a programming language based on the dialogues of Batman Triology. This is just a hobby project and is not meant to be used for serious software development.

## Installation
- batscript requires **python >= 3.8**. Install python from [here](https://www.python.org/downloads/).
- Install the batscript interpreter using the following command:
  `pip install batscript`

- test installation: `batscript version`

## Getting started

batscript is not a feature rich language and is not intended for serious use. It is rather a hobby project and a tribute to the one and only superstar.

### Run programs
`hello_world.bts`:
```
LET THE GAMES BEGIN
BAT SIGNAL "Hello World from BatScript !!!";
SOME MEN JUST WANT TO WATCH THE WORLD BURN
```
- Run the `hello_world.bts` program:

  `batscript run examples/hello_world.bts`

will result in the following output:

![hello world output](./imgs/hello-out.png)

## Acknowledgements
<!-- - A lot of learnings from [DIVSPL](https://github.com/di/divspl) and its accompanying [pycon talk](https://www.youtube.com/watch?v=ApgUrtCrmV8).
- A lot of learnings from [this pycon talk](https://www.youtube.com/watch?v=LCslqgM48D4&t=1388s) by [Alex Gaynor](alex).
- Workflows setup based on [poetry_pypi_template](https://github.com/a-parida12/poetry_pypi_template). -->
- This project is inspired by the [Rajini++](https://github.com/aadhithya/batscript) project.

## Roadmap
### batscript Features
- [x] Math Ops
  - [x] SUM
  - [x] SUB
  - [x] MUL
  - [x] DIV
  - [x] MOD
- [x] Unary Ops
- [x] print multiple objects with the same statement.
- [x] variable declaration
- [x] variable access
- [x] variable manipulation
- [x] bool data type
- [x] float datatype
- [x] logical ops
- [x] if statement
- [x] if-else statement
- [x] for loop
- [x] while loop
- [x] functions
- [x] functions with return
- [ ] functions with arguments
- [ ] Execute python code in batscript scripts
### batscript package
- [ ] batscript python runner:
  - [ ] `batscript.api.require`: load batscript code into python program.
  - [x] `batscript.runner.BatScriptRunner.exec`: execute batscript programs in python loaded as string.
  - [ ] `batscript.runner.BatScriptRunner.eval`:
    - [x] eval batscript statement in python scripts [limited support].
    - [ ] support flow control statements.
    - [ ] eval function calls from loaded batscript code and return output.
- [ ] batscript shell to run batscript commands from the terminal.
  - [x] limited support using `batscript.runner.BatScriptRunner.eval`.
  - [ ] complete support to all batscript features.

<!-- ### General
- [x] Add tests.
- [x] semantic releases. -->
