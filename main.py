import subprocess
import sys
import time
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent / "scripts"
INTERVAL_SECONDS = 30 * 60


def run_all():
    scripts = sorted(p for p in SCRIPTS_DIR.glob("*.py") if p.is_file())
    if not scripts:
        return

    for script in scripts:
        subprocess.run([sys.executable, str(script)], cwd=SCRIPTS_DIR)


def main():
    while True:
        run_all()
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
