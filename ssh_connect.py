
import paramiko
import time
server = '10.84.2.164'
uname = 'administrator'
pwd = 'password'
def ssh_conn():

    #server = '10.84.2.100'

    data = ''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=uname, password=pwd)
    c = ssh.invoke_shell()

    c.setblocking(1)
    resp = b''

    while not c.recv_ready():
        resp = c.recv(2000)
        if resp.decode().endswith('@cli> '):
            break
    # if c.recv_ready():
    #     resp = c.recv(9999)

        # data+=resp
        data = 'administrator@cli> '

    # only @cli, send command to console to execute

    if resp.decode().endswith('@cli> '):

        return c,ssh
