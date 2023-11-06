# NFS_Project
This project is about leveraging the concept of Logical voume management and Network file system that works kinda Google drive allocating storage to users on demand on a minimal scale but rather Block Storage not Object Storage. It's kind of wonderful that you can even create your own partitions on that storage, so this is A Block storage Service. I call it as my "Block Drive ++".

# SERVER Side setup
1. Make sure you have a volume group setup.(create physical volume using pvcreate from one or more VDIs then create a volume group, mine is mycloud.
2. install apache2,pyinstaller
3. enable apache to execute cgi scripts and that too .py scripts as well
4. give superuser permission to www-data with NOPASSWD property so that sudo command doesn't prompt for password
5. www-data user is apache's user that runs our script.
6. Make sure your script has executable permissions.

# Client side setup
1. make sure the user that is running the downloaded script has NOPASSWD property set.
2. now run the script with sudo privileges.

# How to run the project?
1. go to http://<your-server-ip>/index.html [not https]
2. submit the form and then a binary file is downloaded to your system.
3. run that file and now you have a block storage active in /mnt directory.

Note: there might be some additional configuration with your apache server depending on the version and environment variables and also your os specific. Make sure you fix those. 
