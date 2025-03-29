import os
import sys
from os import chdir, getcwd, listdir
from os.path import expanduser

# Define shell built-in commands
builtin_cmds = ["echo", "exit", "type", "pwd", "cd", "clear", "about", "ls"]

# Get system PATH
PATH = os.getenv("PATH", "")

def is_command(cmd):
    """
    Check if the command is a valid executable or built-in command.
    """
    if cmd in builtin_cmds:
        return True
    for path in PATH.split(":"):
        full_path = os.path.join(path, cmd)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return True
    return False

def main():
    print("""
██████╗░██╗░░░██╗░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░
██╔══██╗╚██╗░██╔╝██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░
██████╔╝░╚████╔╝░╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░
██╔═══╝░░░╚██╔╝░░░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░
██║░░░░░░░░██║░░░██████╔╝██║░░██║███████╗███████╗███████╗
╚═╝░░░░░░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝

---------------------------------
| Created By: Dev M John        |
---------------------------------
""")
    while True:
        try:
            # Display the shell prompt
            sys.stdout.write("$ ")
            sys.stdout.flush()
            user_input = input().strip()  # Read and clean user input

            # Split the command into parts
            command_parts = user_input.split()

            # Handle empty input
            if not command_parts:
                continue

            cmd, *args = command_parts

            if cmd == "exit" and args == ["0"]:
                print("Goodbye! Thanks for using PyShell.")
                sys.exit(0)
            elif cmd == "echo":
                print(" ".join(args))
            elif cmd == "pwd":
                print(getcwd())
            elif cmd == "cd":
                if not args:
                    directory = expanduser("~")
                else:
                    directory = args[0]
                try:
                    chdir(expanduser(directory))
                except OSError:
                    print(f"cd: {directory}: No such file or directory")
            elif cmd == "clear":
                os.system("cls" if os.name == "nt" else "clear")
            elif cmd == "ls":
                try:
                    print(" ".join(listdir(getcwd())))
                except OSError:
                    print("ls: error listing directory contents")
            elif cmd == "type":
                if not args:
                    print("type: missing argument")
                    continue
                target_cmd = args[0]
                if target_cmd in builtin_cmds:
                    print(f"{target_cmd} is a shell builtin")
                else:
                    found = False
                    for path in PATH.split(":"):
                        full_path = os.path.join(path, target_cmd)
                        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                            print(f"{target_cmd} is {full_path}")
                            found = True
                            break
                    if not found:
                        print(f"{target_cmd} not found")
            elif not is_command(cmd):
                print(f"{cmd}: command not found")
            else:
                os.system(user_input)
        except KeyboardInterrupt:
            print("\nExiting shell. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
