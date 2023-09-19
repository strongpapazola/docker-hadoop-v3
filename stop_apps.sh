docker rm -f nodemanager
docker rm -f resourcemanager
docker rm -f namenode
docker rm -f datanode
docker rm -f datanode1
docker rm -f historyserver
docker rm -f spark-worker-1
docker rm -f spark-master

docker ps --all 
