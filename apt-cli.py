import os
import sys
import subprocess
import argparse
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

ACTIONS = {
    "1": "Install a package",
    "2": "Install specific version of a package",
    "3": "Remove a package",
    "4": "Completely remove a package",
    "5": "Install recommended packages",
    "6": "Install without recommended dependencies",
    "7": "Upgrade installed packages",
    "8": "Update package list",
    "9": "Upgrade the entire system",
    "10": "Remove unused packages",
    "11": "Search for a package",
    "12": "Show package details",
    "13": "List installed packages",
    "14": "Check package dependencies",
    "15": "Clean package cache",
    "16": "List upgradable packages",
    "17": "Simulate install of a package"
}


def show_menu():
    table = Table(title="apt-cli: Sleek REPL APT Tool", show_lines=True)
    table.add_column("Option", style="cyan", justify="center")
    table.add_column("Action", style="magenta")
    
    for key, val in ACTIONS.items():
        table.add_row(key, val)
    
    console.print(table)
    choice = Prompt.ask("Choose an action", choices=ACTIONS.keys())
    return choice


def input_method():
    return Prompt.ask("Choose input method", choices=["CLI", "GUI", "CLI Rainbow"])


def get_input_gui():
    try:
        output = subprocess.check_output(
            ['dialog', '--inputbox', 'Enter package names/versions', '10', '50'],
            stderr=subprocess.STDOUT
        )
        return output.decode().strip()
    except Exception as e:
        print(f"[red]Error with dialog: {e}[/red]")
        return None


def get_input_cli_rainbow():
    user_input = input("Enter package name(s) and version(s) if needed: ")
    rainbow_output = subprocess.check_output(
        ['lolcat'], input=user_input, text=True, stderr=subprocess.STDOUT
    )
    print(f"[rainbow]{rainbow_output}[/rainbow]")
    return user_input


def get_package_input():
    method = input_method()
    if method == "CLI":
        return input("Enter package name(s) and version(s) if needed: ")
    elif method == "CLI Rainbow":
        return get_input_cli_rainbow()
    else:
        return get_input_gui()


def run_command(args_list):
    console.print(f"[green]Running:[/green] {' '.join(args_list)}")
    try:
        subprocess.run(args_list, check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Command failed: {e}[/red]")


def ai_mode():
    prompt = Prompt.ask("What do you want to do?").lower()
    
    patterns = {
        "what's my version of apt": ["apt", "--version"],
        "update packages": ["apt", "update"],
        "upgrade system": ["apt", "full-upgrade", "-y"],
        "remove unused": ["apt", "autoremove", "-y"],
        "list installed": ["apt", "list", "--installed"],
        "search package": lambda: ["apt", "search", get_package_input()],
        "show details": lambda: ["apt", "show", get_package_input()],
        "install package": lambda: ["apt", "install", "-y"] + get_package_input().split(),
        "check dependencies": lambda: ["apt-cache", "depends", get_package_input()],
        "clean cache": ["apt", "clean"],
        "list upgradable": ["apt", "list", "--upgradable"]
    }

    for key, cmd in patterns.items():
        if key in prompt:
            if callable(cmd):
                run_command(cmd())
            else:
                run_command(cmd)
            return

    print("[yellow]Sorry, couldn't match your AI prompt.[/yellow]")


def main():
    parser = argparse.ArgumentParser(description="apt-cli: APT in a colorful REPL")
    parser.add_argument('--ai', action='store_true', help='Use AI natural language mode')
    args = parser.parse_args()

    if args.ai:
        ai_mode()
        return

    while True:
        choice = show_menu()

        if choice in ["1", "2", "3", "4", "5", "6", "11", "12", "14", "17"]:
            pkg_input = get_package_input()
            if not pkg_input:
                print("[red]No input provided.[/red]")
                continue
            pkg_args = pkg_input.split()

            if choice == "1":
                run_command(["apt", "install", "-y"] + pkg_args)
            elif choice == "2":
                run_command(["apt", "install", "-y"] + pkg_args)
            elif choice == "3":
                run_command(["apt", "remove", "-y"] + pkg_args)
            elif choice == "4":
                run_command(["apt", "purge", "-y"] + pkg_args)
            elif choice == "5":
                run_command(["apt", "install", "--install-recommends", "-y"] + pkg_args)
            elif choice == "6":
                run_command(["apt", "install", "--no-install-recommends", "-y"] + pkg_args)
            elif choice == "11":
                run_command(["apt", "search"] + pkg_args)
            elif choice == "12":
                run_command(["apt", "show"] + pkg_args)
            elif choice == "14":
                run_command(["apt-cache", "depends"] + pkg_args)
            elif choice == "17":
                run_command(["apt", "install", "--simulate"] + pkg_args)

        elif choice == "7":
            run_command(["apt", "upgrade", "-y"])
        elif choice == "8":
            run_command(["apt", "update"])
        elif choice == "9":
            run_command(["apt", "full-upgrade", "-y"])
        elif choice == "10":
            run_command(["apt", "autoremove", "-y"])
        elif choice == "13":
            run_command(["apt", "list", "--installed"])
        elif choice == "15":
            run_command(["apt", "clean"])
        elif choice == "16":
            run_command(["apt", "list", "--upgradable"])

        again = Prompt.ask("Do you want to run another command?", choices=["yes", "no"])
        if again == "no":
            break


if __name__ == '__main__':
    main()
