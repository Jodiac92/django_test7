from django.db import models

# Create your models here.
class Maker(models.Model):
    mname = models.CharField(max_length=10)
    tel = models.CharField(max_length=20)
    addr = models.CharField(max_length=50)

    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.mname #admin 화면에서 fk 입력시 mname이 보이도록 함
        
class Product(models.Model):
    pname = models.CharField(max_length=10)
    price = models.IntegerField()
    maker_name = models.ForeignKey(Maker, on_delete = models.CASCADE) #알아서 내부적으로 Maker class의 id랑(#pk를 선언 안해줘서 자동생성) 매핑