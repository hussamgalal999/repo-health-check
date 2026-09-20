import argparse
import json
from pathlib import Path

from .checks import run_checks


def main() -> int:
    parser = argparse.ArgumentParser(description="Check open-source repository readiness.")
    parser.add_argument("path", nargs="?", default=".", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    results = run_checks(args.path.resolve())
    if args.as_json:
        print(json.dumps([result.as_dict() for result in results], indent=2))
    else:
        for result in results:
            status = "PASS" if result.present else "TODO"
            print(f"[{status}] {result.name}: {result.path}")
            if not result.present:
                print(f"       {result.recommendation}")
    return 0 if all(result.present for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
