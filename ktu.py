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
    parser.add_argument('-sleep', dest='sleep', type=int, default=2)
    parser.add_argument('-command', dest='command', type=str, default='')
    args = parser.parse_args()
    sleep_seconds = args.sleep
    secs_after_error = 0

    while True:
        sleep(sleep_seconds)
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        isup = check_ping(args.host)
        print(f'[log {now}] Tunel to {args.host} UP: {isup} \n')
        if isup:
            if secs_after_error != 0:
                secs_after_error = 0
                sleep_seconds = args.sleep
        else:
            secs_after_error+=sleep_seconds
            if secs_after_error <= 60:
                system(f'{args.command}')
            else:
                sleep_seconds = 60




if __name__ == '__main__':
    main()
