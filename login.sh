
USERNAME=root
HOSTS="138.68.189.32"
SCRIPT="pwd"
# value=$(<travisDeploy)
for HOSTNAME in ${HOSTS} ; do
    chmod 600 ./travisDeploy
    # ssh-keygen  -f -p -P "" -N "" -f ./travisDeploy.enc
    eval `ssh-agent -s`
    ssh-keygen -p -P "" -N "" -f ./travisDeploy
    ssh -o StrictHostKeyChecking=no -i ./travisDeploy root@138.68.189.32 'ls'
    ping google.com
    # # ssh-add -T pubkey ${value}
    # # ssh -o StrictHostKeyChecking=no -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
    



done



