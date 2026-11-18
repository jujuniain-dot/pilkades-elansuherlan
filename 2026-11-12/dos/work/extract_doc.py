from docx import Document
p=r'C:/Users/ASUS/OneDrive/Documents/Rencana Penelitian Tesis/File Proposal Diujikan/Bimbingan setelah SK/BAB 4/REV_BAB IV Jujun (20-7-26).docx'
d=Document(p)
print('PARAGRAPHS',len(d.paragraphs),'TABLES',len(d.tables))
for i,x in enumerate(d.paragraphs):
 t=x.text.strip()
 if t: print(f'P{i}: {t}')
for ti,tab in enumerate(d.tables):
 print(f'---TABLE {ti}---')
 for row in tab.rows: print(' | '.join(c.text.replace(chr(10),' / ') for c in row.cells))
