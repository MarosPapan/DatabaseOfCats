from django.db import models

# Create your models here.


class rasa(models.Model):
    meno_rasy = models.CharField(max_length=100)
    popis_rasy = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.meno_rasy


class macka(models.Model):
    typ_rasy = models.ForeignKey(rasa, on_delete=models.CASCADE)
    meno = models.CharField(max_length=50)
    rok = models.IntegerField(default=0)
    hmotnost = models.IntegerField()
    vyska = models.IntegerField()
    kastracie = models.CharField(max_length=50)
    popis = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.meno