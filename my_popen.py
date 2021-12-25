import subprocess

ps = subprocess.Popen(('python', 'prog.py'), stdout=subprocess.PIPE)
output = subprocess.check_output(('grep', 'na'), stdin=ps.stdout)
print(output.decode('utf-8'))
ps.wait()
