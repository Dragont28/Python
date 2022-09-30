import subprocess, sys

if __name__=='__main__':
    subprocess.call(f"ping {sys.argv[1]}")