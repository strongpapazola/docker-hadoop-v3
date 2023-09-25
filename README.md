# Hadoop Ecosystem Inside Docker

## Installasi Di Ubuntu 22.04
<pre>
sudo bash
apt update
apt install docker.io curl git -y
VERSION=$(curl --silent https://api.github.com/repos/docker/compose/releases/latest | grep -Po '"tag_name": "\K.*\d')
DESTINATION=/usr/bin/docker-compose
curl -L https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-$(uname -s)-$(uname -m) -o $DESTINATION
chmod 755 $DESTINATION
git clone https://github.com/strongpapazola/docker-hadoop-v3
cd docker-hadoop-v3
docker-compose up -d --force-recreate
</pre>

## Penjelasan Folder
- Folder Ini Merupakan Template Dasar Aplikasi Aplikasi Lainnya
<pre>
base/
</pre>

- Folder Ini Merupakan Komponen Dari Aplikasi Hadoop Itu Sendiri
<pre>
namenode/
datanode/
nodemanager/
resourcemanager/
historyserver/
</pre>

- Folder Ini Merupakan Komponen Spark
<pre>
spark-master
spark-worker
</pre>

- File Ini Merupakan Installer Semua Ecosystem
<pre>
docker-compose.yml
</pre>

- File Ini Test Jobs Hadoop Dan Spark
<pre>
spark-examples/ <-- Spark Example
mapreduce-compose.yml <-- Hadoop Yarn Example
</pre>

- Script Untuk Build Jika Ada Perubahan
<pre>
./build.sh
</pre>

- Script Untuk Clear Semua Data Termasuk Aplikasi Agar Fresh
<pre>
./clean.sh
</pre>

- Sample Aplikasi Yang Bisa Di Integrasikan
<pre>
apps-sample/
</pre>
