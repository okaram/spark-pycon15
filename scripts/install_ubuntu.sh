sudo apt-get update
sudo apt-get install -y git

# install geany with terminal emulator (feel free to comment if prefer favorite editor)
sudo apt-get install -y geany libvte-dev

wget http://d3kbcqa49mib13.cloudfront.net/spark-1.3.0-bin-hadoop2.4.tgz

mkdir spark
cd spark
tar -xzvf ../spark-1.3.0-bin-hadoop2.4.tgz
rm ../spark-1.3.0-bin-hadoop2.4.tgz
mv spark-1.3.0-bin-hadoop2.4 spark
# get a useful log4j.properties
curl https://raw.githubusercontent.com/okaram/spark-pycon15/master/scripts/log4j.properties > spark/conf/log4j.properties

git clone https://github.com/okaram/spark-pycon15

# install java from David Branner
curl -L --cookie "oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u40-b26/jdk-8u40-linux-x64.tar.gz -o jdk-8u40-linux-x64.tar.gz
tar -xvf jdk-8u40-linux-x64.tar.gz

sudo mkdir -p /usr/lib/jvm
sudo mv ./jdk1.8.0_40* /usr/lib/jvm/

sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.8.0_40/bin/java" 1
sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.8.0_40/bin/javac" 1
sudo update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/lib/jvm/jdk1.8.0_40/bin/javaws" 1

sudo chmod a+x /usr/bin/java 
sudo chmod a+x /usr/bin/javac 
sudo chmod a+x /usr/bin/javaws
sudo chown -R root:root /usr/lib/jvm/jdk1.8.0_40

rm jdk-8u40-linux-x64.tar.gz
