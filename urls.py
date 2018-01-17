from django.contrib.sitemaps.views import sitemap 
# urls.py için django sitemap fonksiyonunu ekledik.


from views import BlogSitemap # şeklinde views.py içindeki site harita sınıfımı çağırdım
# sizlerde import işlemleri urls.py ve views.py dosyalarının konumuna göre değişebilir
# bunu import etme kurallarını araştırıp sıkıntısız bir şekilde dahil edebilirsiniz


sitemaps = { 
    "blog":BlogSitemap(),
}
"""
sitemaps adında bir sözlük (dict) tipinde bir değişken açtık ve
az önce views.py de ayarladığımız blog site harita sınıfını "blog" şeklinde sözlüğümüze gönderdik 
eğer birden fazla site haritası ekleyecekseniz yine views.py de az önce yaptığımız işlemleri başka eklemek istediğiniz model sınıfınızı dahil ederek ayarlayıp o sınıfı urls.py içine çağırarak ( import ederek ) sitemaps sözlüğüne eklemeniz yetecektir. 
 """

urlpatterns = [
    url(r'^$', home,name = "home"),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
    # son olarak burada sitemap.xml adres kısmını oluşturduk ve django nun sitemap 
    # fonksiyonunu koyduk ikinci paramatere olarak
    # daha sonra {'sitemaps': sitemaps} şu sözlük ile de yukarıda oluşturduğumuz sitemaps
    # oluşturduğum sitemap sınıflarını gönderdim ve işlem bitti hepsi bu kadar

]
