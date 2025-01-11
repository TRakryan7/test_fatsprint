from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..models import Produk, Status, Kategori
from ..forms import ProdukForm
from ..helper import helper

def produk_list(request):
    produk = Produk.objects.filter(status_id=39).select_related('status').select_related('kategori').values('id', 'nama_produk', 'harga', 'status__nama_status', 'kategori__nama_kategori')
    # print("product", produk)
    return render(request, 'produk_list.html', {'produk': produk})

def produk_generate(request):
    produk = Produk.objects.select_related('status').select_related('kategori').values('id', 'nama_produk', 'harga', 'status__nama_status', 'kategori__nama_kategori')
    if produk.exists() is False :
        data = helper.get_data()
        loop_data = data['data']
        statuses = set(item["status"] for item in loop_data)
        categories = set(item["kategori"] for item in loop_data)
        
        formated_status = [{"nama_status": status} for status in statuses]
        formated_kategori = [{"nama_kategori": kategori} for kategori in categories]
        
        obj_status = [Status(nama_status=item["nama_status"]) for item in formated_status]
        obj_kategori = [Kategori(nama_kategori=item["nama_kategori"]) for item in formated_kategori]
        Status.objects.bulk_create(obj_status)
        Kategori.objects.bulk_create(obj_kategori)
        status = Status.objects.all().values()
        kategori = Kategori.objects.all().values()
        
        obj_produk = [
            Produk(
                nama_produk=item['nama_produk'],
                harga=item['harga'],
                status_id=next((i['id'] for i in status if i['nama_status'] == item['status']), None),
                kategori_id=next((i['id'] for i in kategori if i['nama_kategori'] == item['kategori']), None)
            )
            for item in loop_data
        ]
        
        Produk.objects.bulk_create(obj_produk)
        produk = Produk.objects.select_related('status').select_related('kategori').values('id', 'nama_produk', 'harga', 'status__nama_status', 'kategori__nama_kategori')
        messages.success(request, f"Produk berhasil digenerate.")
    return render(request, 'produk_list.html', {'produk': produk})
    #print(data['data'])

def produk_create(request):
    kategori = Kategori.objects.all().values()
    status = Status.objects.all().values()
    
    return render(request, 'produk_create.html', {'kategori':kategori, "status":status})

def produk_save(request):
    if request.method == 'POST':
        print("methode",request.POST['nama_produk'])
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Produk berhasil dibuat.")
            return redirect('produk-list')
    else:
        form = ProdukForm()
    return render(request, 'produk_create.html', {'form': form})

def produk_edit(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    status = Status.objects.all().values()
    messages.success(request, f"Produk {produk.nama_produk} berhasil Edit.")
    kategori = Kategori.objects.all().values()
    return render(request, 'produk_edit.html', {'kategori':kategori, "status":status, "produk":produk})

def produk_update(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('produk-list')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'produk_form.html', {'form': form})

def produk_delete(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        produk.delete()
        messages.success(request, f"Produk {produk.nama_produk} berhasil dihapus.")
        return redirect('produk-list')
    return render(request, 'produk_confirm_delete.html', {'produk': produk})