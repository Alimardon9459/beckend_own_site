from django.db import models

# Create your models here.
class Chat(models.Model):
    fish = models.CharField(max_length=60)
    xabar = models.CharField(max_length=400)
    javob_xabar = models.CharField(max_length=400 , null=True , blank=True)
    sana = models.CharField(max_length=20)

    def __str__(self):
        return self.fish

class Comment(models.Model):
    fish = models.CharField(max_length=60)
    xabar = models.CharField(max_length=400)
    sana = models.CharField(max_length=20)

    def __str__(self):
        return self.fish

class Cpogrm_Comment(models.Model):
    fish = models.CharField(max_length=60)
    xabar = models.CharField(max_length=200)
    sana = models.CharField(max_length=20)

    def __str__(self):
        return self.fish

class Elon(models.Model):
    sarlavha = models.CharField(max_length=200)
    malumot = models.TextField(max_length=10000)
    sana = models.CharField(max_length=20)

    def __str__(self):
        return self.sarlavha

class Elon_rasm(models.Model):
    sarlavha = models.CharField(max_length=200)  
    rasmi = models.TextField(max_length=1000) 
    elon_id = models.ForeignKey('Elon' , on_delete=models.CASCADE, related_name='elon_rasm')   

    def __str__(self):
        return self.sarlavha

class Xodimlar(models.Model):
    fish = models.CharField(max_length=100)
    mansabi = models.CharField(max_length=200)
    tel_raqami = models.CharField(max_length=20)
    manzili = models.CharField(max_length=200)
    rasmi = models.CharField(max_length=200)
    yili = models.CharField(max_length=50)
    telegram_link = models.CharField(max_length=200 , null=True, blank=True)
    location = models.CharField(max_length=500 , null=True , blank=True)
    e_mail = models.CharField(max_length=100 , null=True , blank=True)
    ish_joyi_bir = models.CharField(max_length=200 , null=True , blank=True)
    ish_joyi_ikki = models.CharField(max_length=200 , null=True , blank=True)
    lavozim_doirasi = models.TextField(max_length=100000 , null=True , blank=True )

    def __str__(self):
        return self.fish

class Xodimga_xabar(models.Model):
    fish = models.CharField(max_length=100)
    xabar = models.TextField(max_length=10000)
    tel = models.TextField(max_length=20)
    sana = models.CharField(max_length=20)
    xodim_id = models.ForeignKey('Xodimlar' , on_delete=models.CASCADE, related_name='xodim_xabar')

    def __str__(self):
        return self.fish

class Reyting_xodim(models.Model):
    baho = models.CharField(max_length=10, null=True , blank=True)
    xodim_id = models.ForeignKey('Xodimlar' , on_delete=models.CASCADE, related_name='baholar')

    def __ste__(self):
        return self.baho

class Axolisi(models.Model):
    nomi = models.CharField(max_length=150)
    yoshlar_soni = models.IntegerField()
    orta_yoshlar_soni = models.IntegerField()
    keksalar_soni = models.IntegerField()
    umumiy = models.IntegerField()

    def __str__(self):
        return self.nomi

class Xudud(models.Model):
    nomi = models.CharField(max_length=150)
    raysi = models.CharField(max_length=150)
    xonadon_soni = models.IntegerField()
    axoli_soni = models.IntegerField()

    def __str__(self):
        return self.nomi


class Xudud_rasm(models.Model):
    rasm = models.CharField(max_length=200)
    xudud_id = models.ForeignKey('Xudud' , on_delete=models.CASCADE, related_name='xudud_rasm')

    def __str__(self):
        return self.rasm








