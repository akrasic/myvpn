myvpn - Simple VPN connection manager

Supports OpenVPN connection ATM.

**Installation** 
Clone this repository and install via running:

```bash
python setup.py install
```
**Configuration** 
myvpn uses ``~/.myvpn/`` directory to read the VPN configuration files.
It runs the openvpn process through sudo privilege so make sure you have the
sudo password stored inside ``~/.myvpn/.sudo`` file. 

**Usage** 
To connect to your profile:
``myvpn --profile profile1``

myvpn will read following OVPN file:
``~/.myvpn/profile1/profile1.ovpn``

Make sure that the OVPN file has the correct paths to the CA certificate and
user keys. If you would like to have the CA key and user certificate and key in the OVPN file I would suggest reading up on http://www.brainfart.sg/index.php/2012/05/embedding-certificate-into-openvpn-config/ .

