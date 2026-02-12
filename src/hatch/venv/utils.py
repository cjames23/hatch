from base64 import urlsafe_b64encode
from os import urandom


def get_random_venv_name():
    # Will be length 4
    return urlsafe_b64encode(urandom(3)).decode("ascii")


def write_venv_file(project_root, venv_path):
    """Write .venv file pointing to active virtual environment."""
    if project_root.is_file() or not (project_root / "pyproject.toml").exists():
        return
    venv_file = project_root / ".venv"

    # Skip if .venv is already a directory (existing venv)
    if venv_file.is_dir():
        return

    venv_file.write_text(str(venv_path.resolve()))
