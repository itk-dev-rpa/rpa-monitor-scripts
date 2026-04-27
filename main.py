import logging
import subprocess
import sys
import time
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent / "scripts"
LOG_FILE = Path(__file__).parent / "Scripts.log"
INTERVAL_SECONDS = 5

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def run_scripts():
    logging.info("Running")
    scripts = sorted(p for p in SCRIPTS_DIR.glob("*.py") if p.is_file())
    if not scripts:
        return

    for script in scripts:
        logging.info(f"Running {str(script)}")
        subprocess.run([sys.executable, str(script)], cwd=SCRIPTS_DIR)


def main():
    while True:
        run_scripts()
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
