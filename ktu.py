from os import system
from time import sleep
from datetime import datetime
from argparse import ArgumentParser


def check_ping(hostname:str):
    response = system("ping -c 1 " + hostname)

    if response == 0:
        return True
    else:
        return False

def main():
    parser = ArgumentParser(description="wtop args parser")
    parser.add_argument('-host', dest='host', type=str, default=False)
    parser.add_argument('-command', dest='command', type=str, default='')
    args = parser.parse_args()
    while True:
        sleep(2)
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        isup = check_ping(args.host)
        print(f'[log {now}] Access Point UP: {isup}')
        if not isup:
            system(f'{args.command}')



if __name__ == '__main__':
    main()
