from docx import Document
from pathlib import Path
p=Path(r'C:/Users/ASUS/Documents/Codex/2026-11-12/dos/outputs/REV_BAB_IV_Jujun_dengan_bukti_periode_implementasi.docx')
d=Document(p)
print('paragraphs',len(d.paragraphs),'tables',len(d.tables),'bytes',p.stat().st_size)
for q in ['Gambaran Implementasi Metode Targhib di Dalam Kelas','Gambaran Implementasi Metode Tarhib di Dalam Kelas','Uraian ini merupakan sintesis analitis','Apabila guru menjumpai perilaku']:
 print(q, any(q in x.text for x in d.paragraphs))
for i,x in enumerate(d.paragraphs):
 if x.text.strip().startswith('Gambaran Implementasi Metode'):
  print('insert at',i,x.text)
