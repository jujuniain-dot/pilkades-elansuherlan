from docx import Document
p=r'C:/Users/ASUS/OneDrive/Documents/Rencana Penelitian Tesis/File Proposal Diujikan/Bimbingan setelah SK/BAB 4/REV_BAB IV Jujun (20-7-26).docx'
d=Document(p)
for i,x in enumerate(d.paragraphs):
 if x.style.name.startswith('Heading') or (x.text.strip() and len(x.text.strip())<150 and i>80):
  print(i, x.style.name, x.text.strip())
