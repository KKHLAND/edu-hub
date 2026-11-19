import re, html
def md(lines):
    out, tbl = [], []
    def flush():
        if not tbl: return
        rows = [r for r in tbl if not re.match(r'^\|\s*:?-', r)]
        h = '<table>'
        for i, r in enumerate(rows):
            cells = [c.strip() for c in r.strip('|').split('|')]
            tag = 'th' if i == 0 else 'td'
            h += '<tr>' + ''.join(f'<{tag}>{html.escape(c)}</{tag}>' for c in cells) + '</tr>'
        out.append(h + '</table>'); tbl.clear()
    for ln in lines:
        ln = ln.replace('&amp;', '&')
        if ln.startswith('|'): tbl.append(ln); continue
        flush()
        if not ln.strip(): continue
        e = html.escape(ln)
        e = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', e)
        if re.match(r'^[①②③④⑤]', ln): out.append(f'<p class="ch">{e}</p>')
        elif re.match(r'^\*+ ', ln): out.append(f'<p class="fn">{e}</p>')
        elif ln.startswith('- ') or ln.startswith('Note'): out.append(f'<p class="sm">{e}</p>')
        else: out.append(f'<p>{e}</p>')
    flush()
    return '\n'.join(out)

def script_html(s):
    out = []
    for ln in s.split('\n'):
        ln = ln.strip()
        if not ln: continue
        e = html.escape(ln)
        e = re.sub(r'^(M|W|Emily|Man|Woman):', r'<b>\1:</b>', e)
        out.append(f'<p class="sc">{e}</p>')
    return '\n'.join(out)

def ko_html(s):
    return '\n'.join(f'<p>{html.escape(l)}</p>' for l in s.split('\n') if l.strip())

def voc_html(v):
    return '<ul class="voc">' + ''.join(f'<li><span class="bx"></span>{html.escape(a)} - {html.escape(b)}</li>' for a, b in v) + '</ul>'

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1200px;background:#fff;font-family:'Noto Sans CJK KR','Noto Sans KR',sans-serif;color:#111}
.card{display:flex;padding:22px 20px 26px}
.L{width:66%;padding-right:26px;border-right:1.5px solid #eee}
.R{width:34%;padding-left:24px}
.num{font-size:28px;font-weight:700;margin-bottom:14px}
.stem{font-size:23px;margin-bottom:16px;line-height:1.5}
.L p{font-size:21px;line-height:1.75;text-align:justify;margin-bottom:6px}
.L p.ch{text-align:left;margin:4px 0;line-height:1.5}
.L p.fn{text-align:right;font-size:16px;margin:2px 0}
.L p.sm{font-size:16px;color:#333;text-align:center}
.L p.sc{font-size:18px;line-height:1.6;text-align:left;margin-bottom:4px}
.L .lab{display:inline-block;font-size:15px;font-weight:700;color:#1a73e8;border:1.5px solid #1a73e8;border-radius:4px;padding:1px 8px;margin:18px 0 10px}
.L hr{border:0;border-top:1.5px solid #eee;margin:16px 0}
table{border-collapse:collapse;margin:10px 0 14px;font-size:17px;width:100%}
th,td{border:1px solid #999;padding:5px 8px;text-align:center}
th{background:#f2f4f7}
.R h3{font-size:28px;font-weight:700;color:#333;margin:2px 0 14px}
.R p{font-size:14.5px;line-height:1.75;color:#333;text-align:justify;margin-bottom:4px}
.ans{font-size:25px;font-weight:700;color:#1a73e8;margin:20px 0 6px}
.R hr{border:0;border-top:1.5px solid #eee;margin:22px 0 18px}
.voc{list-style:none}
.voc li{font-size:17px;line-height:1.55;color:#333;display:flex;align-items:center}
.bx{display:inline-block;width:15px;height:15px;border:1.5px solid #777;margin-right:10px;flex:none}
.u{text-decoration:underline}
.chart{margin:8px 0 10px;padding:10px 6px 4px;border:1px solid #bbb}
.br{display:flex;align-items:center;margin:7px 0}
.bl{width:44%;font-size:15px;text-align:right;padding-right:10px;line-height:1.25}
.bt{width:56%;display:flex;align-items:center}
.bf{display:inline-block;height:20px;background:#7f8c9d}
.bv{font-size:14px;margin-left:6px}
.ax{display:flex;justify-content:space-between;margin-left:44%;font-size:12px;color:#555;border-top:1px solid #999;padding-top:3px}
"""

def card(num, left, right_ko, answers, voc):
    ans = ''.join(f'<div class="ans">{a}</div>' for a in answers)
    return f"""<div class="card"><div class="L"><div class="num">{num}</div>{left}</div>
<div class="R"><h3>해석</h3>{right_ko}{ans}<hr><h3>어휘 및 어구</h3>{voc_html(voc)}</div></div>"""

