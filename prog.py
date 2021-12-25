import sys

print('what is your name?')
sys.stdout.flush()
while True:
    name = input()
    print('received you name.')
    print('your name is ' + name)
    sys.stdout.flush()
