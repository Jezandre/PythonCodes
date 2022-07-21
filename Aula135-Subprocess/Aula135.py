import subprocess
# - ping 127.0.0.1
# - ping 127.0.0.1

proc = subprocess.run(
    ['ping','127.0.0.1'],
    capture_output=True,
    text=True
)

saida = proc.stdout
saida = saida.replace('icmp_seq', 'LuizOtavio')
print(proc.stdout)

