
USERNAME=root
HOSTS="138.68.189.32"
SCRIPT="pwd"
value=$(<travisDeploy)
for HOSTNAME in ${HOSTS} ; do
    # ssh -i ./travisDeploy root@138.68.189.32 'ls'
    ping google.com
    
    # eval `ssh-agent -s`
    # # ssh-add -T pubkey ${value}
    # # ssh -o StrictHostKeyChecking=no -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
    # ssh  root@138.68.189.32


done



