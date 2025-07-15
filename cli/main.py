import typer
from core.integrity import baseline, check_integrity

app = typer.Typer()

@app.command()
def scan(filepath:str):
    # Hash and store the value from a file in the db 
    hash_value = baseline(filepath)
    typer.echo(f'Baseline hash saved:{filepath}:{hash_value}')

@app.command()
def check(filepath:str):
    # Checks integrity of a file if stored on 
    result = check_integrity(filepath)
    typer.echo(result)

if __name__ == "__main__":
    app()