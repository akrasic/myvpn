myvpn - Simple VPN connection manager

**Installation**
Clone this repository and install via running:

```bash
python setup.py install
```

**Configuration**
myvpn uses ``~/.myvpn/`` directory to read the VPN configuration files.
It runs the openvpn process through sudo privilege so make sure you have the
sudo password stored inside ``~/.myvpn/.sudo`` file. 

** Usage **
To connect to your profile:
``myvpn profile1``

myvpn will read following OVPN file:
``~/.myvpn/profile1/profile1.ovpn``

Make sure that the OVPN file has the correct paths to the CA certificate and
user keys.

