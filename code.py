import sys
import time
from rich import print as rprint

def delay_print(text, color="white"):
    for char in text:
        rprint(f"[{color}]{char}[/{color}]", end='')
        sys.stdout.flush()
        time.sleep(0.1)
    rprint()

def delay_input(prompt, color="white"):
    for char in prompt:
        rprint(f"[{color}]{char}[/{color}]", end='')
        sys.stdout.flush()
        time.sleep(0.1)
    user_input = input()
    return user_input

def fast_print(text, color="white"):
    for char in text:
        rprint(f"[{color}]{char}[/{color}]", end='')
        sys.stdout.flush()
        time.sleep(0.01)
    rprint()
