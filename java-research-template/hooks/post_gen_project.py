import os
import subprocess

REMOVE_PATHS = [
    '{% if cookiecutter.build_tool != "Gradle" %}build.gradle{% endif %}',
    '{% if cookiecutter.build_tool != "Maven" %}pom.xml{% endif %}',
]


def remove_unnecessary_files():
    for path in REMOVE_PATHS:
        path = path.strip()
        if path and os.path.exists(path):
            os.unlink(path) if os.path.isfile(path) else os.rmdir(path)


def check_build_tool_installed():
    build_tool = "{{ cookiecutter.build_tool }}"
    try:
        if build_tool == "Gradle":
            subprocess.run(["gradle", "--version"],
                           capture_output=True, check=True)
        if build_tool == "Maven":
            subprocess.run(["mvn", "--version"],
                           capture_output=True, check=True)
    except Exception:
        print(f"Warning: {build_tool} not installed.")


check_build_tool_installed()
remove_unnecessary_files()
