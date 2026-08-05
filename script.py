import os
import re

dir_path = 'C:/Users/ishan/Documents/Projects/Awesome-Zero-Token-Architecture'
readme_path = os.path.join(dir_path, 'README.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Generate SVG Banner
svg_content = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="800" height="200" fill="url(#grad1)" />
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Arial" font-size="40" fill="white">
    Awesome Zero Token Architecture
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" />
  </text>
</svg>'''

os.makedirs(os.path.join(dir_path, 'assets'), exist_ok=True)
with open(os.path.join(dir_path, 'assets/banner.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_content)

# Badges
badges = '''<div align="center">
<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
<img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status" />
<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</div>

![Banner](assets/banner.svg)
'''

# Star History
star_history = '''
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-Zero-Token-Architecture&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Zero-Token-Architecture&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Zero-Token-Architecture&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Zero-Token-Architecture&type=date&legend=bottom-right" />
</picture>
</a>
</div>
'''

def replace_bullets(text):
    sections = re.split(r'\n---', text)
    new_sections = []
    
    for sec in sections:
        if '*' in sec:
            lines = sec.split('\n')
            table_lines = ['| Year | Paper | Topic | Description |', '|---|---|---|---|']
            i = 0
            while i < len(lines):
                line = lines[i]
                if line.strip().startswith('*   **') or line.strip().startswith('*   1.') or line.strip().startswith('*   2.') or line.strip().startswith('*   3.'):
                    title_match = re.search(r'\*\s+(?:\d\.\s+)?\*\*?(.*?)\*\*?', line.strip())
                    title = title_match.group(1) if title_match else line.strip().strip('* ')
                    desc = ""
                    i += 1
                    while i < len(lines) and lines[i].strip().startswith('*   *'):
                        desc += lines[i].strip().strip('* ') + " "
                        i += 1
                    
                    filename = re.sub(r'[^a-zA-Z0-9]', '-', title.lower()) + '.md'
                    title_linked = f'[{title}]({filename})'
                    table_lines.append(f'| 2026 | [Paper Link](#) | {title_linked} | {desc} |')
                    
                    with open(os.path.join(dir_path, filename), 'w', encoding='utf-8') as df:
                        df.write(f'# {title}\n\n```mermaid\ngraph TD;\nA-->B;\n```\n\nDetailed info on {title}.\n\n[Back to README](README.md)\n')
                    continue
                else:
                    table_lines.append(line)
                i += 1
            new_sections.append('\n'.join(table_lines))
        else:
            new_sections.append(sec)
    
    return '\n---'.join(new_sections)

content = badges + '\n' + content
content = content.replace('chartrepos', 'chart?repos')
content = content.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')
content = replace_bullets(content)
content = content + star_history

# Replace Emojis
content = content.replace('## 1. ', '## 📅 1. ')
content = content.replace('## 2. ', '## 💡 2. ')
content = content.replace('## 3. ', '## 🛠️ 3. ')
content = content.replace('## 4. ', '## ⚠️ 4. ')
content = content.replace('## 5. ', '## 🌍 5. ')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
