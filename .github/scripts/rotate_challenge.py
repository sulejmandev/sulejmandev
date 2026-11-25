"""Rotate only the daily challenge block; select by the calendar day in Amman."""
from datetime import date, datetime
from html import escape
import json
from pathlib import Path
from zoneinfo import ZoneInfo

START = '<!-- daily-backend:start -->'
END = '<!-- daily-backend:end -->'
FIRST_DAY = date(2026, 11, 25)

def render(readme, bank, day):
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError('Expected one daily challenge block.')
    before, tail = readme.split(START)
    _, after = tail.split(END)
    entry = bank[(day - FIRST_DAY).days % len(bank)]
    topic, question, answer = (escape(entry[k]) for k in ('topic', 'question', 'answer'))
    code = entry['code']
    expected = escape(entry['output'])
    block = f'''
<p><sub>{day:%d %b %Y} · {topic}</sub></p>

<p><strong>{question}</strong></p>

```javascript
{code}
```

<details>
<summary>Reveal the answer</summary>

<p>Output: <code>{expected}</code></p>
<p>{answer}</p>

</details>
'''
    return before + START + '\n' + block + '\n' + END + after

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[2]
    path = root / 'README.md'
    bank = json.loads((root / '.github/backend-challenges.json').read_text())
    path.write_text(render(path.read_text(), bank, datetime.now(ZoneInfo('Asia/Amman')).date()))
