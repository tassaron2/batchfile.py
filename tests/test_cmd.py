"""
Run on Windows to compare outputs
"""
import batchfile
import subprocess


def test():
    # Get CMD.exe output
    try:
        cmd_exe = subprocess.Popen("test.bat", stdout=subprocess.PIPE, encoding="utf-8")
    except PermissionError:
        print("Couldn't run CMD. Are you on Windows?")
        return
    cmd_output, _ = cmd_exe.communicate()

    # Get Batchfile.py output
    bat = batchfile.Batchfile(stdout=[])
    bat.run(".", "test.bat")
    page = "".join(bat.stdout)

    print("CMD.exe output:")
    print(cmd_output)
    print("batchfile.py output:")
    print(page, end="")
    assert cmd_output == page


if __name__ == "__main__":
    try:
        test()
        print("\nTEST PASSED")
    except AssertionError:
        print("\nTEST FAILED")