
import sys
from pathlib import Path

import pandas as pd
from rich.console import Console
from rich.table import Table


def main():
    if len(sys.argv) != 2:
        print("Usage: python tools/table_tool.py data/servers.csv")
        return

    csv_path = Path(sys.argv[1])

    df = pd.read_csv(csv_path)

    # Filter servers with at least 8 CPU cores
    filtered = df[df["cpu_cores"] >= 8]

    table = Table(title="Servers with 8 or More CPU Cores")

    for column in filtered.columns:
        table.add_column(column)

    for _, row in filtered.iterrows():
        table.add_row(*[str(value) for value in row])

    console = Console()
    console.print(table)

    output_path = csv_path.with_name(
        f"{csv_path.stem}_filtered.xlsx"
    )

    filtered.to_excel(output_path, index=False)

    print(f"Saved Excel file: {output_path}")


if __name__ == "__main__":
    main()
