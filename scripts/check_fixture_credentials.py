"""Fail if external service credentials are restored to tracked env fixtures."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
KEYS = {"GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "PADDLE_VENDOR_AUTH_CODE"}
violations = []
for path in sorted((ROOT / "config").glob(".env.*")):
    for number, line in enumerate(path.read_text().splitlines(), 1):
        key, separator, value = line.partition("=")
        if separator and key.strip() in KEYS and value.strip():
            violations.append(f"{path.relative_to(ROOT)}:{number}: {key.strip()} must be empty")
if violations:
    print("\n".join(violations), file=sys.stderr)
    sys.exit(1)
print("External service credential fixtures are empty.")
