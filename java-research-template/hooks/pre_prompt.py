import subprocess


def check_java_installed():
    try:
        subprocess.run(["java", "--version"], capture_output=True, check=True)
    except Exception:
        print("Warning: Java is not installed.")


def check_git_installed():
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
    except Exception:
        print("Warning: Git is not installed.")


check_java_installed()
check_git_installed()
