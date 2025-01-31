from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title

from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# from task1.models import Buyer, Game
#
# # Создание записей Buyer
# buyer1 = Buyer.objects.create(name="Алексей", age=17, balance = 1000)  # младше 18
# buyer2 = Buyer.objects.create(name="Ирина", age=25, balance = 1000)   # старше 18
# buyer3 = Buyer.objects.create(name="Сергей", age=30, balance = 1000)   # старше 18
#
# # Создание записей Game
# game1 = Game.objects.create(title="cyberpunk 2077", cost = 1000, size=100, description="test",age_limited=True)   # с ограничением по возрасту
# game2 = Game.objects.create(title="Игра 2", cost = 1000, size=100, description="test", age_limited=False)  # без ограничения по возрасту
# game3 = Game.objects.create(title="Игра 3", cost = 1000, size=100, description="test",  age_limited=True)   # с ограничением по возрасту
#
# # Назначение покупателей для игр
# game1.buyer.set([buyer2, buyer3])  # Игра 1 доступна для покупателей 2 и 3
# game2.buyer.set([buyer1, buyer2, buyer3])  # Игра 2 доступна для всех покупателей
# game3.buyer.set([buyer2, buyer3])  # Игра 3 доступна для покупателей 2 и 3
#