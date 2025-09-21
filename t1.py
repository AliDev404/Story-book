import sys
import time
import os

def slow_print(text, delay=0.1, clear_before=False):
    if clear_before:
        # Cross-platform clear command
        os.system('cls' if os.name == 'nt' else 'clear')
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # move to next line

# Example usage
slow_print("abc", delay=0.2)
time.sleep(1)
slow_print("xyz", delay=0.2, clear_before=True)
