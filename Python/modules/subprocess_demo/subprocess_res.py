import subprocess

cmd = "ifconfig"

r = subprocess.run(cmd, shell=True, check=True, capture_output=True)

print(r)
print(r.returncode)
print(r.args)
print(r.stdout.decode("utf8"))
print(type(r.stdout.decode("utf8")))
print(r.stderr.decode("utf8"))
