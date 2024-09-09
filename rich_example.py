# Kom ihåg att installera rich i terminalen först: pip install rich

from rich.console import Console
from rich.text import Text

# Skapa en konsol
console = Console()

# Enkel färgad text
console.print("[red]Detta är röd text[/red]")
console.print("[green]Detta är grön text[/green]")

# Kombinera olika färger och stilar
console.print("[blue bold underline]Blå text med fetstil och understruken[/blue bold underline]")

# Text med gradient och en annan bakgrundsfärg
console.print("[on yellow]Text med gul bakgrund[/on yellow]")
console.print("[cyan on red]Cyan text med röd bakgrund[/cyan on red]")

# Skapa ett Text-objekt för mer kontroll
text = Text("En text med gradient", style="bold italic")
text.stylize("color(255) on color(0)")
console.print(text)


# --------------- Advanced -----------------------------
from rich.progress import track
import time

console = Console()

for step in track(range(10), description="Processing..."):
    time.sleep(0.5)


# --------------- Advanced -----------------------------
from rich.table import Table

# Skapa en tabell
table = Table(title="Exempel Tabell")

# Lägg till kolumner
table.add_column("Namn", justify="right", style="cyan", no_wrap=True)
table.add_column("Ålder", style="magenta")
table.add_column("Land", justify="right", style="green")

# Lägg till rader
table.add_row("Anna", "23", "Sverige")
table.add_row("Björn", "45", "Norge")
table.add_row("Cecilia", "34", "Danmark")

# Skriv ut tabellen
console.print(table)
# --------------- Advanced -----------------------------

console.print("[#ff0000]Röd text[/#ff0000] [#00ff00]Grön text[/#00ff00] [#0000ff]Blå text[/#0000ff]")

