"""Verify the mixed legacy/current source manifest without depending on cwd."""
import hashlib
from pathlib import Path


def verify(base):
    failures = []
    count = 0
    for line in (base / 'data/SHA256SUMS.txt').read_text().splitlines():
        if not line.strip():
            continue
        expected, name = line.split(None, 1)
        name = name.strip().lstrip('*')
        path = base / name
        if not path.is_file():
            path = base / 'data/raw' / name
        if not path.is_file():
            failures.append((name, 'missing'))
        elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            failures.append((name, 'checksum mismatch'))
        else:
            count += 1
    return count, failures


if __name__ == '__main__':
    count, failures = verify(Path(__file__).resolve().parents[1])
    print(f'{count} verified; {len(failures)} failed')
    for name, reason in failures:
        print(f'{name}: {reason}')
    raise SystemExit(bool(failures))
