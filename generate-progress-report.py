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
    coverage: int  # Nouveau champ pour la couverture

def get_chapter_progress() -> list[ProgressData]:
    chapters: list[str] = [d.name for d in Path('exercises').iterdir() if d.is_dir() and not d.name.startswith('__')]
    progress_data: list[ProgressData] = []

    for chapter in chapters:
        result = subprocess.run(
            ['pytest', f'exercises/{chapter}', '-q', f'--cov=exercises/{chapter}', '--cov-report=term'],
            capture_output=True,
            text=True
        )
        output = result.stdout
        failed = int(output.split(" failed")[0].split()[-1]) if " failed" in output else 0
        passed = int(output.split(" passed")[0].split()[-1]) if " passed" in output else 0
        total = passed + failed
        percent = int((passed / total) * 100) if total > 0 else 0

        # Extraire le pourcentage de couverture
        coverage_line = next((line for line in output.splitlines() if "TOTAL" in line), None)
        coverage = int(coverage_line.split()[-1].replace('%', '')) if coverage_line else 0

        progress_data.append(ProgressData(chapter, total, passed, percent, coverage))

    return progress_data


def generate_ascii_progress(progress_data: list[ProgressData]):
    with open('README.md', 'r') as f:
        content = f.readlines()

    start_index = next(i for i, line in enumerate(content) if '<!-- START_PROGRESS -->' in line) + 1
    end_index = next(i for i, line in enumerate(content) if '<!-- END_PROGRESS -->' in line)

    progress_lines = []
    for data in progress_data:
        bar_length = 20
        filled = int(data.percent / (100 / bar_length))
        bar = '[' + '=' * filled + '>' + ' ' * (bar_length - filled - 1) + ']'
        progress_lines.append(
            f"- {data.chapter} {bar} {data.percent}% ({data.passed}/{data.total}) - Coverage: {data.coverage}%\n"
        )

    content[start_index:end_index] = progress_lines

    with open('README.md', 'w') as f:
        f.writelines(content)
        

if __name__ == '__main__':
    progress_data = get_chapter_progress()
    generate_ascii_progress(progress_data)
    print("Progression générée dans progress.md et progress.png")