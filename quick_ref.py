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

• Restore back to what is currently on git website:
  [green]git reset --hard origin/master[/green]

• View/change local git settings:
  [green]git config --list --local[/green]
  [green]git config user.email "email@example.com"[/green]

• View/change global git settings:
  [green]git config --list --global[/green]
  [green]git config --global user.email "email@example.com"[/green]
""")


def ref_screen():
    print("""
[bold underline]Screen Quick Reference[/bold underline]

• Start a new screen:
  [green]screen -S name[/green]

• Detach from screen:
  [green]Ctrl-A, then D[/green]

• Reattach screen:
  [green]screen -r name[/green]

• List screens:
  [green]screen -ls[/green]

• Kill session:
  [green]screen -X -S name quit[/green]
""")

def ref_send():
    print("""
[bold underline]Send Files to/from Remote Computers Quick Reference[/bold underline]

• Format: 
  [green]rsync -<flags> <src> <dest>[/green]
  [yellow]<user>@server:<dir_path>[/yellow]

• Example:
  [green]rsync -azhvP --inplace etl@ceamtddaq01:~/lpGBTv2_3_SO1_ETL .[/green]

• Flag descriptions:
  [green]-a[/green] Archive, recursive, preserve metadata
  [green]-v[/green] Verbose
  [green]-z[/green] Compress
  [green]-h[/green] Human-Readable
  [green]-P[/green] Progress bar per file + keeps partially transferred
  [green]--inplace[/green] Write updates directly to the dest (saves space)

""")

def ref_help(hidden = True):
    print("\n[bold]Available topics:[/bold]")
    for key in reference_map:
        print(f"  • [green]{key}[/green]")
    #print("\nUse: [yellow]python3 quick_ref.py <topic>[/yellow]")


class CallableDisplay:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        self.func()

    def __repr__(self):
        self.func()
        return ""

# All possible commands
reference_map = {
    "git": CallableDisplay(ref_git),
    "screen": CallableDisplay(ref_screen),
    "help": CallableDisplay(ref_help),
    "send" : CallableDisplay(ref_send),
}

def interactive_shell():
    console.rule("[bold yellow]Quick Reference Shell[/bold yellow]", characters="=")
    ref_help()
    print("\nType [cyan]git[/cyan], [cyan]screen[/cyan], etc., to see command info.")
    print("Type [green]exit()[/green] or press [red]Ctrl-D[/red] to quit.\n")

    # Add aliases for plain commands like "git" and "screen"
    shell_vars = {k: v for k, v in reference_map.items()}
    shell_vars.update({
        "__name__": "__main__",  # for REPL context
    })
    code.interact(local=shell_vars)

def main():
    if len(sys.argv) < 2:
        display_logo()
        interactive_shell()
        return

    topic = sys.argv[1].lower()

    if topic in reference_map:
        reference_map[topic]()
    else:
        print(f"[red]Unknown topic:[/red] {topic}\n")
        ref_help()

if __name__ == "__main__":
    main()






