import sys
import os
import subprocess


def cold_boot_invert_rx():
    subprocess.call(['sh','tamu/cold_boot_invert_rx.sh'])
    return

def main():
    cold_boot_invert_rx()
    return

if __name__ == '__main__':
    main()
