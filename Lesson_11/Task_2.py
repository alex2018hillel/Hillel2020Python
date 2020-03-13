import configparser

class Switch:

    def __init__(self,unit_name, mac_address, ip_address, login, password):
        self.parser = configparser.ConfigParser()
        self.parser.read('simple_config.ini')
        self.unit_name = unit_name
        self.mac_address = mac_address
        self.ip_address = ip_address
        self.login = login
        self.password = password

    @property
    def unit_name(self):
        print("Getting value")
        return self._unit_name

    @unit_name.setter
    def unit_name(self, value):
        if value == 'name':
            value = self.parser.get('data', 'unit_name')
            self._unit_name = value
        else:
            self._unit_name = value
    """"""
    @property
    def mac_address(self):
        print("Getting value")
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        self._mac_address = value
    """"""
    @property
    def ip_address(self):
        print("Getting value")
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value
    """"""
    @property
    def login(self):
        print("Getting value")
        return self._login

    @login.setter
    def login(self, value):
        self._login = value
    """"""
    @property
    def password(self):
        print("Getting value")
        return self._password

    @password.setter
    def password(self, value):
        if value == 'password':
            value = self.parser.get('data', 'password')
            self._password = value
        else:
            self._password = value

switch = Switch('name','12345678','192.168.11.24','2020hillel','password')
switch.mac_address = "111111111"
switch.ip_address = "192.168.00.25"
switch.login = "2222222222"

print(switch.unit_name)
print(switch.mac_address)
print(switch.ip_address)
print(switch.login)
print(switch.password)
print('-----------------------------')

switch = Switch('Piter','12345678','192.168.11.24','2020hillel','abrakadabra')
print(switch.unit_name)
print(switch.mac_address)
print(switch.ip_address)
print(switch.login)
print(switch.password)
