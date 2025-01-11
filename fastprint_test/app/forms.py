from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']

    def clean_harga(self):
        harga = self.cleaned_data.get('harga')
        if harga <= 0:
            raise forms.ValidationError("Harga harus lebih besar dari 0.")
        return harga