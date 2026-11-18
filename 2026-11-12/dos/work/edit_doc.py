from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from pathlib import Path
src=Path(r'C:/Users/ASUS/OneDrive/Documents/Rencana Penelitian Tesis/File Proposal Diujikan/Bimbingan setelah SK/BAB 4/REV_BAB IV Jujun (20-7-26).docx')
out=Path(r'C:/Users/ASUS/Documents/Codex/2026-11-12/dos/outputs/REV_BAB_IV_Jujun_dengan_bukti_periode_implementasi.docx')
doc=Document(src)
anchor=next(p for p in doc.paragraphs if p.text.strip().startswith('Implementasi Metode Targhib dalam Pengembangan Budaya Religius'))
def insert_para(text, style='Normal', before=anchor):
 p=before.insert_paragraph_before(text, style=style)
 return p
insert_para('Masa dan Kesinambungan Implementasi Metode Targhib wa Tarhib', 'Heading 3')
insert_para('Bukti dokumentasi dalam penelitian ini menunjukkan bahwa konteks implementasi metode targhib wa tarhib berlangsung di tengah program keagamaan yang terjadwal dan berulang. Jadwal kegiatan peserta didik yang disajikan pada Tabel 4.5 sampai dengan Tabel 4.8 memuat kegiatan harian, mingguan, semesteran, dan tahunan. Rentang tersebut memberi bukti tentang kesinambungan kesempatan pembinaan dan pembiasaan yang menjadi konteks penerapan metode oleh pendidik.')
insert_para('Ringkasan bukti periode kegiatan disajikan pada tabel berikut. Pengelompokan ini merujuk pada agenda yang telah dicantumkan dalam naskah, bukan pada tanggal awal penerapan metode.')
t=doc.add_table(rows=1, cols=3)

for cell, val in zip(t.rows[0].cells, ['Periode kegiatan','Bukti yang tercantum dalam naskah','Rujukan']): cell.text=val
rows=[
('Harian','Agenda salat berjamaah, pengajian, pembelajaran, dan pembinaan peserta didik.','Tabel 4.5'),
('Mingguan','Agenda kegiatan keagamaan dan pembinaan yang dijadwalkan menurut hari.','Tabel 4.6'),
('Semesteran','Agenda ujian akhir semester dan Pekan Bahasa.','Tabel 4.7'),
('Tahunan','Agenda kegiatan keagamaan dan kepesantrenan sepanjang siklus tahun ajaran.','Tabel 4.8'),
]
for row in rows:
 cells=t.add_row().cells
 for c,val in zip(cells,row): c.text=val
# move table XML to immediately before original anchor
anchor._p.addprevious(t._tbl)
insert_para('Berdasarkan bukti tersebut, implementasi yang dibahas pada bagian ini dapat dijelaskan sebagai proses yang hadir dalam kegiatan rutin dan dalam beberapa skala waktu, dari harian hingga tahunan. Namun, agenda kegiatan hanya membuktikan jadwal program lembaga; agenda tersebut tidak dengan sendirinya menetapkan sejak kapan metode targhib wa tarhib mulai digunakan. Naskah yang tersedia juga belum mencantumkan tanggal observasi atau rentang waktu pengumpulan data. Karena itu, klaim tentang tahun atau tanggal awal penerapan metode perlu didukung dengan keterangan wawancara yang menyebut waktu secara spesifik, catatan observasi bertanggal, atau dokumen program/evaluasi dari tahun terkait.')
# table typography and header emphasis
for cell in t.rows[0].cells:
 for p in cell.paragraphs:
  for r in p.runs: r.bold=True
for row in t.rows:
 for cell in row.cells:
  for p in cell.paragraphs:
   p.paragraph_format.space_after=Pt(0)
   for r in p.runs: r.font.size=Pt(10)
doc.save(out)
print(out)
