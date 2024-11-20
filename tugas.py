nama = input ("Nama : ")

print ("===============Barang===============")
print ("1. Sendok  (2.000)")
print ("2. piring  (5.000)")
print ("3. sabun   (3.000)")
print ("4. mangkok (5.000)")
print ("====================================")

sendok  = (2000)
piring  = (5000)
sabun   = (3000)
mangkok = (5000)

# dictionary
keranjang = {
    "Sendok" : 0,
    "Piring" : 0,
    "Sabun"  : 0,
    "Mangkok": 0
}

total_biaya = 0

print ("(input 0 untuk berhenti membeli!)")

while True:
    input_data = int(input ("pilih barang list barang yang akan dibeli (1/2/3/4) : ")) 
    if input_data == 0:
        break
    elif input_data == 1:
        jumlah_data = int (input ("masukan jumlah barang : "))
        keranjang ["Sendok"] += jumlah_data
        total_biaya += sendok * jumlah_data
    elif input_data == 2:
        jumlah_data = int (input ("masukan jumlah barang : "))
        keranjang ["Piring"] += jumlah_data
        total_biaya += piring * jumlah_data
    elif input_data == 3:
        jumlah_data = int (input ("masukan jumlah barang : "))
        keranjang ["Sabun"] += jumlah_data
        total_biaya += sabun * jumlah_data
    elif input_data == 4:
        jumlah_data = int (input ("masukan jumlah barang : "))
        keranjang ["Mangkok"] += jumlah_data
        total_biaya += mangkok * jumlah_data
    elif input_data > 4 or input_data < 0:
        jumlah_data = int (input ("masukan jumlah barang : "))
        print ("perintah salah!")
        break

print ("===============Rincian===============")
print(f"Nama Pembeli: {nama}")
for barang, jumlah in keranjang.items():
    if jumlah > 0:
        print(f"{barang} : {jumlah}")
print(f"Total Biaya: Rp {total_biaya}")
print("================Bayar================")

bayar = int(input ("Masukan sejumlah uang : "))
if bayar > total_biaya:
    print (f"kembalian anda : Rp {bayar - total_biaya}, Terimakasih")
elif bayar == total_biaya:
    print ("Uang anda pas, Terimakasih")
else:
    print (f"uang anda kurang Rp {total_biaya - bayar}, silahkan ambil uang terlebih dahulu")











