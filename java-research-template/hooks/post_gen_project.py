import os
import subprocess

REMOVE_PATHS = [
    '{% if cookiecutter.build_tool != "Gradle" %}build.gradle{% endif %}',
    '{% if cookiecutter.build_tool != "Maven" %}pom.xml{% endif %}',
    '{% if cookiecutter.license == "None" %}LICENSE{% endif %}',
]


def remove_unnecessary_files():
    for path in REMOVE_PATHS:
        path = path.strip()
        if path and os.path.exists(path):
            os.unlink(path) if os.path.isfile(path) else os.rmdir(path)


def tool_installed_check(tool, log_level) -> bool:
    try:
        subprocess.run([tool, "--version"],
                       capture_output=True, check=True)
        return True
    except Exception:
        print(f"{log_level}: {tool} not installed.")
        return False


def check_build_tool_installed():
    if "{{ cookiecutter.build_tool }}" == "Gradle":
        tool = "gradle"
    elif "{{ cookiecutter.build_tool }}" == "Maven":
        tool = "mvn"
    tool_installed_check(tool, "Warning")


def init_git_repository():
    # working with strings in order to maintain valid python syntax
    if "{{ cookiecutter.init_git_repository }}" == "True" \
            and tool_installed_check("git", "Error"):
        subprocess.run(["git", "init"], capture_output=True, check=True)
        subprocess.run(["git", "add", "."], capture_output=True, check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"],
                       capture_output=True, check=True)


def create_remote_repository():
    if "{{ cookiecutter.git_hosting_service }}" == "GitHub" \
            and "{{ cookiecutter.init_git_repository }}" == "True" \
            and tool_installed_check("gh", "Error"):
        subprocess.run(["gh", "repo", "create",
                        "{{ cookiecutter.__project_slug }}", "--public",
                        "--source=.", "--remote=upstream"],
                       capture_output=True, check=True)
        subprocess.run(["git", "push", "--set-upstream", "upstream",
                        "main"], capture_output=True, check=True)


check_build_tool_installed()
remove_unnecessary_files()
init_git_repository()
create_remote_repository()
