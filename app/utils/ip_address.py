class IPAddress:
    def __init__(self, ip_address: str):
        self.ip_address = ip_address
        self.octets = list(map(int, self.ip_address.split(".")))

    def next(self):
        self.octets[3] = (self.octets[3] + 1) % 256
        i = 3

        while i > 0 and self.octets[i] == 0:
            self.octets[i - 1] = (self.octets[i - 1] + 1) % 256
            i -= 1

        return IPAddress(".".join(map(str, self.octets)))

    def __lt__(self, other):
        for i in range(4):
            if self.octets[i] != other.octets[i]:
                return self.octets[i] < other.octets[i]
        return False

    def __str__(self):
        return self.ip_address
