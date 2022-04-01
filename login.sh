
USERNAME=root
HOSTS="138.68.189.32"
SCRIPT="git clone git@github.com:Morgan-Gicheha/tasksAPIClass.git"
# value=$(<travisDeploy)
for HOSTNAME in ${HOSTS} ; do
    
    ssh -i  root@138.68.189.32 '${SCRIPT} ls'
    
    # chmod 600 ./deploy_key
    # ssh-keygen  -f -p -P "" -N "" -f ./travisDeploy.enc
    # eval `ssh-agent -s`
    # # ssh-keygen -p -P "" -N "" -f ./deploy_key
    # ssh -o StrictHostKeyChecking=no -i ./deploy_key root@138.68.189.32 'ls'


    # # ssh-add -T pubkey ${value}
    # # ssh -o StrictHostKeyChecking=no -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"

done



