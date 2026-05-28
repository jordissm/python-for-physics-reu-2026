# Python for Physics REU 2026

This repository contains setup notes and bootcamp materials for the Python for
Physics REU program hosted by the Department of Physics at the University of
Illinois Urbana-Champaign. The instructions below are written for students who
may be new to Python, programming, or command-line tools.

If something does not work on the first try, that is normal. Setup is often the
most confusing part of learning to program because every computer is a little
different.

## Before You Start

You will need:

- A recent version of Python. Use Python 3.11 or newer.
- A code editor. We recommend Visual Studio Code, usually called VS Code.
- A terminal. On macOS and Linux this is called Terminal. On Windows, use WSL,
  which is described below.
- This project folder open on your computer.

## Python Setup

Install Python 3.11 or newer, then create a virtual environment for this
project. A virtual environment is a private Python workspace for this folder. It
keeps packages for this bootcamp separate from packages used by other projects.

The exact install steps depend on your operating system.

Throughout this README, use `python3` to run Python commands.

## VS Code Setup

1. Install [Visual Studio Code](https://code.visualstudio.com/).
2. Install the following extensions:
   - Python
   - Pylance
   - WSL, if you are using Windows
3. Open this folder in VS Code.
   - macOS / Linux: open the folder normally.
   - Windows with WSL: open the Ubuntu terminal, move into the project folder,
     and run:

     ```bash
     code .
     ```

     VS Code should open in WSL mode. Look for `WSL: Ubuntu` in the lower-left
     corner of the VS Code window.
4. Open the Command Palette:
   - macOS: Cmd+Shift+P
   - Windows / Linux: Ctrl+Shift+P
5. Select `Python: Select Interpreter`.
6. Create and activate a virtual environment.

## Installing Libraries

Python libraries are extra packages that add useful tools. For example, a
physics or data analysis project might use libraries such as NumPy, SciPy,
Matplotlib, or pandas.

This project includes a file named `requirements.txt`. That file lists the
libraries needed for the bootcamp. Install those libraries inside the virtual
environment, not into your system Python.

## Recommended Workflow

1. Open this project folder in VS Code.
2. Open a terminal in VS Code.
3. Create the virtual environment once per machine or clone:

   ```bash
   python3 -m venv .venv
   ```

4. Activate it before working:

   macOS / Linux / Windows with WSL:

   ```bash
   source .venv/bin/activate
   ```

5. Install the project libraries from `requirements.txt`:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

6. Run scripts from the activated environment so VS Code and the terminal use the
   same Python.

7. When you are done working, you can close the terminal or run:

   ```bash
   deactivate
   ```

## Quick Check

Run this to confirm Python is working:

```bash
python3 --version
python3 -c "print('Python is ready')"
```
