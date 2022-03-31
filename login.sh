USERNAME=root
HOSTS="138.68.189.32"
SCRIPT="pwd"
value=$(<travisDeploy)
for HOSTNAME in ${HOSTS} ; do
    eval `ssh-agent -s`
    ssh-add ${value}
    ssh -o StrictHostKeyChecking=no -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done

