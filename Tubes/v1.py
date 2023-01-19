import csv

def load_data(filename):
    data = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

def save_data(filename, data):
    fieldnames = ['nama', 'stok', 'harga']
    with open(filename, 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)

def search_data(data, key, value):
    for row in data:
        if row[key] == value:
            return row
    return None

def sort_data(data, key):
    return sorted(data, key=lambda x: x[key])

def update_stok(data, nama, jumlah):
    for i, row in enumerate(data):
        if row['nama'] == nama:
            data[i]['stok'] = str(int(row['stok']) + jumlah)
    return data

def transaksi(data, nama, jumlah):
    for i, row in enumerate(data):
        if row['nama'] == nama:
            data[i]['stok'] = str(int(row['stok']) - jumlah)
    return data

jawab = 'iya'
while jawab == 'iya':
    
    print('=============== Menu ===============')
    print('1. Review Data')
    print('2. Searching Data')
    print('3. Sorting Data')
    print('4. Update Data')
    print('5. Transaksi')
    print('====================================')

    print('Pilih menu :')
    pilih = input('- ')
    print('====================================')

    # Review data
    if pilih == 'Review Data' or pilih == '1':
        jawab = 'iya'
        while jawab == 'iya':
            
            filename = 'stok_barang.csv'
            data = load_data(filename)
            
            print('Data keseluruhan : ')
            print(data)
            print('====================================')
            print('Apakah anda ingin review lagi? iya/tidak')
            print('====================================')
            jawab = input('- ')
            print('====================================')

    # Searching data
    elif pilih == 'Searching Data' or pilih == '2':
        jawab = 'iya'
        while jawab == 'iya':
            
            filename = "stok_barang.csv"
            data = load_data(filename)
            
            print('Masukkan nama barang : ')
            value = input('- ')
            print('====================================')
            search_key = 'nama'
            result = search_data(data, search_key, value)
            if result:
                print('Data ditemukan : ')
                print(result)
                print('====================================')
            else:
                print('Data tidak ditemukan')
                print('====================================')
            print('Apakah anda ingin searching lagi? iya/tidak')
            print('====================================')
            jawab = input('- ')
            print('====================================')

    # Sorting data
    elif pilih == 'Sorting Data' or pilih == '3':
        jawab = 'iya'
        while jawab == 'iya':
            
            filename = 'stok_barang.csv'
            data = load_data(filename)
            
            sort_key = 'stok'
            data = sort_data(data, sort_key)
            print('Urutan data terendah : ')
            print(data)
            print('====================================')
            print('Apakah anda ingin sorting lagi? iya/tidak')
            print('====================================')
            jawab = input('- ')
            print('====================================')

    # Update stok
    elif pilih == 'Update Data' or pilih == '4':
        jawab = 'iya'
        while jawab == 'iya':
            
            filename = 'stok_barang.csv'
            data = load_data(filename)
            
            print('Masukkan nama barang : ')
            key = input('- ')
            print('====================================')
            search_key = 'nama'
            result = search_data(data, search_key, key)
            if result:
                print('Masukkan jumlah update : ')
                jumlah = int(input('- '))
                print('====================================')
                data = update_stok(data, key, jumlah)
                print('Data berhasil diperbarui')
                print('====================================')
                
                # Saving data
                save_data(filename, data)
                print('Data berhasil disimpan ke file CSV.')
                print('====================================')
            else:
                print('Data tidak ditemukan')
                print('====================================')
            
            print('Apakah anda ingin update lagi? iya/tidak')
            print('====================================')
            jawab = input('- ')
            print('====================================')
            
    # Transaksi
    elif pilih == 'Transaksi' or pilih == '5':
        jawab = 'iya'
        while jawab == 'iya':
            
            filename = 'stok_barang.csv'
            data = load_data(filename)
            
            print('Masukkan nama barang : ')
            key = input('- ')
            print('====================================')
            search_key = 'nama'
            result = search_data(data, search_key, key)
            if result:
                print('Masukkan jumlah transaksi : ')
                jumlah = int(input('- '))
                print('====================================')
                data = transaksi(data, key, jumlah)
                print('Data berhasil diperbarui')
                print('====================================') 
                
                # Saving data
                save_data(filename, data)
                print('Data berhasil disimpan ke file CSV.')
                print('====================================')
            else:
                print('Data tidak ditemukan')
                print('====================================')
            
            print('Apakah anda ingin transaksi lagi? iya/tidak')
            print('====================================')
            jawab = input('- ')
            print('====================================')
            
    print('Apakah anda ingin kembali ke halaman awal? iya/tidak')
    print('====================================')
    jawab = input('- ')