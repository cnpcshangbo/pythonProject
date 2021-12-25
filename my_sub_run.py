import subprocess
retur=subprocess.run(["ls", "-l"], capture_output=True)
print(type(retur))
