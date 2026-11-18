from docx import Document
from zipfile import ZipFile
from lxml import etree
p=r'C:/Users/ASUS/OneDrive/Documents/Rencana Penelitian Tesis/File Proposal Diujikan/Bimbingan setelah SK/BAB 4/REV_BAB IV Jujun (20-7-26).docx'
d=Document(p)
for i,x in enumerate(d.paragraphs):
 t=x.text.strip()
 if 65 <= i <= 170 or any(k in t.lower() for k in ['periode','tahun ajaran','selama','sejak','tanggal wawancara','observasi dilaksanakan','targhib wa tarhib']):
  if t: print(f'P{i}: {t}')
with ZipFile(p) as z:
 print('COMMENTS FILE', 'word/comments.xml' in z.namelist())
 if 'word/comments.xml' in z.namelist():
  root=etree.fromstring(z.read('word/comments.xml'))
  ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
  for c in root.xpath('//w:comment',namespaces=ns): print('COMMENT',c.get('{%s}id'%ns['w']), ''.join(c.xpath('.//w:t/text()',namespaces=ns)))
