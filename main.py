import os
import runpy
from src.console import console, Markdown


try:
    os.mkdir("data")
except FileExistsError:
    pass

console.print(
    Markdown(
        """# Welcome to the Python Discord Manager!

Please select one of the following mods to manage:

- `(1)` Replugged *(Beta)*"""
    )
)

selection = ""
while True:
    try:
        selection = console.input("[grey]> [white]")
        selection = int(selection)
    except ValueError:
        console.print(f"[error]{selection} isn't a number!")
    else:
        break

match selection:
    case 1:
        runpy.run_module("src.mods.powercord")
