from django.db import models

# Create your models here.
class BarangWishlist(models.Model):
    nama_barang = models.CharField(max_length=50)
    harga_barang = models.IntegerField()
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_barang