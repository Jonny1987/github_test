import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--error', action='store_true')
parser.add_argument('-x')
args = parser.parse_args()

wait_time = 0
if args.x == 'b':
    wait_time += 3
if args.error:
    wait_time += 1

time.sleep(wait_time)
if args.error and args.x == 'a':
    raise Exception()
else:
    print('Successful')

