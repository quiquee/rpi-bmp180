# rpi-bmp108
Run it exposing the host i2c interface as this:
docker run -t -i --device=/dev/i2c-1 -p 8888:888  <image> 
