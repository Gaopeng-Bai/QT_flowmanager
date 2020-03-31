# Own_flowmanager

This project is a GUI client access ryu network manager to control the flows in the swithes networks. By default, using mininet to simulate the swithes network.

Basically, this programm can run any OS but must be with docker env as blow. Otherwise, you must build mininet environment on VM or linux OS.
## 1. Build ryu manager (docker).
* Pull ryu manager image.
    ```
    docker pull osrg/ryu
    ```
* Build a container for this
    ```
    docker run -it --rm -p 6633:8080 -v {the path of your code on local os}:/root/project osrg/ryu /bin/bash
  ```
  (eg path: /d/Technology/Python_project/Tools/Own_flowmanager/server_flows)
* check ip address for mininet
    ```
    ip addr show eth0
    ```
    (eg.. 170.17.0.2)
* Run your ryu-manager.
    ```
    cd project
    ryu-manager {filename in the path of your code}.py        
    ```
## 2. Build mininet (docker).
* Under docker-mininet file, run command:
    ```
    docker-compose run --rm mininet
    ```
    If issue appear, reboot docker host try to solve it.
* create a switches network.
    ```
    mn --controller remote,ip={ryu manager ip above}  --switch ovsk,protocols=OpenFlow13 --mac --ipbase=10.1.1.0/24 --topo single,4
    ```
## 3. Run this programm on your python interpreter.
```
python Main.py
```
Change the server ip and port to connect ryu server. By default if using docker: 
```
IP: 127.0.0.1
Port: 6633
```