
USERNAME=root
HOSTS="138.68.189.32"
SCRIPT="pwd"
value=$(<travisDeploy)
for HOSTNAME in ${HOSTS} ; do
    eval `ssh-agent -s`
    # ssh-add -T pubkey ${value}
    ssh -o StrictHostKeyChecking=no -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
    # ping google.com
done

ssh root@138.68.189.32