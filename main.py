#!/usr/bin/env python3
import subprocess, time
file_path = 'menus/main.py'

def main():
    child = subprocess.Popen(['python3', file_path])
    while child.poll() is None:
        print("parent: child (pid = %d) is still running" % child.pid)
        # do parent stuff
        time.sleep(1)
    print("parent: child has terminated, returncode = %d" % child.returncode)

if __name__ == '__main__':
    main()