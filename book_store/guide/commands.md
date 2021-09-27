## To clone project
$git clone

## install virtual environment and requirements
$apt install python3.8-venv
$python3 -m venv env
$ pip install -r requirements.txt

## Run project
$ uvicorn book_store.main:app --reload

## docker setup
"""$sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
    """


$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
$  echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
$ sudo apt-get install docker-ce=5:20.10.8~3-0~ubuntu-focal docker-ce-cli=5:20.10.8~3-0~ubuntu-focal containerd.io
$ sudo chmod 666 /var/run/docker.sock
$ docker run -d --name book-store_container -p 80:80 book_store_image


##mongodb
$ wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
$ mongosh
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
