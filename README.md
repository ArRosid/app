# app

## run the backend
use operating system ami-01b479c50edc9aca5

### install python pip
yum install python3-pip -y

### install dependencies
pip3 install -r requirements.txt

### run the program
python3 app.py
access it via port 5000


## run the frontend
### install nodejs
yum install gcc-c++ make -y

curl -fsSL https://rpm.nodesource.com/setup_16.x | sudo -E bash -

yum install nodejs git -y


### install dependencies
npm install

### create .env file
VUE_APP_BACKEND_URL=http://backend_ip:5000

### run the program
npm run serve
access it via port 8080
