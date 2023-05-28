import subprocess

DETACHED_PROCESS = 8
subprocess.Popen('cmd /c "pythonw main.py"', creationflags=DETACHED_PROCESS, close_fds=True)
