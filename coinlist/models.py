from django.db import models
# Make your models here.


class Coin(models.Model):
    coin_name = models.CharField(max_length=30)
    coin_price = models.FloatField()
    coin_img_url = models.URLField()
    active_masternodes = models.IntegerField()
    coins_daily = models.FloatField()
    collaterial = models.IntegerField(default=1000)
    rpc_port = models.IntegerField(default=0)

    def show_coins_daily(self):
        return round(self.coins_daily * 10)/10

    def roi(self):
        result = round((self.coins_daily * 365000)/(self.active_masternodes * self.collaterial))/10
        return result

    def __str__(self):
        return self.coin_name

