from docx import Document
from pathlib import Path
src=Path(r'C:/Users/ASUS/OneDrive/Documents/Rencana Penelitian Tesis/File Proposal Diujikan/Bimbingan setelah SK/BAB 3/Rev3_BAB III (20-7-26).docx')
out=Path(r'C:/Users/ASUS/Documents/Codex/2026-11-12/dos/outputs/Rev3_BAB_III_periode_observasi_implementasi.docx')
doc=Document(src)
p=next(x for x in doc.paragraphs if x.text.strip().startswith('Pelaksanaan penelitian dilakukan pada bulan Februari 2026'))
p.text=('Penelitian ini dilaksanakan pada bulan Februari sampai dengan Juli 2026. Berdasarkan jadwal penelitian pada Tabel 3.1, observasi dilaksanakan pada Maret sampai dengan April 2026, sedangkan wawancara dan pengumpulan dokumentasi dilaksanakan pada Maret sampai dengan Mei 2026. Analisis data berlangsung pada Mei sampai dengan Juli 2026, kemudian triangulasi dan member checking dilaksanakan pada Juni sampai dengan Juli 2026. Dengan demikian, observasi langsung terhadap penerapan metode di kelas berlangsung pada Maret-April 2026; rentang ini menunjukkan masa pengamatan penelitian, bukan tahun awal metode tersebut mulai diterapkan di madrasah.')
anchor=next(x for x in doc.paragraphs if x.text.strip().startswith('Untuk memberikan gambaran yang lebih sistematis mengenai tahapan pelaksanaan penelitian'))
h=anchor.insert_paragraph_before('Batas Periode Pengamatan Implementasi Metode', style='List Paragraph')
body=anchor.insert_paragraph_before('Pengamatan implementasi metode targhib wa tarhib difokuskan pada proses pembelajaran PAI di kelas XI MA Daarussalam Kunir selama Maret-April 2026. Pada setiap kegiatan yang diamati, lembar observasi dan catatan lapangan digunakan untuk mencatat tanggal atau pertemuan, konteks materi pembelajaran, tindakan guru yang menunjukkan unsur targhib atau tarhib, serta respons dan partisipasi peserta didik. Catatan tersebut diperiksa bersama dokumen pembelajaran yang tersedia, seperti RPP atau i’dad al-tadris, media pembelajaran, foto atau video kegiatan, dan keterangan wawancara guru maupun peserta didik. Pencantuman tanggal pada catatan lapangan memungkinkan temuan Bab IV ditautkan pada masa pengamatan yang jelas dan dibedakan dari rutinitas lembaga yang berlaku sepanjang tahun.')
doc.save(out)
print(out)
