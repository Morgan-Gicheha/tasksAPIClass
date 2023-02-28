

USERNAME=root
HOSTS="138.68.189.32"
SCRIPT=" cd tasksAPIClass;git pull ;docker-compose down; docker-compose up --build -d"
for HOSTNAME in ${HOSTS} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done
//morgan
