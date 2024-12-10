class ViewMahasiswa:
    @staticmethod
    def daftar_mahasiswa(data):
        if not data:
            print("Tidak ada data mahasiswa.")
        else:
            for nim, info in data.items():
                print(f"NIM: {nim}, Nama: {info['nama']}, Jurusan: {info['jurusan']}")

    @staticmethod
    def detail_mahasiswa(mahasiswa):
        print(f"NIM: {mahasiswa['nim']}")
        print(f"Nama: {mahasiswa['nama']}")
        print(f"Jurusan: {mahasiswa['jurusan']}")