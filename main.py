import requests
from colorama import Fore , init


red = Fore.RED
blue = Fore.BLUE
reset = Fore.RESET
init()


print(red+'''
 _   _      _ ____  _                _                       
| | | |_ __| / ___|| |__   ___  _ __| |_ ___ _ __   ___ _ __ 
| | | | '__| \___ \| '_ \ / _ \| '__| __/ _ \ '_ \ / _ \ '__|
| |_| | |  | |___) | | | | (_) | |  | ||  __/ | | |  __/ |   
 \___/|_|  |_|____/|_| |_|\___/|_|   \__\___|_| |_|\___|_| 
'''+reset)

def url_shortener():
    while True:
        print(blue+"[-] Url > ", end=""+reset)
        user_url = input()

        header = {
            "Authorization": "Bearer >TOKEN< ",
            "Content-Type": "application/json"
        }
        params = {
            "long_url": str(user_url)
        }

        response = requests.post("https://api-ssl.bitly.com/v4/shorten", json=params, headers=header)
        kisa_url  = response.json()["link"]
        orjinal_url  = response.json()["long_url"]
        print(Fore.GREEN+f"\n[-] Kısaltılmış url > {kisa_url}\n[-] Orjinal Url > {orjinal_url}\n")



if __name__ == "__main__":
    url_shortener()