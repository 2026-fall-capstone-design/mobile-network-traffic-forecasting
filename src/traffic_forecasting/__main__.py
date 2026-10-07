"""Run from the repository root: python -m traffic_forecasting --help."""

import argparse
from pathlib import Path

from traffic_forecasting.export import run_demo
from traffic_forecasting.export.validation import validate_export, validate_site


def main() -> None:
    parser = argparse.ArgumentParser(description="Traffic forecasting demo and data validation")
    commands = parser.add_subparsers(dest="command", required=True)
    demo = commands.add_parser("demo", help="Export CPU-only synthetic reference forecasts")
    demo.add_argument("--config", type=Path, default=Path("configs/demo.yaml"))
    demo.add_argument("--output", type=Path)
    check = commands.add_parser("check-data", help="Validate schemas and result consistency")
    check.add_argument("--directory", type=Path, default=Path("web/data"))
    check.add_argument("--schemas", type=Path, default=Path("schemas"))
    check.add_argument("--site", type=Path, help="Also check static HTML asset references")
    args = parser.parse_args()
    if args.command == "demo":
        destination = run_demo(args.config, args.output)
        print(f"Exported synthetic demo to {destination}")
    else:
        validate_export(args.directory, args.schemas)
        if args.site:
            validate_site(args.site)
        print("Data and requested site checks passed.")


if __name__ == "__main__":
    main()
