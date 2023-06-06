import re

# alat bantu: regex101

# fungsi membaca isi file
def baca_file(nama_file):
    handle = open(nama_file)
    artikel = handle.read()
    handle.close()
    return artikel

# input nama file
nama_file = input('Masukkan nama file: ')

#  baca berita dari file
artikel = baca_file(nama_file)

# lakukan operasi regex
# 1. Tampilkan semua kata yang diawali huruf besar
pattern = r"[A-Z]\w+"
hasil = re.findall(pattern, artikel) # cari semua
print(f'Ditemukan {len(hasil)} kata yang diawali huruf besar')
print(hasil)

# 2. Tampilkan informasi tanggal
pattern = r"\d+/\d+/\d{4}"
hasil = re.findall(pattern, artikel) # kalau re.search() cari satu, berarti kalau mau ambil semua pakai looping
print(f'Ditemukan {len(hasil)} tanggal')
print(hasil)

# 3. Tampilkan semua kata yang panjangnya 7
pattern = r"\b\w{7}\b" # word boundary, untuk mengambil kata keseluruhan agar tidak terpotong
hasil = re.findall(pattern, artikel)
print(f'Ditemukan {len(hasil)} kata yang panjangnya 7')
print(hasil)

# 4. Tampilkan semua string nilai uang
pattern = r"\bRp.{3,9}ribu\b|\bRp.{3,9}juta\b" # word boundary, untuk mengambil kata keseluruhan agar tidak terpotong
hasil = re.findall(pattern, artikel)
print(f'Ditemukan {len(hasil)} string uang')
print(hasil)

# 5. Ganti semua kata tertentu dengan input user
kata_lama = input('Masukkan kata yang akan diganti (case sensitive): ')
kata_baru = input('Masukkan kata penggantinya: ')

hasil = re.sub(kata_lama, kata_baru, artikel)

# simpan dalam file
handle = open(nama_file, 'w')
handle.write(hasil)
handle.close()