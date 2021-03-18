
########################################################################
# By Kristian
# Eiii lammer 
# Kiba o codigo e vai me mamar para sempre! Alem de ser lammer

########################################################################


from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import sys
import time



if sys.version[0] in "2":
    print ("\n[x] ..L4mm3r.. você esta usando Python 2.x Use Python 3.x \n")
    print ("\n\n\tDeadly Parser \033[1;91mMuito bem! Não me decepcione. \033[0m\n\n")
    exit()


class colors:
    CRED2 = "\u001b[35;1m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"


banner = ("""
         ._                __.
        / \"-.          ,-",'/ 
       (   \ ,"--.__.--".,' /  
       =---Y(_i.-'  |-.i_)---=
      f ,  "..'/\\v/|/|/\  , l
      l//  ,'|/   V / /||  \\j
       "--; / db     db|/---"
          | \ YY   , YY//
          '.\>_   (_),"' __
        .-"    "-.-." I,"  `.
        \.-""-. ( , ) ( \   |
        (     l  `"'  -'-._j 
 __,---_ '._." .  .    \
(__.--_-'.  ,  :  '  \  '-.
    ,' .'  /   |   \  \  \ "-
     "--.._____t____.--'-""'
            /  /  `. ".
           / ":     \' '.
         .'  (       \   : 
         |    l      j    "-.
         l_;_;I      l____;_I

                         v1.0 """)


for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
      ( ◕‿◕)(•̤̀‿•̤́)(◕‿◕)(◕∀◕) \n """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\tWith Bloods in our hand, only one of us is leaving.\n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


try:
    data = input("\n[ᴥ] Você gostaria de salvar os resultados em txt? (S/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] Oops, que lame, cancelou o processo..!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] Muito bem! Não me decepcione. \033[0m\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("s" or "S"):
    l0g = input("[~] Qual nome eu deveria dar no arquivo: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] Avancei esse passo...")
    print ("\n" + "  " + "»" * 78 + "\n")


def dorks():
    try:
        dork = input("\n[ᴥ] Manda uma query para ser pesquisada: ")
        quantidade = input("[ᴥ] Quantos websites a serem enviados: ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="pt", num=int(quantidade), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[ᴥ] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(quantidade):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] Oops, que lame, cancelou o processo..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] Muito bem! Não me decepcione.  \033[0m\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Pronto... Saindo da tool...")
    print ("\n\t\t\t\t\033[34mDeadly Parsers x Casa Blanca\033[0m")
    print ("\t\t\033[1;91m[!] Muito bem! Não me decepcione. \033[0m\n\n")
    sys.exit()

if __name__ == "__main__":
    dorks()
