import paramiko
import os


host = 192.168.100.206
username = root
password = ""

minutos = sys.argv[1]

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command("cd / ")
_stdin, _stdout,_stderr = client.exec_command("cd emotions/ ")
_stdin, _stdout,_stderr = client.exec_command("python main_lite.py "+minutos)
print(stdout.read().decode())
client.close()
os.system("scp root@192.168.100.206:/emotions/data.txt /home/Desktop/")
os.chdir("/home/Desktop")
os.system("geany data.txt")
