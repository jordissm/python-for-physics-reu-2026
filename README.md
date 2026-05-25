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

When instructions say "run this command", type the command into the terminal and
press Enter. Do not type the surrounding code block marks, and do not type a
leading `$` if you see one in other tutorials.

Most commands in this README should be run from inside this project folder. In
VS Code, you can open a terminal already pointed at the project by choosing
Terminal > New Terminal.

## Python Setup

Install Python 3.11 or newer, then create a virtual environment for this
project. A virtual environment is a private Python workspace for this folder. It
keeps packages for this bootcamp separate from packages used by other projects.

The exact install steps depend on your operating system.

Throughout this README, use `python3` to run Python commands.

### macOS

The simplest option is the official Python installer from python.org.

1. Download Python from `https://www.python.org/downloads/mac-osx/`.
2. Open the installer and follow the prompts.
3. Open Terminal and verify the install:

   ```bash
   python3 --version
   ```

   You should see something like `Python 3.11.9`, `Python 3.12.3`, or newer.

4. Create and activate a virtual environment inside the project folder:

   ```bash
   python3 -m venv reu2026_env
   source reu2026_env/bin/activate
   ```

5. Upgrade pip:

   ```bash
   python3 -m pip install --upgrade pip
   ```

When the virtual environment is active, your terminal prompt may start with
`(reu2026_env)`.

If you use Homebrew, you can also install Python with:

```bash
brew install python
```

### Linux

Use your distribution package manager or the official Python release.

Ubuntu / Debian:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

Fedora:

```bash
sudo dnf install python3 python3-pip
```

Then verify Python and create a virtual environment:

```bash
python3 --version
python3 -m venv reu2026_env
source reu2026_env/bin/activate
python3 -m pip install --upgrade pip
```

When the virtual environment is active, your terminal prompt may start with
`(reu2026_env)`.

### Windows, Using WSL

For this bootcamp, Windows users should use WSL, the Windows Subsystem for Linux.
WSL gives you a Linux terminal inside Windows, so your commands will match the
Linux and macOS instructions more closely.

Install Python inside WSL.

1. Open PowerShell as Administrator.
2. Install Ubuntu for WSL:

   ```powershell
   wsl --install -d Ubuntu
   ```

3. Restart your computer if Windows asks you to.
4. Open the Ubuntu app from the Start menu.
5. The first time Ubuntu opens, it may ask you to create a Linux username and
   password. This password is for WSL. It can be different from your Windows
   password.
6. In the Ubuntu terminal, update the package list and install Python tools:

   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
   ```

7. Verify Python and create a virtual environment from inside this project
   folder:

   ```bash
   python3 --version
   python3 -m venv reu2026_env
   source reu2026_env/bin/activate
   python3 -m pip install --upgrade pip
   ```

   If `python3 --version` shows a version older than Python 3.11, ask an
   instructor for help before continuing.

When the virtual environment is active, your terminal prompt may start with
`(reu2026_env)`.

For best results, keep bootcamp files inside your WSL home folder, such as
`/home/your-username/python-for-physics-reu-2026`, rather than in your Windows
Desktop or Downloads folder.

If you already downloaded this project somewhere in Windows, ask for help moving
or cloning it inside WSL before continuing.

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
6. Choose the interpreter inside the project virtual environment, usually
   `reu2026_env`.
   - macOS / Linux / Windows with WSL: `reu2026_env/bin/python3`
7. Open a terminal in VS Code and activate the virtual environment if it is not
   already active.

## Installing Libraries

Python libraries are extra packages that add useful tools. For example, a
physics or data analysis project might use libraries such as NumPy, SciPy,
Matplotlib, or pandas.

This project may include a file named `requirements.txt`. That file lists the
libraries needed for the bootcamp. Install those libraries inside the virtual
environment, not into your system Python.

1. Make sure you are in this project folder.
2. Activate the virtual environment:

   ```bash
   source reu2026_env/bin/activate
   ```

3. Check that the prompt includes `(reu2026_env)`.
4. Upgrade pip:

   ```bash
   python3 -m pip install --upgrade pip
   ```

5. Install the libraries from `requirements.txt`:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

6. Check that the libraries installed:

   ```bash
   python3 -m pip list
   ```

If `requirements.txt` changes later, run this command again while the virtual
environment is active:

```bash
python3 -m pip install -r requirements.txt
```

If your terminal says `requirements.txt` cannot be found, make sure you are in
the project folder. You can check your current folder with:

```bash
pwd
```

## Recommended Workflow

1. Open this project folder in VS Code.
2. Open a terminal in VS Code.
3. Create the virtual environment once per machine or clone:

   ```bash
   python3 -m venv reu2026_env
   ```

4. Activate it before working:

   macOS / Linux / Windows with WSL:

   ```bash
   source reu2026_env/bin/activate
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
