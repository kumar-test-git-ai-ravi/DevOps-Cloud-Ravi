import paramiko
import time
import reg

"""
this is script login using the ssh

below are manuall step i have written for login DUT using ssh 
1. go the linux terminal where i have access to lab  devices.[ravi-desktop] where in netstat routing table we can see the routes to reach the lab devices[93.0.0.166/24]
2. onces step 1 is correct and verified using the ping 93.0.0.166 then do ssh dut_166@93.0.0.166 asking for password: after password is filled then HIT ENTER On keyboard3. then observed the prompt will change from [ravi-desktop] to DUT-prompt# that means i have successfully login to our LAB DEVICES.
4. Now i start my testing on cisco-IOS XE cisco catalyst 9300
5. but to login from ssh-access-lab-devices using the script then i have run the ssh-access.py from [ravi-desktop] terminal.
"""
"""
1.ssh -i mykey.pem ubuntu@10.0.1.25
2.pip3 install paramiko
3.
"""
import paramiko

host = "10.0.1.25"  # EC2-2 private IP
user = "ubuntu"
key_path = "/home/ubuntu/mykey.pem"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

private_key = paramiko.RSAKey.from_private_key_file(key_path)

ssh.connect(
    hostname=host,
    username=user,
    pkey=private_key
)

stdin, stdout, stderr = ssh.exec_command("hostname")

print("Hostname:", stdout.read().decode())

ssh.close()
