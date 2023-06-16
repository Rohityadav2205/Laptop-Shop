from django.db import models

# Create your models here.
class  laptopModel(models.Model):
    sno=models.IntegerField()
    company_name=models.CharField(max_length=200)
    ram=models.CharField(max_length=10)
    rom=models.CharField(max_length=10)
    model_name=models.CharField(max_length=30)
    price=models.IntegerField()


    def __str__(self):
        return "sno={0},company_name={1},ram={2},rom={3},model_name={4},price={5}".format(self.sno,
            self.company_name,self.ram,self.rom,self.model_name,self.price)
