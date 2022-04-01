
USERNAME=root
HOSTS="138.68.189.32"
SCRIPT="pwd"
# value=$(<travisDeploy)
for HOSTNAME in ${HOSTS} ; do
    
    # ssh-keygen  -f -p -P "" -N "" -f ./travisDeploy.enc
    sshpass -p passphrase ssh-add ./travisDeploy.enc
    eval $(ssh-agent)
    ssh-add
    ssh -o StrictHostKeyChecking=no -i ./travisDeploy.enc root@138.68.189.32 'ls'
    ls
    pwd
    
    # eval `ssh-agent -s`
    # # ssh-add -T pubkey ${value}
    # # ssh -o StrictHostKeyChecking=no -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
    # ssh  root@138.68.189.32



done



