import os
import subprocess
from dataclasses import dataclass

import matplotlib.pyplot as plt
from pathlib import Path

@dataclass
class ProgressData:
    chapter: str
    total: int
    passed: int
    percent: int


def get_chapter_progress() -> list[ProgressData]:
    chapters: list[str] = [d.name for d in Path('exercises').iterdir() if d.is_dir() and d.name.startswith('chapter')]
    progress_data: list[ProgressData] = []

    for chapter in chapters:
        result = subprocess.run(
            ['pytest', f'exercises/{chapter}', '-q'],
            capture_output=True,
            text=True
        )
        output = result.stdout
        failed = int(output.split(" failed")[0].split()[-1]) if " failed" in output else 0
        passed = int(output.split(" passed")[0].split()[-1]) if " passed" in output else 0
        total = passed + failed
        percent = int((passed / total) * 100) if total > 0 else 0

        progress_data.append(ProgressData(chapter, total, passed, percent))

    return progress_data

def generate_ascii_progress(progress_data: list[ProgressData]):
    with open('progress.md', 'w') as f:
        f.write("# Progression des Tests\n\n")
        for data in progress_data:
            bar_length = 20
            filled = int(data.percent / (100 / bar_length))
            bar = '[' + '=' * filled + '>' + ' ' * (bar_length - filled - 1) + ']'
            f.write(f"- {data.chapter} {bar} {data.percent}% ({data.passed}/{data.total})\n")

if __name__ == '__main__':
    progress_data = get_chapter_progress()
    generate_ascii_progress(progress_data)
    print("Progression générée dans progress.md et progress.png")