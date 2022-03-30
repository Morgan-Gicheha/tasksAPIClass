USERNAME=root
HOSTS="138.68.189.32"
SCRIPT="pwd"
for HOSTNAME in ${HOSTS} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done