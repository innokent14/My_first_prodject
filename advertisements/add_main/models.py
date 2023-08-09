from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.html import format_html
from django.contrib import admin

User = get_user_model()


class Advertisements(models.Model):
    title = models.CharField('Title', max_length=128)
    description = models.TextField('Description')
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Auction', help_text='торг')
    created_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisiments/')

    def __str__(self):
        return f'id: {self.id}, title: {self.title},  price: {self.price}'

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_ad.date() == timezone.now().date():
            created_time = self.created_ad.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="Color: green; font-weight: bold"> Сегодня в </span>'
                '<span style="font-weight: bold; Color: gray">{}</span>', created_time
            )

        return self.created_ad.time().strftime('%d:%M:%Y B %H:%M:%S')


    @admin.display(description='Дата Обновления')
    def update_date(self):
        if self.update_ad.date() == timezone.now().date():
            created_time = self.update_ad.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="Color: green; font-weight: bold"> Сегодня в </span>'
                '<span style="font-weight: bold; Color: gray">{}</span>', created_time
            )

        return self.update_ad.time().strftime('%d:%M:%Y B %H:%M:%S')


    class Meta:
        db_table = "advertisements"
