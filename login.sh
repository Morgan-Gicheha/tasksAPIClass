

USERNAME=root
HOSTS="138.68.189.32"
SCRIPT=" cd tasksAPIClass;git pull ;docker-compose down; docker-compose -d up --build"
for HOSTNAME in ${HOSTS} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done