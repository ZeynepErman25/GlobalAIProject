#https://www.linkedin.com/in/zeyneperman/
#Zeynep Erman

#kodda kullanacağımız modüllerin aktarımı
#csv kullanıcı bilgilerini depolamada kullanılacak
#datetime ana menüde tarih göstermek için kullanılacak
import csv
import datetime

#Pizza çeşitlerimizin özelliklerini alacağı bir pizza üst sınıfı
class Pizza:
    def __init__(self,description,cost):
        self.description = description
        self.cost = cost


    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

#Pizza çeşitlerinin tanımlanması
#Pizzaların özellikleri ve fiyatları
class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza: domates, mozarella, fesleğen ", 40.0)

class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza: ekstra mozarella  ", 45.0)

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Türk Pizzası: kıyma, soğan ", 35.0)

class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza: domates, biber", 30.0)

#Seçilecek ekstra sos malzemeleri için Pizza üst sınıfına bağlı bir sos üst sınıfı
class Decorator(Pizza):
    def __init__(self, component, description, cost):
        self.component = component
        super().__init__(description,cost)

    def get_cost(self):
        return self.component.get_cost() + \
            Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
        ' ' + Pizza.get_description(self)

#Ekstra malzeme seçeneklerinin olduğu alt sınıflar
#Ekstra malzeme çeşidine göre fiyata eklenen ücretler
class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component, ' + ekstra zeytin', 3.0)


class Mantar(Decorator):
    def __init__(self, component):
        super().__init__(component,' + ekstra mantar', 2.5)


class KeciPeynir(Decorator):
    def __init__(self, component):
        super().__init__(component,' + ekstra keçi peyniri', 4.0)

class Et(Decorator):
    def __init__(self, component):
        super().__init__(component,' + et sosu', 5.0)

class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component,' + ekstra soğan', 2.5)

class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component, ' + ekstra mısır', 2.5)

#Ana menüde tarihin görünmesi için tanımlanan bir method
def tarih():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#Ana menünüyü ve kullanıcı seçimlerini kapsayan main methodu
def main():
    tarih()
    menu = open("Menu.txt", "r", encoding="utf-8")
    ana_menu = menu.read()
    print(ana_menu)

    taban = int(input("Lütfen Pizzanızı seçiniz: (1-4)"))
    while taban < 1 or taban > 4:
        print('Geçersiz seçim. Lütfen 1-4 arasında bir sayı giriniz.')
        taban = int(input("Lütfen Pizzanızı seçiniz: (1-4)"))

    if taban == 1:
        pizza = KlasikPizza()
    elif taban == 2:
        pizza = MargaritaPizza()
    elif taban == 3:
        pizza = TurkPizza()
    else:
        pizza = SadePizza()

    sos_secimi = int(input("Lütfen Sos malzemenizi seçiniz: (1-6)"))
    while sos_secimi < 1 or sos_secimi > 6:
        print('Geçersiz seçim. Lütfen 1-6 arasında bir sayı giriniz.')
        sos_secimi = int(input("Lütfen Sos malzemenizi seçiniz: (1-6)"))

    if sos_secimi == 1:
        sos = Zeytin(pizza)
    elif sos_secimi == 2:
        sos = Mantar(pizza)
    elif sos_secimi == 3:
        sos = KeciPeynir(pizza)
    elif sos_secimi == 4:
        sos = Et(pizza)
    elif sos_secimi == 5:
        sos = Sogan(pizza)
    else:
        sos = Misir(pizza)

#Kullanıcının seçtiği pizza bilgilerinin bastırılması
    print(f"Pizza seçiminiz: {sos.get_description()}")
    toplam_fiyat = str(sos.get_cost())
    print(f"Pizzanız {toplam_fiyat} TL'dir. ")

#Kullanıcının siparişi onaylamasına göre aktive olacak kullanıcı bilgileri kısmı
#Kimlik kartı, kredi kartı numaralarının ve kart şifresinin uygun uzunlukta olduğunu kontrol ediyor.
    sipariş_onayı = str(input("Siparişinizi onaylıyor musunuz? (Evet veya Hayır) "))
    if sipariş_onayı == 'Evet':
        isim = str(input("Lütfen isminizi giriniz: "))
        while True:
            try:
                kimlik = int(input("Lütfen TC Kimlik numaranızı giriniz: "))
                if len(str(kimlik)) != 11:
                    raise ValueError("TC Kimlik numarasının 11 haneli olması gerekir.")
                break
            except ValueError as e:
                print("Hata:", e)

        while True:
            try:
                kart_no = int(input("Lütfen kredi kartı numaranızı giriniz: "))
                if len(str(kart_no)) != 16:
                    raise ValueError("Kart numarasının 16 haneli olması gerekir.")
                break
            except ValueError as e:
                print("Hata:", e)

        while True:
            try:
                kart_şifre = int(input("Lütfen kredi kartı şifrenizi giriniz: "))
                if len(str(kart_şifre)) != 4:
                    raise ValueError("Kart şifresinin 4 haneli olması gerekir. Lütfen 4 haneli kart şifrenizi tuşlayın.")
                break
            except ValueError as e:
                print("Hata:", e)

        data = [[isim, kimlik, kart_no, kart_şifre]]
        with open("Orders_Database.csv", "a", newline='') as file_csv:
            csv_writer = csv.writer(file_csv)
            csv_writer.writerows(data)

        print("Siparişinizi aldık. Bizi tercih ettiğiniz için teşekkürler. ")
    elif sipariş_onayı == 'Hayır':
        print("Siparişiniz iptal edilmiştir.")
    else:
        print("Hatalı tuşladınız. Lütfen tekrar deneyin.")


#Depolanan datayı okutmak için aşağıdaki kodu yorum satırından çıkarıp kullanabilirsiniz
"""with open("Orders_Database.csv", "r", newline='') as file_csv:
        csv_reader = csv.reader(file_csv)
        data = []
        for row in csv_reader:
            data.append(row)
        print(data)"""

#Main methodunun çağrılması
if __name__ == '__main__':
    main()




