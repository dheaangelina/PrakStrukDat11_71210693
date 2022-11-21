class RakObat:
    def __init__(self):
        self.size = 5
        self.map = [None] * self.size

    def getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char) # mendapatkan nilai ASCII
        return hash % self.size

    def probing(self, key):
        for index in range(self.size):
            # probeHash = (self._getHash(key)+index) % self.size
            probeHash = self.linearProbing(key, index)
            # valid bila index adalah None atau ber-flag deleted
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'deleted'):
                return probeHash
        return None

    # melakukan linear probing
    def linearProbing(self, key, index):
        return (self.getHash(key)+index) % self.size

    # menambahkan jenisObat pada hash table
    def tambahObat(self, jenisObat, namaObat):
        # periksa apakah key_hash sudah terpakai
        key_hash = self.getHash(jenisObat)
        # buat pasangan key value
        jenisObat_namaObat = [jenisObat, namaObat]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([jenisObat_namaObat])
            return True
        else:
            key_hash = self.probing(jenisObat)
            if key_hash is None:
                print("Rak Obat anda sudah penuh")
                return False
        self.map[key_hash] = list([jenisObat_namaObat])
        return False

    def lihatObat(self, jenisObat):
        key_hash = self.getHash(jenisObat)
        if (self.map[key_hash] is not None) and (self.map[key_hash] != 'deleted'):
            for index in range(self.size):
                #mencari dengan melakukan probing
                key_hash = self.linearProbing(jenisObat, index)
                # periksa apakah jenisObat adalah data yg akan dihapus
                if(self.map[key_hash][0][0] == jenisObat):
                    return self.map[key_hash][0][1]
        print("Key", jenisObat, "tidak ditemukan")
        return "None"

    def ambilObat(self, jenisObat):
        key_hash = self.getHash(jenisObat)
        if self.map[key_hash] is None:
            return False
        for index in range(self.size):
            #menghapus dengan melakukan linear probing
            key_hash = self.linearProbing(jenisObat, index)
            # periksa apakah jenisObat adalah data yg akan dihapus
            if(self.map[key_hash][0][0] == jenisObat):
                print("obat", jenisObat, "diambil dari rak")
                self.map[key_hash] = "deleted"
                return True
        
        print("Key", jenisObat, "tidak ditemukan")
        return False

    def printAll(self):
        print('==================== List Obat ====================')
        for item in self.map:
            if item is not None and type(item) == list:
                print("Nama :", (item[0][1]), "<> Jenis :", (item[0][0]))
        print('===================================================')


if __name__ == "__main__":
    rak1 = RakObat()

    rak1.tambahObat("Covid", "AstraZeneca (A01)")
    rak1.tambahObat("Flu", "UltraFlu (A02)")
    rak1.tambahObat("Sakit Kepala", "Paramex (A03)")
    rak1.tambahObat("Maag", "Pro Maag (A04)")
    rak1.tambahObat("Sakit Kepala", "Bodrex (A05)")
    rak1.tambahObat("Vitamin", "Vitacimin")

    print(rak1.lihatObat("Sakit Kepala"))
    print(rak1.lihatObat("Migraine"))

    rak1.ambilObat("Flu")
    rak1.ambilObat("Malaria")
    rak1.printAll()