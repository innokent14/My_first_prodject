from django.db import models


class Advertisements(models.Model):
    title = models.CharField('Title', max_length=128)
    description = models.TextField('Description')
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Auction', help_text='торг')
    created_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id: {self.id}, title: {self.title},  price: {self.price}'

    class Meta:
        db_table = "advertisements"
