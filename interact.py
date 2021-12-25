from subprocess import Popen, PIPE, STDOUT
p = Popen(['python', 'prog.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
p.stdout.readline().rstrip()
outs, errs = p.communicate('mike'.encode('utf-8'))
print(outs.decode('utf-8'))
print(type(outs))
print(errs)
#p.stdout.readline().rstrip()
outs, errs = p.communicate('bo'.encode('utf-8'))
print(outs.decode('utf-8'))
print(type(outs))
print(errs)

p.wait()
