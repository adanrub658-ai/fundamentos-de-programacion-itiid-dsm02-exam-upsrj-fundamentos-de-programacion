#!/usr/bin/env python3
import subprocess
import os
import sys
import re

# ANSI escape codes for colors
GREEN = "\033[92m"
RED   = "\033[91m"
BLUE  = "\033[34m"
RESET = "\033[0m"

# Paths
SRC_DIR = "src"
FILENAME = "main"
BIN_PATH = os.path.join("build", "bin", FILENAME)
OBJ_PATH = os.path.join("build", "obj", f"{FILENAME}.obj")
LOG_PATH = os.path.join("build", "log", f"{FILENAME}.log")

def run_cmd(cmd, cwd=None, input_data=None):
    """Run a shell command and return (exit_code, stdout, stderr)."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            shell=True,
            input=input_data,
            capture_output=True,
            text=True
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def test_make():
    print(">>> Testing compilation with make clean all run-save...")
    code, out, err = run_cmd("make clean all", cwd=SRC_DIR)
    if err:
        print("stderr:", err)
    assert code == 0, f"{RED}Compilation or run-save failed{RESET}"
    print(f"{GREEN}Compilation OK{RESET}")

def test_binary_exists():
    print(">>> Checking if binary exists...")
    assert os.path.isfile(BIN_PATH), f"{RED}Binary not found at {BIN_PATH}{RESET}"
    print(f"{GREEN}Binary found: {BIN_PATH}{RESET}")

def test_log_exists_and_content():
    print(">>> Checking if log file exists and has content...")
    assert os.path.isfile(LOG_PATH), f"{RED}Log file not found at {LOG_PATH}{RESET}"
    with open(LOG_PATH, "r") as f:
        content = f.read().strip()
    assert content, f"{RED}Log file is empty{RESET}"
    print(f"{GREEN}Log file OK{RESET}")
    print(f"{BLUE}Log content:\n{content}{RESET}")

def test_code_functionality(username: str, passwords: list, iteration: int, expected: str):
    """Black-box test: simulate interactive input (username + password attempts)."""
    print(f">>> Testing program functionality — case {iteration}")

    # Construimos la entrada: username + cada password en líneas separadas
    input_data = username + "\n" + "\n".join(passwords) + "\n"

    code, out, err = run_cmd(BIN_PATH, input_data=input_data)

    if err:
        print("stderr:", err)

    assert code == 0, f"{RED}Program execution failed{RESET}"
    assert expected in out, (
        f"{RED}Unexpected output (case {iteration}):\n"
        f"Expected to find:\n{expected}\n"
        f"Got:\n{out}{RESET}"
    )

    print(f"{GREEN}Case {iteration} OK{RESET}")

if __name__ == "__main__":
    try:
        testcases = [
            {
                "username": "adminUser",
                "passwords": ["admin123"],
                "expected": "Access granted."
            },
            {
                "username": "shrt",
                "passwords": ["admin123"],
                "expected": "Invalid username"  # El programa pedirá de nuevo
            },
            {
                "username": "validName",
                "passwords": ["wrongpass", "wrong2", "wrong3"],
                "expected": "Account locked."
            },
            {
                "username": "validName",
                "passwords": ["passNoDigit", "admin123"],
                "expected": "Password must contain at least one number."
            }
        ]

        test_make()
        test_binary_exists()
        for i, case in enumerate(testcases):
            test_code_functionality(case["username"], case["passwords"], i, case["expected"])
        print(f"\n{GREEN}All tests passed{RESET}")
    except AssertionError as e:
        print(f"{RED}Test failed: {e}{RESET}")
        sys.exit(1)
