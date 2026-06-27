# DHCP Client Hook Automation Workflow
- Ansible install the DHCP client package if it is not already installed.
- Ansible creates the /etc/opt/dhcp/dhclient-enter-hooks.d directory if it does not exit.
- Ansible copies the custom Bash script my_hook.sh into the hook directory.
- Ansible sets executable permissions on my_hook.sh
- The DHCP client [dhclient] requests an IP address from the DHCP server.
- After Receiving an IP addr dhclient automatically executes my_hook.sh
- The Bash script perform the required Automation,such as logging the assigned IP address,updating configuration files or triggering additional tasks.
  ## topology details
  isc-dhcp-server[Linux]---------------p1-[switch]-p2--------------Bob[linux]
                                              |
                                             p3
                                              |
  
  
                                              |  
                                              |
                                        John[Red-hat]
