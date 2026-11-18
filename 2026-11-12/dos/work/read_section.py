from docx import Document
p=r'C:/Users/ASUS/Documents/Codex/2026-11-12/dos/outputs/REV_BAB_IV_Jujun_dengan_bukti_periode_implementasi.docx'
d=Document(p)
for i,x in enumerate(d.paragraphs):
 if 145<=i<=270:
  t=x.text.strip()
  if t: print(f'P{i} [{x.style.name}]: {t}')
