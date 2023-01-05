from django.shortcuts import render
from django.views import View
from django.http import request
from .models import Benh, TrieuChung,User, BenhAn
from .ultils import cbr
import datetime
from  django.utils import timezone
from django.contrib import sessions
# Create your views here.

def TrangChu(request):
    if(request.POST):
        email = request.POST["email"];
        matkhau = request.POST["matkhau"]\

        try:
            user = User.objects.get(email=email, matkhau=matkhau)
            request.session["id"] = user.id
            request.session["ten"] = user.ten
            list_tc = TrieuChung.objects.all().order_by("ki_hieu")
            context = {"list_tc": list_tc, "user": user.ten}
            return render(request, "TrangChu.html", context)
        except Exception:
            return render(request, "Dangnhap.html", {"err": " Tài khoản hoặc mật khẩu không chính xác"})
    else:
        list_tc = TrieuChung.objects.all().order_by("ki_hieu")
        context = {"list_tc": list_tc, "user": request.session["ten"]}
        return render(request, "TrangChu.html", context)

def KetQua(request):
    vote = {
    'p01' : request.POST['p01'],
    'p02' : request.POST['p02'],
    'p03' : request.POST['p03'],
    'p04' : request.POST['p04'],
    'p05' : request.POST['p05'],
    'p06' : request.POST['p06'],
    'p07' : request.POST['p07'],
    'p08' : request.POST['p08'],
    'p09' : request.POST['p09'],
    'p10' : request.POST['p10'],
    'p11' : request.POST['p11'],
    'p12' : request.POST['p12'],
    'p13' : request.POST['p13'],
    'p14' : request.POST['p14'],
    'p15' : request.POST['p15'],
    'p16' : request.POST['p16'],
    'p17' : request.POST['p17'],
    'p18' : request.POST['p18'],
    'p19' : request.POST['p19'],
    'p20' : request.POST['p20'],
    'p21' : request.POST['p21'],
    'p22' : request.POST['p22'],
    'p23' : request.POST['p23'],
    'p24' : request.POST['p24']
    }
    tennguoidung = request.session["ten"]
    user_id = request.session["id"]
    list_kq = []
    for value in vote.values():
        list_kq.append(float(value))
    index = cbr(list_kq)
    benhan = BenhAn(user = User.objects.get(pk = user_id),tenbenh = Benh.objects.get(pk = index).ten_benh, ngaychuandoan = timezone.now() )
    benhan.save()
    context = {"result": Benh.objects.get(pk = index), "user": tennguoidung}
    return render(request, "KetQua.html", context)

def DangNhap(request):
    return render(request, "Dangnhap.html",{"err": ""})

def gdBenhAn(request):
    user_id = request.session["id"]
    user = User.objects.get(pk = user_id)
    list_benhan = user.benhan_set.all()
    context = {"list_benhan": list_benhan,
               "user": request.session["ten"]}
    return render(request, "BenhAn.html", context)

def dangki(request):
    if (request.POST):
        email = request.POST["email"]
        matkhau = request.POST["matkhau"]
        matkhau2 = request.POST["matkhau2"]
        ten = request.POST["ten"]
        err = ""
        try:
            user = User.objects.get(email=email)
            err = "Email đã trùng"
            return render(request, "Dangki.html", {"err": err})
        except Exception:
            user = User(ten= ten, email= email, matkhau= matkhau)
            user.save()
            return render(request, "Dangnhap.html")
    else:
        return render(request, "Dangki.html")
