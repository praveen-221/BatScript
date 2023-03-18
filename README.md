# BatScript

BatScript is a programming language based on the dialogues of Batman Triology. This is just a hobby project and is not meant to be used for serious software development.

## Installation
- batscript requires **python >= 3.8**. Install python from [here](https://www.python.org/downloads/).
- Install poetry and then install the dependencies as folows:
```
pip install poetry
poetry install
```
<!-- - Install the batscript interpreter using the following command:
  `pip install batscript`- test installation: `batscript version` -->

## Getting started

BatScript is not a feature rich language and is not intended for serious use. It is rather a hobby project.

### Run programs
`hello_world.bts`:
```
LET THE GAMES BEGIN
BAT SIGNAL "Hello World from BatScript !!!";
SOME MEN JUST WANT TO WATCH THE WORLD BURN
```
- Run the `hello_world.bts` program:

  `python -m batscript run examples/hello_world.bts`

<!--will result in the following output:

![hello world output](./imgs/hello-out.png) -->

## Acknowledgements
- This project is inspired by the [ArnoldC](https://github.com/lhartikk/ArnoldC) project and [Rajini++](https://github.com/aadhithya/rajiniPP.git) project.

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
