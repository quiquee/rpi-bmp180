FROM hypriot/rpi-python
MAINTAINER <blgulla@ncsu.edu>


RUN apt-get update; apt-get install -y git build-essential python-dev python-smbus 
RUN git clone https://github.com/adafruit/Adafruit_Python_BMP.git /data/adafruit ; cd /data/adafruit; python setup.py install
RUN pip install Flask

CMD ["python","/data/adafruit//examples/simpletest.py"]
