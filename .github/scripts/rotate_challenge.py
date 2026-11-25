"""Publish the Amman day's challenge as responsive artwork and accessible source."""
from datetime import date, datetime
from html import escape
import json
from pathlib import Path
import re
import textwrap
from zoneinfo import ZoneInfo

START, END = '<!-- daily-backend:start -->', '<!-- daily-backend:end -->'
FIRST_DAY = date(2026, 11, 25)
TOKEN = re.compile(r'''("(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|\b(?:async|function|return|const|let|await|new|try|catch|finally|throw|if|else|true|false|null|undefined)\b|\b\d+\b)''')

def text(x, y, value, size, color, *, mono=False, weight=400):
    font = 'monospace' if mono else 'Arial, sans-serif'
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(value)}</text>'

def highlight(line):
    parts = TOKEN.split(line)
    for i in range(1, len(parts), 2):
        token = parts[i]
        color = '#d2f59b' if token.startswith(('"', "'")) else '#fdc99c' if token.isdigit() else '#baafff'
        parts[i] = f'<tspan fill="{color}">{escape(token)}</tspan>'
    return ''.join(value if i % 2 else escape(value) for i, value in enumerate(parts))

def chart(entry, day, mobile):
    width = 460 if mobile else 960
    margin = 20 if mobile else 28
    code_x = margin if mobile else 393
    code_w = width - code_x - margin
    questions = textwrap.wrap(entry['question'], 33 if mobile else 24)
    code_y = (103 + 26 * len(questions)) if mobile else 26
    header = 'DAILY BACK-END CHALLENGE'
    lines = []
    for line_number, raw in enumerate(entry['code'].splitlines(),1):
        wraps = textwrap.wrap(raw,40 if mobile else 51,replace_whitespace=False,drop_whitespace=False) or ['']
        for index,wrapped in enumerate(wraps):
            lines.append((str(line_number) if index == 0 else '',wrapped))
    code_height = 55 + len(lines)*21
    height = max(code_y + code_height + 24, 156 + len(questions)*27)
    body = [text(margin,37,header,14,'#ccfa85',mono=True),
            text(margin,68,f"{day:%d %b %Y}  /  {entry['topic']}",14,'#aebbc4',mono=True)]
    for i, line in enumerate(questions):
        body.append(text(margin,108+26*i,line,22 if mobile else 23,'#f3f0e6',weight=600))
    body.append(f'<rect x="{code_x}" y="{code_y}" width="{code_w}" height="{code_height}" rx="5" fill="#121921" stroke="#40505a"/>')
    body.append(text(code_x+17,code_y+25,'challenge.js',14,'#c5d2da',mono=True))
    body.append(f'<path d="M{code_x} {code_y+36}h{code_w}" stroke="#34414d"/>')
    for i,(n,line) in enumerate(lines):
        y=code_y+58+i*21
        body.append(text(code_x+10,y,n,12,'#82909e',mono=True))
        body.append(f'<text x="{code_x+39}" y="{y}" xml:space="preserve" fill="#e1e6f1" font-size="15" font-family="monospace">{highlight(line)}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><title>Daily back-end challenge</title>'
            f'<rect width="{width}" height="{height}" rx="5" fill="#1d292d"/>' + ''.join(body) + '</svg>\n')

def update(root, day):
    path=root/'README.md'
    old=path.read_text()
    if old.count(START)!=1 or old.count(END)!=1:
        raise ValueError('Expected one daily challenge block.')
    before,tail=old.split(START)
    _,after=tail.split(END)
    bank=json.loads((root/'.github/backend-challenges.json').read_text())
    entry=bank[(day-FIRST_DAY).days % len(bank)]
    alt=escape(f"One-minute back-end challenge · {day:%d %b %Y} · {entry['topic']}. {entry['question']}", quote=True)
    block=f'''
<picture>
  <source media="(max-width: 600px)" srcset="assets/daily-mobile.svg">
  <img src="assets/daily.svg" width="100%" alt="{alt}">
</picture>

<details>
<summary>Read or copy the function</summary>

{entry["question"]}

```javascript
{entry["code"]}
```

</details>

<details>
<summary><strong>Reveal the answer</strong></summary>

<p>Output: <code>{escape(entry['output'])}</code></p>
<p>{escape(entry['answer'])}</p>

</details>
'''
    for mobile, filename in [(False,'daily.svg'),(True,'daily-mobile.svg')]:
        (root/'assets'/filename).write_text(chart(entry,day,mobile))
    path.write_text(before+START+'\n'+block+'\n'+END+after)

if __name__=='__main__':
    update(Path(__file__).resolve().parents[2],datetime.now(ZoneInfo('Asia/Amman')).date())
