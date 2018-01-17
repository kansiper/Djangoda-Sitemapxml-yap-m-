from models import Blog
# model dosyamızdan Blog adlı sınıfı çağırıyoruz 
# Blog model sınıfını örnek için veriyorum siz içeriklerinizi hangi model sınıfında tutuyorsanız yanı 
# hangi model sınıfı için site haritası yapacaksanız onu çağırın 

from django.contrib.sitemaps import Sitemap
# django nun sitemap sınıfını çağırıyoruz




class BlogSitemap(Sitemap): 
# sınıf ismimizi verdik ve çağırdığımız Sitemap sınıfından miras alıyoruz

    changefreq = "daily" # bu değişkenimiz site haritasında yazacak olan ne 
                         # sıklıkla tarayacağı bilgisini yazar { daily always weekly }
                         # gibi seçenekler vardır araştırın
    priority = 1.0    # priority değişkenimiz tarama önceliğini arama motorlarına belirtir 
                      # 0.1 ,0.6 veya 1.0 gibi değerler verilebilir size kalmış

    def items(self):  # items fonksiyonu Blog nesnesindeki her öğeyi belirtir yani 
                      # item.url , veya item.time diyerel modelinize ait değişkenleri alabilirsiniz
        return Blog.objects.all()

    def lastmod(self,obj): # lastmod fonksiyonu içeriğinizin en son değiştirilme tarihini gösterir.
        return Blog.objects.filter(user = obj.user)[0].lastmod 
        # benim modelimde en son değişme tarihi bu şekilde kayıtlı 
        # olduğu için ben bu şekilde aldım , kullanıcının yazmış olduğu en 
        # son içerik tarihini alıyorum buda en son güncelleme zamanını vermiş oluyor ve bu bilgiyi return ile gönderiyorum

    def location(self,obj): # location fonksiyonu içerik adreslerinin tutulduğu yerdir
         return obj.url # items fonksiyonunda gönderdiğimiz model nesnemizin öğelerine erişmek için
            # (self,obj) şu parametreleri kullanıp obj değişkenindeki 
            # ( bu bizim çağırdığımız model oluyor ) ögelere erişebiliyoruz bende içerik adreseri 
            # Blog modelimde url değişkeninde olduğu için bu şekilde çağırdım.
