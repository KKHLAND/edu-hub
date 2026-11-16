import re
t = open('listen.txt').read()
lines = t.split('\n')
starts = [(i, int(m.group(1))) for i, l in enumerate(lines) if (m := re.match(r'^(\d{1,2})\. ', l)) and int(m.group(1)) <= 15]
i16 = next(i for i, l in enumerate(lines) if l.startswith('[16'))
i16q = next(i for i, l in enumerate(lines) if l.startswith('16. '))
def clean(block):
    out = []
    for l in block:
        s = l.rstrip()
        if not s.strip() or '듣기평가' in s or re.match(r'^\s*\d+\s+17\s*$', s) or '고르시오' in s or s.strip().startswith('것을') or s.strip().startswith('시오'): continue
        if l.startswith('   ') and out and not re.match(r'^\s*\[', l): out[-1] += ' ' + s.strip()
        else: out.append(s.strip())
    return '\n'.join(out)
SC = {}
for k, (i, n) in enumerate(starts):
    end = starts[k+1][0] if k+1 < len(starts) else i16
    SC[n] = clean(lines[i+1:end])
SC[16] = clean(lines[i16+1:i16q])
if __name__ == '__main__':
    for n in (1, 10, 15, 16): print(n, '>>', SC[n][:600], '\n')
