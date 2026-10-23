"""Обновляет стандарты из клона https://github.com/zeegin/v8std: python -I update.py <путь к клону>."""
import pathlib
import re
import shutil
import subprocess
import sys

src = pathlib.Path(sys.argv[1])
dst = pathlib.Path(__file__).parent
std = dst / 'std'
shutil.rmtree(std, ignore_errors=True)
std.mkdir()
rows = []
for f in sorted((src / 'docs' / 'std').glob('*.md'), key=lambda p: int(re.sub(r'\D', '', p.stem) or 0)):
    text = f.read_text(encoding='utf-8')
    (std / f.name).write_text(text, encoding='utf-8', newline='\n')
    title = next((l[2:].strip() for l in text.splitlines() if l.startswith('# ')), f.stem)
    rows.append(f'- [{f.stem}](std/{f.name}) {title}')
shutil.copy(src / 'LICENSE', dst / 'LICENSE-v8std')
sha = subprocess.run(['git', '-C', str(src), 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
(dst / 'INDEX.md').write_text(f'# Стандарты разработки 1С (v8std {sha})\n\n' + '\n'.join(rows) + '\n', encoding='utf-8', newline='\n')
print(len(rows))
