
hesapmakinesi = """
(1) Toplama İşlemi\t +

(2) Çıkarma İşlemi\t -

(3) Çarpma İşlemi\t *

(4) Bölme İşlemi\t /
"""
print(hesapmakinesi)

while True:
    soru = input(
        "Yapmak İstediğiniz işlemin numarasını lütfen yazınız 1-4 Hesap Makinesinden Çıkış Yapabilmek İçin Çıkış Yazmalısın\t")
    if soru == "Çıkış":
        print("Hesap Makinesinden başarıyla çıkış yapılmıştır iyi günler.")
        break
    elif soru == "1":
        num = input("İlk sayıyı giriniz:\t")
        num1 = input("İkinci sayıyı giriniz:\t")
        try:
            num = int(num)
            num1 = int(num1)
            print(num+num1)
            print("İşleminiz Başarılı!")
        except ValueError:
            print("Lütfen sadece sayı giriniz!!!")
    elif soru == "2":
        c1 = input("İlk sayıyı giriniz:\t")
        c2 = input("İkinci sayıyı giriniz:\t")
        try:
            c_1 = int(c1)
            c_2 = int(c2)
            print(c_1-c_2)
            print("İşleminiz Başarılı!")
        except ValueError:
            print("Lütfen sadece sayı giriniz!!!")
    elif soru == "3":
        p1 = input("İlk sayıyı giriniz:\t")
        p2 = input("İkinci sayıyı giriniz:\t")
        try:
            p_1 = int(p1)
            p_2 = int(p2)
            print(p_1*p_2)
            print("İşleminiz Başarılı!")
        except ValueError:
            print("Lütfen sadece sayı giriniz!!!")
    elif soru == "4":
        p1 = input("İlk sayıyı giriniz:\t")
        p2 = input("İkinci sayıyı giriniz:\t")
        try:
            p_1 = int(p1)
            p_2 = int(p2)
            print(p_1/p_2)
            print("İşleminiz Başarılı!")
        except ValueError:
            print("Lütfen sadece sayı giriniz!!!")
