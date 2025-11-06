# Temel Matematiksel Operatörler
a=36
b=23
c=a+b
print("Toplam:",c)

print(a-b)
print(a*b)
print(a/b)
print(a%b) #Kalanı verir 
print(a**b) #Üs alma işlemi
print(a//b) #Tam sayı bölme

# Değişkenler ve Veri Tipleri
ad ="Ecem Nur"
soyad ="Özen"
print("Ad:",ad)
print("Soyad:",soyad)
print("Ad Soyad:",ad,soyad)
print(f"Benim adım {ad} ve soyadım {soyad}") #f-string kullanımı

# String Metotları
metin="Python programlama dili çok eğlenceli!"
upper_metin=metin.upper() #büyük harfe çevirir
lower_metin=metin.lower() #küçük harfe çevirir
print("Büyük Harf:",upper_metin)
print("Küçük Harf:",lower_metin)
print(metin.replace("eğlenceli","harika")) #kelime değiştirme

# Koşul İfadeleri
yas=21 
if yas<18: #girinti : ile oluşturuyoruz.
    print("Reşit değilsiniz.")
elif yas==18:
    print("Yeni reşit oldunuz.")
else:
    print("Reşitsiniz.")

# Döngüler
for i in range(5): #0'dan 4'e kadar sayılar index 0 dan başlar.
    print("Sayı:",i) 

#Diziler üzerinde for döngüsü
meyveler=["elma","muz","çilek"]
for meyve in meyveler:
    print("Meyve:",meyve)

#for döngüsünden çıkıp while döngüsüne geçiş
sayac=0
while sayac<5:
    print("Sayaç:",sayac)
    sayac+=1 #sayacı 1 artırır sayacımın değeri 5 olana kadar döngü devam eder.

for sayi in range(1,21): #(1,20,(2)) mesela kaçar kaçar artmasını istiyorsak 3. parametreyi ekleyebiliriz.
    if sayi%2==0:
        print("Çift Sayı:",sayi)
    else:
        print("Tek Sayı:",sayi)


# Liste ve Sözlükler
notlar=[85,90,78,92,88] 
print(type(notlar)) #liste türünü gösterir
print("Notlar:",notlar)
notlar.append(95) #listeye eleman ekleme
print("Güncellenmiş Notlar:",notlar)
notlar.remove(78) #listeden eleman çıkarma
print("Güncellenmiş Notlar:",notlar)

ogrenci={"ad":"Ecem Nur","soyad":"Özen","yas":21}
print(type(ogrenci)) #sözlük türünü gösterir
print("Öğrenci Bilgileri:",ogrenci)
print("Ad:",ogrenci["ad"]) #sözlükten ad bilgisini alma
ogrenci["yas"]=22 #sözlükteki yaşı güncelleme
print("Güncellenmiş Öğrenci Bilgileri:",ogrenci)


koordinatlar=(10,20) #tuple
print(type(koordinatlar))
print("Koordinatlar:",koordinatlar)

set_meyveler={"elma","muz","çilek"} #set benzersiz elemanlar tutar
print(type(set_meyveler))
print("Meyveler Seti:",set_meyveler)