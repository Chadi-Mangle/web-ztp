from app.models import DHCPConfig

def get_dhcp_config():
    """Récupère les informations du subnet DHCP et du pool d'adresses IP."""
    config = DHCPConfig.objects.first()
    return config



#### Je garde les ancien fichier au cas ou

#from app.utils import device_utils, dhcp_utils

from app.utils.ip_address import IPAddress

class DHCPData:
    def __init__(self):
        self.subnet = self.get_subnet()
        self.min_ip_pool = self.get_min_ip_pool()
        self.max_ip_pool = self.get_max_ip_pool()
        self.server_ip = "10.30.31.30"


        self.generate_ip = self.get_ip_in_pool()

    def get_subnet(self) -> str:
        return self.get_dhcp_config().subnet

    def get_min_ip_pool(self) -> str:
        return self.get_dhcp_config().min_ip_pool

    def get_max_ip_pool(self) -> str:
        return self.get_dhcp_config().max_ip_pool

    def get_use_ip(self) -> set:
        return device_utils.get_used_ips()

    def get_bootfile(self, serial_number):
        return device_utils.get_template_url(serial_number)

    def get_ip_in_pool(self) -> str:
        ip_address = IPAddress(self.min_ip_pool)
        max_ip_address = IPAddress(self.max_ip_pool)

        if str(ip_address) not in self.get_use_ip():
            yield str(ip_address)

        while ip_address < max_ip_address:
            ip_address = ip_address.next()
            if str(ip_address) not in self.get_use_ip():
                yield str(ip_address)

    def add_device(self, serial_number: str, ip: str, hostname: str) -> None:
        device_utils.add_device(serial_number, ip, hostname)

    def get_ip(self, serial_number: str):
        if serial_number:
            device = device_utils.get_device_by_serial(serial_number)
            if device:
                return device
            try:
                return next(self.generate_ip)
            except StopIteration:
                self.generate_ip = self.get_ip_in_pool()
                try:
                    return next(self.generate_ip)
                except StopIteration:
                    return None