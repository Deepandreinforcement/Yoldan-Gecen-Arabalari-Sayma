Burada arabaları saymak için basit bir yol kullanılıyor. 
Normalde object tracking (nesne takibi) tarzı algroitmalar kullanılır bu tarz görevler için. 
Fakat ben burada küçük bir model kullandım videonun fps'i yüksek olsun diye. 
Bu modelde object tracking çok da iyi sonuçlar vermiyor. Ben de kendi yöntemimi geliştirdim.
Yolun solundaki arabalar griş sağındaki arabalar çıkış yapıyor. 
Normalde tam tersi olur fakat bulduğum videoda trafik tersten akıyor. 
Burada şöye bir yöntem var. Giriş yapan arabaları bulmak için yolun solunda bir hayali dikdörtgen oluşturdum. 
Giriş yapan arabalar genelde buradan bir kere geçiyor. Tabi bunu özel ayarladım. 
Burada araba bu dikdörtgenin içinde olursa giriş değişkenini bir arttıyorum. 
Aynı şeyi uygun şekilde çıkış yapan arabalar için de yapıyorum. Orada sağ tarafta bir dikdörtfen ayarladım. 
Bu dikdörtgenler if kodları ile yaplıyor. 
Bu yöntemde video değişirse yani yeni bir yol olursa o zaman o yol için yeni bir ayarlama yapmak gerekebilir. 
Fakat video ve kamera konumu değişmezse kodda değişikliğe gerek kalmadan algoritma yüksek doğrulukla çalışıyor.

Ben bu algoritmayı 3 farklı  videoda denedim. Gayet güzel çalıştı. 
Tabi videoya uygun konum değişikşikleri yaptım. 

Bu arada bu algoritma ile kadraja giren ve çıkan insan insan sayısını bulma yapılmaz.
Çünkü arabalar yolun sağından girip yolun solundan çıkar. Bu videoda trafik ters aktığı için bunun tersi söz konusu.
Fakat insanlar için böyle bir durum söz konusu değil. 


Kullandığım videonun boyutu yüksek o yüzden yüklemedim. Videonun linki:
https://www.youtube.com/watch?v=wqctLW0Hb_0&t=4s
