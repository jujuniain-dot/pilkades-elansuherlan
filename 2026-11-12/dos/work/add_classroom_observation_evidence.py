from docx import Document
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from pathlib import Path
src=Path(r'C:/Users/ASUS/Documents/Codex/2026-11-12/dos/outputs/REV_BAB_IV_Jujun_dengan_bukti_periode_implementasi.docx')
out=Path(r'C:/Users/ASUS/Documents/Codex/2026-11-12/dos/outputs/REV_BAB_IV_Jujun_bukti_observasi_kelas.docx')
doc=Document(src)
anchor=next(p for p in doc.paragraphs if p.text.strip().startswith('Implementasi Metode Targhib melalui Pemberian Stimulasi Edukatif'))
def para(text, style='Normal'):
 return anchor.insert_paragraph_before(text, style=style)
para('Bukti Observasi Kelas dan Keterkaitan dengan RPP atau I’dad Tadris', 'List Paragraph')
para('Pada hari [hari], tanggal [tanggal sesuai catatan lapangan], pukul [waktu], peneliti melakukan observasi pembelajaran Pendidikan Agama Islam di kelas XI [kelas/rombel] MA Daarussalam Kunir. Materi yang dipelajari adalah [materi sesuai perangkat ajar]. Sebelum menguraikan kegiatan, peneliti memeriksa RPP atau i’dad tadris [nama dokumen, tanggal penyusunan, dan bagian/halaman]. Pada perangkat tersebut tercantum [tujuan pembelajaran dan langkah kegiatan yang benar-benar tertulis].')
para('Berdasarkan catatan observasi, pada kegiatan awal guru [uraikan tindakan yang benar-benar diamati]. Pada kegiatan inti, guru menyampaikan [materi] dan menerapkan targhib dengan [ayat, hadis, kisah, motivasi, atau penguatan yang benar-benar disampaikan]; peserta didik merespons dengan [respons yang tercatat]. Unsur tarhib tampak ketika [peristiwa nyata yang diamati, jika ada]: guru [nasihat/peringatan/tindakan edukatif yang benar-benar dilakukan] dan menjelaskan [alasan atau konsekuensi yang disampaikan]. Pada kegiatan penutup, guru [refleksi, tindak lanjut, atau penguatan yang benar-benar dilakukan].')
para('Ringkasan pencatatan observasi dan sumber pembuktiannya disajikan berikut. Isian dalam tanda kurung siku harus disesuaikan dengan catatan lapangan dan perangkat ajar asli; apabila salah satu unsur metode tidak muncul pada pertemuan yang diamati, tuliskan bahwa unsur tersebut tidak teramati pada pertemuan itu.')
t=doc.add_table(rows=1, cols=3)
headers=['Tahap pembelajaran','Catatan praktik kelas','Sumber bukti']
for c,v in zip(t.rows[0].cells,headers): c.text=v
rows=[
('Kegiatan awal','[Pembukaan, tujuan, apersepsi, atau pemantik yang benar-benar diamati]','[Catatan lapangan; bagian pendahuluan RPP/i’dad]'),
('Targhib','[Motivasi/ayat/hadis/kisah/penguatan yang benar-benar disampaikan guru]','[Catatan lapangan; bagian langkah atau strategi dalam RPP/i’dad]'),
('Kegiatan inti dan respons siswa','[Aktivitas belajar dan respons/partisipasi siswa yang tercatat]','[Catatan lapangan; dokumentasi yang tersedia]'),
('Tarhib, bila teramati','[Situasi yang terjadi, nasihat/peringatan, dan tindak lanjut guru; jangan menambahkan kejadian yang tidak tercatat]','[Catatan lapangan; aturan atau perangkat ajar yang relevan]'),
('Penutup dan tindak lanjut','[Refleksi, kesimpulan, tugas, atau pesan guru yang benar-benar diamati]','[Catatan lapangan; bagian penutup RPP/i’dad]'),
]
for row in rows:
 cells=t.add_row().cells
 for c,v in zip(cells,row): c.text=v
# Move the table from document end to the intended position.
anchor._p.addprevious(t._tbl)
# Explicit light borders so the evidence matrix remains legible.
pr=t._tbl.tblPr
borders=OxmlElement('w:tblBorders')
for edge in ('top','left','bottom','right','insideH','insideV'):
 el=OxmlElement(f'w:{edge}')
 el.set(qn('w:val'),'single'); el.set(qn('w:sz'),'4'); el.set(qn('w:space'),'0'); el.set(qn('w:color'),'D9D9D9')
 borders.append(el)
pr.append(borders)
widths=[Inches(1.35), Inches(3.25), Inches(1.75)]
for row in t.rows:
 for i,(cell,w) in enumerate(zip(row.cells,widths)):
  cell.width=w
  for p in cell.paragraphs:
   p.paragraph_format.space_after=Pt(0)
   for run in p.runs: run.font.size=Pt(9)
for c in t.rows[0].cells:
 for p in c.paragraphs:
  for run in p.runs: run.bold=True
para('Dalam Bab IV, uraian observasi ini perlu disandingkan dengan bukti yang benar-benar tersedia, misalnya salinan RPP/i’dad tadris, lembar observasi bertanggal, catatan lapangan, dan dokumentasi kelas. Jadwal penelitian pada Bab III menunjukkan observasi berlangsung pada Maret-April 2026, sedangkan tanggal dan rincian pertemuan diisi dari catatan lapangan asli.')
doc.save(out)
print(out)
