#!/bin/bash -e

# Write the host IP and Ansible variables to the inventory file
echo "$host_ip ansible_user=$ansible_user ansible_password=$ansible_pass" > inventory.ini

# Run the playbook using the inventory file and passing extra variables
ansible-playbook playbook.yml -i inventory.ini -e "ansible_port=$ansible_port"