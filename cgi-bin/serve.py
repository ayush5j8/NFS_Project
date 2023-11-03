#!/usr/bin/python3
import subprocess
import cgi

print("Content-type: application/octet-stream")
print("Content-Disposition: attachment; filename=client")
print()

form = cgi.FieldStorage()

ip = form.getvalue("ip")
username = form.getvalue("username")
password = form.getvalue("password")
size = form.getvalue("size")

mount_point = f"/mnt/fs_{ip}"
create_directory_cmd = f"mkdir -p {mount_point}"
subprocess.run(create_directory_cmd, shell=True, check=True)
chmod_cmd = f"chmod -R 777 {mount_point}"
subprocess.run(chmod_cmd, shell=True, check=True)

lv_path = f"/dev/mycloud/{ip}"
create_lv_cmd = f"lvcreate -L {size} -n {ip} mycloud"
create_fs_cmd = f"mkfs.ext4 {lv_path}"
create_mount_cmd = f"mount {lv_path} {mount_point}"

subprocess.run(create_lv_cmd, shell=True, check=True)
subprocess.run(create_fs_cmd, shell=True, check=True)
subprocess.run(create_mount_cmd, shell=True, check=True)

with open("/etc/exports", "a") as exports_file:
    exports_file.write(f"{mount_point} {ip}(rw,sync,no_subtree_check)\n")
subprocess.run("exportfs -a", shell=True, check=True)

generate_exe_cmd = f"pyinstaller /path/to/client.py --onefile --distpath /tmp"
subprocess.run(generate_exe_cmd, shell=True, check=True)
with open("/tmp/client", "rb") as executable:
    import sys
    sys.stdout.buffer.write(executable.read())

fstab_entry = f"{lv_path} {mount_point} ext4 defaults 0 0"
with open('/etc/fstab', 'a') as fstab_file:
    fstab_file.write(fstab_entry+'\n')
subprocess.run("sudo mount -a",shell=True,check=True)
