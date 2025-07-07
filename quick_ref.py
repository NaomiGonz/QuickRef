import sys
import code
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

console = Console()

def display_logo(color="cyan"):
    art = r"""
 ██████╗ ██╗   ██╗██╗ ██████╗██╗  ██╗    ██████╗ ███████╗███████╗
██╔═══██╗██║   ██║██║██╔════╝██║ ██╔╝    ██╔══██╗██╔════╝██╔════╝
██║   ██║██║   ██║██║██║     █████╔╝     ██████╔╝█████╗  █████╗  
██║▄▄ ██║██║   ██║██║██║     ██╔═██╗     ██╔══██╗██╔══╝  ██╔══╝  
╚██████╔╝╚██████╔╝██║╚██████╗██║  ██╗    ██║  ██║███████╗██║     
 ╚══▀▀═╝  ╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝     
"""
    logo = Align.center(Text(art, style=color, justify="center"), vertical="middle")
    print(logo)

def ref_git():
	print("""
[bold underline]Git Quick Reference[/bold underline]

• [cyan]Restore back to what is currently on git website:[/cyan]
  [green]git reset --hard origin/master[/green]

• [cyan]View local git settings:[/cyan]
  [green]git config --list --local[/green]

• [cyan]View global git settings:[/cyan]
  git config --list --global
  
""")