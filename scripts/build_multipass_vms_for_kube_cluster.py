import subprocess

# Define the names of the virtual machines
vm_names = ["kube-master", "kube-node01", "kube-node02"]

# Launch the VMs
for vm_name in vm_names:
    # Check if the virtual machine exists
    check_command = f"multipass info {vm_name}"
    check_return_code = subprocess.call(check_command.split(), stdout=subprocess.DEVNULL)

    # If the return code is 0, the virtual machine exists
    if check_return_code == 0:
        print(f"Virtual machine '{vm_name}' already exists.")
    else:
        # Launch the virtual machine
        launch_command = f"multipass launch focal -n {vm_name} -c 2 -m 4G -d 12G"
        launch_return_code = subprocess.call(launch_command.split())

        if launch_return_code == 0:
            print(f"Virtual machine '{vm_name}' launched successfully.")

        else:
            print(f"Failed to launch virtual machine '{vm_name}'.")




# Enable password authentication in ssh config.

# Iterate over the list of VM names and execute the command on each of them
for vm_name in vm_names:
    sshd_config = f"multipass exec {vm_name} -- sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config"
    subprocess.call(sshd_config, shell=True)

    ssh_service = f" sudo systemctl reload ssh.service"
    subprocess.call(ssh_service, shell=True)

# # Define the path to the sshd_config file
# sshd_config_path = "/etc/ssh/sshd_config"

# # Open the sshd_config file for reading and writing
# with open(sshd_config_path, "r+") as sshd_config_file:
#     # Read the contents of the file
#     sshd_config_contents = sshd_config_file.read()

#     # Replace the line that comments out PasswordAuthentication with one that enables it
#     sshd_config_contents = sshd_config_contents.replace("#PasswordAuthentication", "PasswordAuthentication")

#     # Replace the line that enables/disables password authentication with one that enables it
#     sshd_config_contents = sshd_config_contents.replace("PasswordAuthentication no", "PasswordAuthentication yes")

#     # Return to the beginning of the file and write the modified contents
#     sshd_config_file.seek(0)
#     sshd_config_file.write(sshd_config_contents)
#     sshd_config_file.truncate()

# # Restart the SSH service to apply the changes
# restart_command = "sudo systemctl restart ssh"
# subprocess.call(restart_command.split())

    
