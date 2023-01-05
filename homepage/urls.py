from django.urls import path
from . import views
app_name = "homepage"
urlpatterns = [
    path('', views.DangNhap, name = "dangnhap"),
    path('trangchu/', views.TrangChu, name = "trangchu"),
    path("result/", views.KetQua, name = 'ketqua' ),
    path("history/", views.gdBenhAn, name = "benhan"),
    path("dangki/", views.dangki, name = "dangki")
]
