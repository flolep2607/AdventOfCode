"""
Abstract base class for Advent of Code solutions.

Usage:
    from utils.base import AOCSolution

    class Day01(AOCSolution):
        def part1(self) -> None:
            # self.input contains the raw input string
            # self.lines contains the input split by lines
            print("Part 1 answer")

        def part2(self) -> None:
            print("Part 2 answer")

    if __name__ == "__main__":
        Day01().run()
"""

from abc import ABC, abstractmethod
import inspect
from pathlib import Path
from typing import Optional


class AOCSolution(ABC):
    """Abstract base class for Advent of Code daily solutions."""

    def __init__(self, input_file: Optional[str] = None):
        """
        Initialize the solution and read the input file if it exists.

        Args:
            input_file: Path to the input file (default: "input.txt")
        """
        if not input_file:
            input_file = Path(inspect.getfile(self.__class__)).parent / "input.txt"
        self.input_file = input_file
        self.input: Optional[str] = None
        self.lines: list[str] = []

        self._load_input()

    def _load_input(self) -> None:
        """Load the input file if it exists."""
        input_path = Path(self.input_file)
        if input_path.exists():
            self.input = input_path.read_text().strip()
            self.lines = self.input.split("\n")
        else:
            print(f"Warning: Input file '{self.input_file}' not found.")

    @abstractmethod
    def part1(self) -> None:
        """Solve part 1 of the puzzle. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def part2(self) -> None:
        """Solve part 2 of the puzzle. Must be implemented by subclasses."""
        pass

    def run(self, parts: Optional[list[int]] = None) -> None:
        """
        Run the solution for the specified parts.

        Args:
            parts: List of parts to run (default: [1, 2])
        """
        if parts is None:
            parts = [1, 2]

        if 1 in parts:
            print("--- Part 1 ---")
            self.part1()

        if 2 in parts:
            print("--- Part 2 ---")
            self.part2()
