from django.db import models

from django.db import models

class Template(models.Model):
    """Modèle de données pour un template de configuration ZTP"""
    file_path = models.CharField(max_length=255)

    def __str__(self):
        return str(self.file_path)

class Device(models.Model):
    """Modèle de données pour une machine à configurer"""
    serial_number = models.CharField(max_length=255)
    ip = models.GenericIPAddressField(unique=True)
    hostname = models.CharField(max_length=255, null=True, blank=True)
    interface = models.CharField(max_length=255, null=True, blank=True)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, related_name="devices")

    class Meta:
        unique_together = ('serial_number', 'interface')

    def __str__(self):
        return f"{self.hostname} ({self.ip})"

class DHCPConfig(models.Model):
    """Modèle de données pour une configuration DHCP"""
    subnet = models.GenericIPAddressField()
    min_ip_pool = models.GenericIPAddressField()
    max_ip_pool = models.GenericIPAddressField()

    def __str__(self):
        return f"DHCP: {self.subnet}"
