USERNAME=root
HOSTS="138.68.189.32"
SCRIPT="pwd"
for HOSTNAME in ${HOSTS} ; do
    # eval `ssh-agent -s`
    ssh -o StrictHostKeyChecking=no -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
    ping  ${HOSTNAME}
done