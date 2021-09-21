### Para instalar `javac`
```
yum install java-1.8.0-openjdk-devel
```

### Tras instalar `openjdk`
Incluso si instalamos la versión 1.7 se instalará la versión 1.8. Hemos de cambiar los paths a las versión 1.8 para que funciona correctamente:
```
export JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk
```

Editamos el archivo `/opt/hadoop/etc/hadoop/hadoop.env.sh`:
```
export JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk
```

### Para compilar
(Gloria): Dentro de hdfs (dentro de opt/hadoop):

```
sudo bash run.sh WordCount
```

# Para ejecutar

Primero hay que iniciar el NameNode y el DataNode:
```
sbin/start-dfs.sh
```

Iniciar el ResourceManager y el NodeManager:
```
sbin/start-yarn.sh
```

Recuerda que hemos de subir el archivo utilizando:
```
/opt/hadoop/bin/hdfs dfs -put Quijote.txt /user/root
```

Lanzamos nuestro trabajo de MapReduce:

```
sudo /opt/hadoop/bin/hadoop jar WordCount.jar uam.WordCount Quijote.txt output/
```