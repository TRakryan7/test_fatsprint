from rest_framework import serializers
from .models import Produk, Kategori, Status

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id','nama_kategori']
        
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id','nama_status']
        
class ProdukSerializer(serializers.ModelSerializer):
    kategori = KategoriSerializer(read_only=True) 
    status = StatusSerializer(read_only=True)     
    kategori_id = serializers.PrimaryKeyRelatedField(
        queryset=Kategori.objects.all(),
        source='kategori',
        write_only=True
    )  # Untuk input kategori
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(),
        source='status',
        write_only=True
    )  # Untuk input status

    class Meta:
        model = Produk
        fields = ['id', 'nama_produk', 'harga', 'kategori', 'status', 'kategori_id', 'status_id']