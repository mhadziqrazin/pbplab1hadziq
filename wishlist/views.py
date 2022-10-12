from curses.ascii import HT
from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Hadziq',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "wishlist.html", context)

@login_required(login_url='/wishlist/login/')
def wishlist_ajax(request):
    context = {
        'nama': 'Hadziq',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "wishlist_ajax.html", context)
    # data_barang_wishlist = BarangWishlist.objects.all()
    # context = {
    #     'list_barang': data_barang_wishlist,
    #     'nama': 'Hadziq',
    #     'last_login': request.COOKIES['last_login'],
    # }


@login_required(login_url='/wishlist/login/')
def get_wishlist_ajax(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize('json', data_barang_wishlist))

@login_required(login_url="/wishlist/login/")
def add_wishlist(request):
    if request.method == 'POST':
        nama_barang = request.POST.get('nama_barang')
        harga = request.POST.get('harga')
        deskripsi = request.POST.get('deskripsi')
        new_barang = BarangWishlist(
            nama_barang = nama_barang,
            harga_barang = harga,
            deskripsi = deskripsi,
        )
        new_barang.save()
        return HttpResponse(b"Created", status=201)
    return HttpResponseNotFound()
    # if request.method == "POST":
    #     nama_barang = request.POST.get('nama_barang')
    #     harga = request.POST.get('harga')
    #     deskripsi = request.POST.get('deskripsi')
    #     new_barang = BarangWishlist(
    #         nama_barang = nama_barang,
    #         harga_barang = harga,
    #         deskripsi = deskripsi,
    #     )
    #     new_barang.save()
    #     data_barang_wishlist = BarangWishlist.objects.all()
    # return HttpResponse(b"Created", status=201)
    # return redirect('wishlist:wishlist_ajax')


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login')
    return response
    
def show_wishlist_xml(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_wishlist_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
