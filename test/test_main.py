#!/usr/bin/env python3
import subprocess
import os
import sys
import re

GREEN = "\033[92m"
RED   = "\033[91m"
BLUE  = "\033[34m"
RESET = "\033[0m"

SRC_DIR = "src"
FILENAME = "main"
BIN_PATH = os.path.join("build", "bin", FILENAME)

def run_cmd(cmd, cwd=None, input_data=None, timeout=3):
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,         
            input=input_data,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired as e:
        # El reloj sigue corriendo, pero capturamos lo que imprimió
        stdout = e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
        stderr = e.stderr.decode() if isinstance(e.stderr, bytes) else (e.stderr or "")
        return 0, stdout, stderr

def test_make():
    print(">>> Testing compilation with make clean all...")
    code, out, err = run_cmd(["make", "clean", "all"], cwd=SRC_DIR, timeout=10)
    if err:
        print("stderr:", err)
    assert code == 0, f"{RED}Compilation failed{RESET}"
    print(f"{GREEN}Compilation OK{RESET}")

def test_binary_exists():
    print(">>> Checking if binary exists...")
    assert os.path.isfile(BIN_PATH), f"{RED}Binary not found at {BIN_PATH}{RESET}"
    print(f"{GREEN}Binary found: {BIN_PATH}{RESET}")

def test_code_functionality(initial_time: str, iteration: int, expected_pattern: str):
    print(f">>> Testing program functionality — case {iteration}")
    input_data = initial_time + "\n"

    code, out, err = run_cmd(BIN_PATH, input_data=input_data, timeout=3)

    if err:
        print("stderr:", err)

    assert code == 0, f"{RED}Program execution failed{RESET}"

    # Verificamos que la salida contiene al menos la hora inicial
    match = re.search(expected_pattern, out)
    assert match, (
        f"{RED}Unexpected output (case {iteration}):\n"
        f"Expected to match regex:\n{expected_pattern}\n"
        f"Got:\n{out}{RESET}"
    )

    print(f"{GREEN}Case {iteration} OK{RESET}")
    
    clean_out = out.replace("\r", "\n").strip()
    print(f"{BLUE}Captured output:\n{clean_out}{RESET}")


if __name__ == "__main__":
    try:
        testcases = [
            {
                "initial_time": "09:45:12", 
                "expected": r"Hora actual: 09:45:12"
            },
            {
                "initial_time": "23:59:59", 
                "expected": r"Hora actual: 23:59:59"
            },
            {
                "initial_time": "00:00:00", 
                "expected": r"Hora actual: 00:00:00"
            },
        ]

        test_make()
        test_binary_exists()
        for i, case in enumerate(testcases):
            test_code_functionality(case["initial_time"], i, case["expected"])
        print(f"\n{GREEN}All tests passed{RESET}")
    except AssertionError as e:
        print(f"{RED}Test failed: {e}{RESET}")
        sys.exit(1)