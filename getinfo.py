import requests,json
ses=requests.Session()

bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
kontol = []
memek = []
token = input("Masukan Token : ")
idt = input("Masukan ID : ")
url = ses.get(f"https://graph.facebook.com/{idt}?&access_token={token}").json()
uid = url["id"]
try:
	ttl = url["birthday"]
	month,day,year = ttl.split("/")
	month = bulan[month]
except:
	day = "-"
	month = ""
	year = ""
try:
	nama_depan = url["first_name"]
except:
	nama_depan = "-"
try:
	kelamin = url["gender"]
except:
	kelamin = "-"
try:
	nama_belakang = url["last_name"]
except:
	nama_belakang = "-"
try:
	link = url["link"]
except:
	link = "-"
try:
	lokasi = url["location"]["name"]
except:
	lokasi = "-"
try:
	nama_lengkap = url["name"]
except:
	nama_lengkap = "-"
try:
	username = url["username"]
except:
	username = "-"
try:
	dari_kota = url["hometown"]["name"]
except:
	dari_kota = "-"
try:
	bahasa = url["locale"]
	if "id_ID" in bahasa:
		bahasa_akun = "Bahasa Indonesia"
	else:
		bahasa_akun = "Bahasa Luar"
except:
	bahasa_akun = "-"
try:
	terakhir_update = url["updated_time"][:10]
	year2,month2,day2 = terakhir_update.split("-")
	month2 = bulan[month2]
except:
	day2 = "-"
	month2 = ""
	year2 = ""
try:
	for i in ses.get(f"https://graph.facebook.com/{uid}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}").json()["friends"]["data"]:
		kontol.append(i["id"])
	teman = len(kontol)
except:
	teman = "-"
try:
	for i in ses.get(f"https://graph.facebook.com/{uid}?fields=name,subscribers.fields(id,name).limit(500000)&access_token={token}").json()["subscribers"]["data"]:
		memek.append(i["id"])
	fols = len(memek)
except:
	fols = "-"
	
print(f"""
ID : {uid}
TTL : {day} {month} {year}
Jumlah Teman : {teman}
Jumlah Followers : {fols}
Nama Depan : {nama_depan}
Nama Belakang : {nama_belakang}
Nama Lengkap : {nama_lengkap}
Link Akun : {link}
Username : {username}
Kelamin : {kelamin}
Tinggal Di : {lokasi}
Dari Kota : {dari_kota}
Terakhir Update : {day2} {month2} {year2}
Bahasa Akun : {bahasa_akun}
""")