import subprocess

p = subprocess.Popen(["python", "1st.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# get output from process "Something to print"
one_line_output = p.stdout.readline()
print(one_line_output)
one_line_output = p.stdout.readline()
print(one_line_output)

# write 'a line\n' to the process
p.stdin.write('a line\n'.encode())
p.stdin.flush() # not necessary in this case
# get output from process "not time to break"
one_line_output = p.stdout.readline()
print(one_line_output)
# write "n\n" to that process for if r=='n':
p.stdin.write('n\n'.encode())
p.stdin.flush() # not necessary in this case

# read the last output from the process  "Exiting"
one_line_output = p.stdout.read()
print(one_line_output)
