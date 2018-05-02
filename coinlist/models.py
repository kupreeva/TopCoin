from django.db import models
# Make your models here.


class Coin(models.Model):
    coin_name = models.CharField(max_length=30)
    coin_price = models.FloatField()
    coin_img_url = models.URLField()
    active_masternodes = models.IntegerField()
    coins_daily = models.FloatField()
    collaterial = models.IntegerField(default=1000)

    def roi(self):
        result = (self.coins_daily * 36500)/(self.active_masternodes * self.collaterial)
        return result

    def __str__(self):
        return self.coin_name

