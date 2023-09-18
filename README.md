# Hadoop Ecosystem Inside Docker

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