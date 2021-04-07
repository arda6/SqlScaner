### Coded by EYLL'
### github link : https://www.github.com/arda6
import requests
print("""
 _______  _____         _______ _______ _______ __   _ __   _ _______  ______
 |______ |   __| |      |______ |       |_____| | \  | | \  | |______ |_____/
 ______| |____\| |_____ ______| |_____  |     | |  \_| |  \_| |______ |    \_
 
                                                        Powered by EYLL'
                                                        
                                                        o yabancı pop severdi                     
                                                        
""")
while True:
    site = input("Hedef Site : ")
    url = requests.get(r""+site+"'")
    sql = str(url.content)
    if sql.find("syntax") == int('-1'):
       print("")
       print(""+site+ "Hedefte Açık Tespit Edilemedi")
    else :
        print("")
        print(""+site+ " Hedefte SQL İnjection Tespit Edildi")
        print("")
