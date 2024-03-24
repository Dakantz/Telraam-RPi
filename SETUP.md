## Setup for wired connection

### Install dependencies

```bash
sudo apt install libopenblas-dev libatlas-base-dev python3-libcamera python3-kms++ python3-pyqt5 python3-prctl libatlas-base-dev ffmpeg python3-pip libcap-dev qtbase5-dev python3-picamera2
```

### Create and install python libraries

<!-- 
> DOES NOT WORK AS PyQT is currently broken, install using apt - picamera2 is a piece of s**t -->
```bash
python3 -m venv venv-telraam
source --system-site-packages venv-telraam/bin/activate
pip install --prefer-binary -r requirements.txt
```


### Find the ID for the interface you will run on

Run (replace `eth0` with the interface you will use):
```bash
source venv-telraam/bin/activate
python Access-point/telraam_generate_id.py --interface eth0
```
Should output something like:
```
Calculating id for eth0
2024-8158-8434-153QH
```
You can copy that ID and use it to register your device. Copy that  

### Configure Services

* Modify `Image-Processing/telraam_monitoring.service` to reflect the correct user directories
* Copy and start the service:
```bash
sudo cp Image-processing/telraam_monitoring.service /etc/systemd/system/telraam_monitoring.service 
sudo systemctl daemon-reload
sudo systemctl start telraam_monitoring.service
#monitor
sudo systemctl status telraam_monitoring.service
```