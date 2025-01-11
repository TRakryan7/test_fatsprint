from django.db import models
from .kategori import Kategori
from .status import Status

class Produk(models.Model):
    nama_produk = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='produk')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='produk')

    def __str__(self):
        return self.nama_produk