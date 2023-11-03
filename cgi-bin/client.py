#!/usr/bin/python3
import subprocess
def get_ipv4_address():
    try:
        ifconfig_output = subprocess.check_output(["ifconfig"]).decode("utf-8")
        inet_line = [line for line in ifconfig_output.splitlines() if "inet " in line][0]
        ipv4_address = inet_line.split()[1]
        return ipv4_address
    except Exception as e:
        return str(e)
    
    
client_ip=get_ipv4_address()
server_ip = "192.168.1.55"
mount_point = f"/mnt/fs_{client_ip}"
mount_cmd = f"sudo mount {server_ip}:{mount_point} {mount_point}"
fstab_entry = f"{server_ip}:{mount_point} {mount_point} nfs defaults 0 0"
subprocess.run(mount_cmd, shell=True, check=True)
with open("/etc/fstab", "a") as fstab_file:
    fstab_file.write(fstab_entry)
subprocess.run("sudo mount -a",shell=True,check=True)