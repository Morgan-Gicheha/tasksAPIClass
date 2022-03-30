USERNAME=root
HOSTS="138.68.189.32"
SCRIPT="pwd"
for HOSTNAME in ${HOSTS} ; do
    eval `ssh-agent -s`
    ssh-add travisDeploy
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done