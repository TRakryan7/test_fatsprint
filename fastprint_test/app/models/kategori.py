from django.db import models

class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=225)
    
    def __str__(self):
        return self.nama_kategori