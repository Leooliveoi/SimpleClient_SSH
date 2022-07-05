import paramiko
host = "0.0.0.0"
user = "root"
passwd = "root"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(host, username=user, password=passwd)
while True:
    stdin, stdout, stderr = client.exec_command(input("Enter a Command: "))
    for line in stdout.readlines():
        print(line.strip())

    erro = stderr.readlines()
    if erro:
        print(erro)
