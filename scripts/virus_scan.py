import os
import sys
import subprocess

def scan_file(filename):
    try:
        result = subprocess.run(
            ['clamscan', '-r', '--no-summary', filename],
            capture_output=True,
            text=True
        )
        if "Infected files: 0" not in result.stdout:
            raise ValueError("Virus detected")
    except FileNotFoundError:
        print("ClamAV not installed, skipping scan")

if __name__ == "__main__":
    scan_file(sys.argv[1])
