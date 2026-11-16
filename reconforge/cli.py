import typer

app = typer.Typer(help="ReconForge - scope-aware recon framework", no_args_is_help=True)


@app.callback()
def main():
    """ReconForge - scope-aware recon framework."""


@app.command()
def version():
    """Show version."""
    typer.echo("reconforge 0.1.0")


if __name__ == "__main__":
    app()
