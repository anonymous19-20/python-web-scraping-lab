from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_TEXT = PROJECT_ROOT / "data" / "sample_text.txt"


def main():
    """Read the sample text file line by line."""
    lines = SAMPLE_TEXT.read_text(encoding="utf-8").splitlines()

    for line_number, line in enumerate(lines, 1):
        print(f"{line_number}: {line}")


if __name__ == "__main__":
    main()
