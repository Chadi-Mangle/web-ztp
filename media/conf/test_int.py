import socket
import fcntl
import struct

class DHCPBroadcastListener:
    def __init__(self, bind_port=67, buffer_size=1024):
        self.bind_port = bind_port
        self.buffer_size = buffer_size

    def get_interface_ip(self, interface_name):
        """ Récupère l'adresse IP associée à une interface réseau """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR (Get interface address)
                struct.pack('256s', bytes(interface_name[:15], 'utf-8'))
            )[20:24])
        except OSError:
            return None

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            
            # Vérifier si IP_PKTINFO est supporté
            if hasattr(socket, "IP_PKTINFO"):
                s.setsockopt(socket.IPPROTO_IP, socket.IP_PKTINFO, 1)
                print("Using IP_PKTINFO for metadata extraction.")

            s.bind(("", self.bind_port))
            print(f"Serveur en écoute sur le port {self.bind_port}...")

            while True:
                data, ancdata, msg_flags, addr = s.recvmsg(self.buffer_size, 1024)
                
                print(f"Paquet reçu de {addr}, données: {data}")

                if not ancdata:
                    print("⚠️ Aucun `ancdata` reçu ! Vérifiez votre système.")

                for cmsg_level, cmsg_type, cmsg_data in ancdata:
                    if cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SO_BINDTODEVICE:
                        interface_name = cmsg_data.decode("utf-8").strip("\x00")
                        print(f"Paquet reçu sur l'interface : {interface_name}")

                        # Obtenir l'adresse IP associée
                        interface_ip = self.get_interface_ip(interface_name)
                        if interface_ip:
                            print(f"Adresse IP associée à {interface_name} : {interface_ip}")

if __name__ == "__main__":
    dhcp_listener = DHCPBroadcastListener()
    dhcp_listener.run()
