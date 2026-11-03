from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def confirmation(path: Path):
    typer.echo(f"installing {path}")


def main():
    app()
