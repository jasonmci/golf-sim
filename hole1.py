from typing import Tuple
from rich.console import Console
from rich.text import Text

TERRAIN_STYLES = {
    "T": ("  ", "on white"),
    "F": ("  ", "on green"),
    "R": ("  ", "on green4"),
    "B": ("  ", "on khaki3"),
    "W": ("  ", "on blue"),
    "G": ("  ", "on green3"),
    "P": ("  ", "on white"),
    "X": ("  ", "on black"),
}

def load_hole_from_file(path: str) -> list[list[str]]:
    with open(path, 'r') as f:
        lines = f.readlines()
    return [line.strip().split() for line in lines if line.strip()]


class Hole:
    def __init__(self, name: str, grid: list[list[str]], par: int, viewport_width: int = 200):
        self.name = name
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.par = par
        self.scroll_offset = 0
        self.viewport_width = viewport_width

    def display(self):
        console = Console()
        console.print(f"\n[bold underline]{self.name}[/] (Par {self.par})")
        for row in self.grid:
            line = Text()
            start = self.scroll_offset
            end = self.scroll_offset + self.viewport_width
            for cell in row[start:end]:
                char, style = TERRAIN_STYLES.get(cell, (" ", "on black"))
                line.append(char, style=style)
            console.print(line)

# Generate and render the 773-yard hole

hole = Hole("TPC Colorado - Hole 13", load_hole_from_file("courses/pine-creek-road/hole1.txt"), par=5, viewport_width=80)
hole.display()
