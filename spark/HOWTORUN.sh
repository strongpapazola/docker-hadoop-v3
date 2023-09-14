sqoop import --connect jdbc:mysql://bigdata.bisa.ai:3306/barang --username root --password passwordaman --table barang --target-dir /user/hadoop/barang --fields-terminated-by ',' --num-mappers 1 --driver com.mysql.cj.jdbc.Driver
sqoop import --connect jdbc:mysql://bigdata.bisa.ai:3306/barang --username root --password passwordaman --table barang --target-dir /user/hadoop/barang
sqoop import --connect jdbc:mysql://bigdata.bisa.ai:3306/barang --username root --password passwordaman --table barang --target-dir /user/hadoop/barang3 --driver com.mysql.cj.jdbc.Driver

hadoop fs -rm -r /barang && sqoop import --connect jdbc:mysql://bigdata.bisa.ai:3306/barang --username root --password passwordaman --table barang --target-dir /barang --driver com.mysql.cj.jdbc.Driver