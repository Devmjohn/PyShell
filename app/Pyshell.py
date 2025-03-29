import os
import sys
from os import chdir, getcwd
from os.path import expanduser

# Define shell built-in commands
builtin_cmds = ["echo", "exit", "type", "pwd", "cd", "clear", "about"]

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
                # Print the current working directory
                print(getcwd())
            elif cmd == "cd":
                if not args:
                    # Default to the user's home directory if no argument is provided
                    directory = expanduser("~")
                else:
                    directory = args[0]
                try:
                    # Change directory and handle errors
                    chdir(expanduser(directory))
                except OSError:
                    print(f"cd: {directory}: No such file or directory")
            elif cmd == "clear":
                os.system("cls" if os.name == "nt" else "clear")
            elif cmd == "about":
                os.system("cls" if os.name == "nt" else "clear")
                print("""
\033[31m██████╗░██╗░░░██╗░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░\033[0m
\033[31m██╔══██╗╚██╗░██╔╝██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░\033[0m
\033[33m██████╔╝░╚████╔╝░╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░\033[0m
\033[32m██╔═══╝░░░╚██╔╝░░░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░\033[0m
\033[32m██║░░░░░░░░██║░░░██████╔╝██║░░██║███████╗███████╗███████╗\033[0m
\033[32m╚═╝░░░░░░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝\033[0m

Created by \033[33mDev M John\033[0m
LinkedIn: \033[33mlinkedin.com/in/devmjohn\033[0m
GitHub: \033[33mgithub.com/devmjohn\033[0m
""")
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
                # If the command is not found, print the appropriate error
                print(f"{cmd}: command not found")
            else:
                # Execute valid commands
                os.system(user_input)
        except KeyboardInterrupt:
            print("\nExiting shell. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
