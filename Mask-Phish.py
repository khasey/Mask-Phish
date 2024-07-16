import re
import requests
import colorama
from colorama import Fore, Back, Style

def url_checker(url):
    if not re.match(r'^http[s]?://', url):
        print("\033[31m[!] Invalid URL. Please use http or https.\033[0m")
        exit(1)

def main():
    print(Fore.RED +""" 
        
███╗   ███╗ █████╗ ███████╗██╗  ██╗     ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗
████╗ ████║██╔══██╗██╔════╝██║ ██╔╝     ██╔══██╗██║  ██║██║██╔════╝██║  ██║
██╔████╔██║███████║███████╗█████╔╝█████╗██████╔╝███████║██║███████╗███████║
██║╚██╔╝██║██╔══██║╚════██║██╔═██╗╚════╝██╔═══╝ ██╔══██║██║╚════██║██╔══██║
██║ ╚═╝ ██║██║  ██║███████║██║  ██╗     ██║     ██║  ██║██║███████║██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝
Created by: Khasey_Nine_Z
        """ + Fore.RESET)

    phish = input(Fore.MAGENTA + "Paste Phishing URL here (with http or https): " + Fore.RESET)
    url_checker(phish)

    print("Processing and Modifying Phishing URL\n")
    short = requests.get(f'https://is.gd/create.php?format=simple&url={phish}').text
    shorter = short.replace('https://', '')

    print(Fore.MAGENTA + "### Masking Domain ###" + Fore.RESET)
    mask = input('Domain to mask the Phishing URL (with http or https), ex: https://google.com, http://anything.org): ')
    url_checker(mask)

    print(Fore.GREEN + '\nType social engineering words:(like free-money, best-pubg-tricks)' + Fore.RESET)
    print("\033[31mDon't use space just use '-' between social engineering words\033[0m")
    words = input("=> ")

    if not words:
        print("\033[31m[!] No words.\033[0m")
        print("\nGenerating MaskPhish Link...\n")
        final = f"{mask}@{shorter}"
        print(f"Here is the MaskPhish URL:\033[32m {final} \033[0m\n")
        exit()

    if ' ' in words:
        print("\033[31m[!] Invalid words. Please avoid space.\033[0m")
        print("\nGenerating MaskPhish Link...\n")
        final = f"{mask}@{shorter}"
        print(f"Here is the MaskPhish URL:\033[32m {final} \033[0m\n")
        exit()

    print("\nGenerating MaskPhish Link...\n")
    final = f"{mask}-{words}@{shorter}"
    print(f"Here is the MaskPhish URL:\033[32m {final} \033[0m\n")

if __name__ == "__main__":
    main()
