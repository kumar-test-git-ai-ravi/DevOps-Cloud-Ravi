# SSH Login from one EC2 Instance to Another Machine.
abc@xyz:~$ssh -i xyz.pem Another_user@Ip_address
Explanation: 
- abc: Current Linux username
- xyz: Hostname of Ec2 instance where you are currently logged in.
- ~: Current user's home directory
- $: Normal user shell prompt
## SSH 
Used to established a secure SSH connection to another Linux server.
i abc.pem
- i: means identify File
- abc.pem: is the private key used to authenticate with the destination EC2 instance.
## What Happen when This Command Is Executed
- The ssh client start a connection to the destination EC2 instance.
- SSH uses the private key abc.pem for authentication
- the destination ec2 instance checks the matching public key in ~/.ssh/authorized_keys.
- if the keys match,the SSH session is established
- on the first successful connection,~/.ssh/known_hosts.
- on future connections ,SSH checks known_hosts to verify the server's identify before completing the connection.
