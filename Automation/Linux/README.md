# Understanding sudo -i and User Permissions
Scenario
Logged in as a normal user
- abc@xyz:~$
- trying to access another user's home directory
- cd /home/x2
- output: -bash:cd: /home/x2: Permission denied
- Reason: the current user abc does not have permission to access the /home/x2 directory
## Switch to the Root User
sudo -i 
the prompt changes to:
root@xyz:~#
verify the current user:
root@xyz:~#whoami -> ouptput root
Now access the directory -> the command succeeds.

Explanation:
-----------
sudo -i starts a login shell as the root user
After switching ,all commands are executed with root privileges.
The root user is the linux superuser and can access almost all files and directories on the system.
A normal user can access only the files and directories for which permission has been granted.

- ubuntu@ansible-controller:/home$ whoami
- ubuntu
- ubuntu@ansible-controller:/home$ sudo -i
- root@ansible-controller:~# cd /home/devops
- root@ansible-controller:/home/devops# ls
- my_playbook.yaml ansible.cfg qainv setup_user.py hosts roles
- root@ansible-controller:/home/devops# whoami
- root
- root@ansible-controller:/home/devops#
## 
# Run a command as the user "deployer" instead of root
sudo -u deployer whoami
# → output: deployer

# Open a shell as another user (useful for testing their environment)
sudo -u deployer -i
# -i = "login shell", loads that user's .bashrc, sets $HOME, etc.

# Run a single command as another user, then come back to yourself
sudo -u deployer ls -la /home/deployer

# Switch to root specifically (same as plain sudo, just explicit)
sudo -u root systemctl restart isc-dhcp-server


