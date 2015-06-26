# proximity-py

## 1. Requirements
Program was tested on **Ubuntu 14.04 Python 3.4** but should work on other operating systems as well.

## 2. Installation
### 2.1. Installation using virtualenv
```
#Install virtual env
apt-get install python-virtualenv
#Create virtualenv
virtualenv -p python3.4 venv
#Activate virtualenv
source venv/bin/activate
#Install required projects
pip install pyqtgraph pyserial
```
And you're ready to go.

## 3. Execution
Sometimes to access UART port you have to run program from root
```
sudo python main.py
```