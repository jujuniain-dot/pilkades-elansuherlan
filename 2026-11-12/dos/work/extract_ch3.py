from docx import Document
from zipfile import ZipFile
from lxml import etree
p=r'C:/Users/ASUS/OneDrive/Documents/Rencana Penelitian Tesis/File Proposal Diujikan/Bimbingan setelah SK/BAB 3/Rev3_BAB III (20-7-26).docx'
d=Document(p)
print('PARAGRAPHS',len(d.paragraphs),'TABLES',len(d.tables))
for i,x in enumerate(d.paragraphs):
 t=x.text.strip()
 if t: print(f'P{i} [{x.style.name}] {t}')
for ti,t in enumerate(d.tables):
 print('TABLE',ti)
 for row in t.rows: print(' | '.join(c.text.replace(chr(10),' / ') for c in row.cells))
with ZipFile(p) as z:
 print('COMMENTS FILE', 'word/comments.xml' in z.namelist())
 if 'word/comments.xml' in z.namelist():
  root=etree.fromstring(z.read('word/comments.xml')); ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
  for c in root.xpath('//w:comment',namespaces=ns): print('COMMENT', ''.join(c.xpath('.//w:t/text()',namespaces=ns)))
