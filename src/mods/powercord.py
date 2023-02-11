from os import path
import shutil

from src.console import console, Markdown
import subprocess
from src.data import data_path

replugged_data_path = path.join(data_path, "replugged")


def check_repository_downloaded() -> bool:
    return path.exists(
        replugged_data_path
    )


def download_repository():
    subprocess.run("git clone https://github.com/replugged-org/replugged", cwd=data_path)


def setup():
    subprocess.run("pnpm i", cwd=replugged_data_path, shell=True)
    subprocess.run("pnpm run bundle", cwd=replugged_data_path, shell=True)


def branch_request():
    console.input("[bold red]Please close discord[/bold red] and then press enter to continue.")
    console.print(Markdown("Please enter your discord branch (`stable`/`ptb`/`canary`/`development`). Leave "
                           "blank for canary"))
    return console.input("> ")


def install():
    subprocess.run(f"pnpm run plug {branch_request()}", cwd=replugged_data_path, shell=True)
    console.input("You can now open discord again.")


def update():
    subprocess.run("git pull", cwd=replugged_data_path)
    setup()
    subprocess.run(f"pnpm run replug {branch_request()}", cwd=replugged_data_path, shell=True)
    console.input("You can now open discord again.")


def remove():
    subprocess.run(f"pnpm run unplug {branch_request()}", cwd=replugged_data_path, shell=True)
    console.input("You can now open discord again.")


# noinspection PyShadowingNames
def delete():
    console.print("[bold red]This will remove ALL data (including plugins and themes)")
    confirm = console.input("If you are absolutely sure you want to do this, type out 'Yes'\n")
    if confirm == "Yes":
        remove()
        shutil.rmtree(replugged_data_path, ignore_errors=True)
        console.input("Done, replugged is now removed. There may be some residual files leftover, though.")


if not check_repository_downloaded():
    console.print(
        Markdown(
            "You don't seem to have downloaded Replugged! Do you want to download it?\n*Requires git to be installed*"
        )
    )
    confirm = console.input("\\[y/n] ")

    if confirm == "n":
        exit(0)
    else:
        download_repository()

    console.print(
        Markdown(
            "Would you like to perform first time setup and install?\n*Requires NodeJS and `pnpm` to be installed*"
        )
    )
    confirm = console.input("\\[y/n] ")
    if confirm == "y":
        setup()
        install()

console.print(
    Markdown(
        """# Replugged

Please select the action you want to take:

- `(1)` Re-run first time setup
- `(2)` Install
- `(3)` Update
- `(4)` Remove from discord
- `(5)` Delete all data"""
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
        setup()
        install()
    case 2:
        install()
    case 3:
        update()
    case 4:
        remove()
    case 5:
        delete()
