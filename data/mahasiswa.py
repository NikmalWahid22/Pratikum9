class DataMahasiswa:
    def __init__(self):
        self.data = {}

    def tambah_mahasiswa(self, nim, nama, jurusan):
        if nim in self.data:
            print("NIM sudah terdaftar.")
        else:
            self.data[nim] = {'nama': nama, 'jurusan': jurusan}

    def cari_mahasiswa(self, nim):
        return self.data.get(nim)

    def ubah_mahasiswa(self, nim, nama_baru, jurusan_baru):
        if nim in self.data:
            self.data[nim] = {'nama': nama_baru, 'jurusan': jurusan_baru}
            return True
        return False

    def hapus_mahasiswa(self, nim):
        if nim in self.data:
            del self.data[nim]
            return True
        return False