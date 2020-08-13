from bs4 import BeautifulSoup

soup = BeautifulSoup(open("leetcode_html.txt").read(), "html.parser" )

def row_to_strings(row):
    items = [cell.find(text=True) for cell in row.findAll("td")]
    hrefs = [a['href'] for a in row.find_all('a', href=True) if a]
    return [items[i] for i in [1,2,5]]  + [hrefs[0][1:]] if len(items)>5 else []

rows = soup.find('table').find_all('tr')
data = [row_to_strings(row) for row in rows[1:-2]]

out = []
for num, name, diff, loc in data:
    href = '['+name+'](https://leetcode.com/'+loc+'/)'
    fname =loc+'.py'
    out.append('|'+'|'.join([num,href,fname,diff])+'|')

outfilename = 'mdlist.txt'

with open(outfilename, 'w') as f:
    for item in out:
        f.write("%s\n" % item)
