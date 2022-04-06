

USERNAME=root
HOSTS="138.68.189.32"
SCRIPT=" rm -r tasksAPIClass; git clone https://github.com/Morgan-Gicheha/tasksAPIClass.git; cd tasksAPIClass; ls"
for HOSTNAME in ${HOSTS} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done