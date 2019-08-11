from django.db import models


class Recruit(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    planet_habitat = models.ForeignKey('Planet', null=True, on_delete=models.PROTECT, verbose_name='Планета обитания')
    age = models.IntegerField(null=True, blank=True, verbose_name='Возраст')
    email = models.EmailField(null=True, blank=True, verbose_name='Электронная почта')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Зарегистрирован')
    answer_1 = models.CharField(null=True, blank=True, max_length=50, verbose_name='Ответ на вопрос №1')
    answer_2 = models.CharField(null=True, blank=True, max_length=50, verbose_name='Ответ на вопрос №2')
    answer_3 = models.CharField(null=True, blank=True, max_length=50, verbose_name='Ответ на вопрос №3')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рекруты'
        verbose_name = 'Рекрут'
        ordering = ['name']


class Sith(models.Model):
    sith_name = models.CharField(max_length=50, verbose_name='Имя')
    learning_planet = models.ForeignKey('Planet', null=True, on_delete=models.PROTECT, verbose_name='Планета обучения')
    shadow_hand = models.ForeignKey('Recruit', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Рука Тени')

    class Meta:
        verbose_name_plural = 'Ситхи'
        verbose_name = 'Ситх'
        ordering = ['sith_name']


class Planet(models.Model):
    planet_name = models.CharField(max_length=50, verbose_name='Планета')

    def __str__(self):
        return self.planet_name

    class Meta:
        verbose_name_plural = 'Планеты'
        verbose_name = 'Планета'
        ordering = ['planet_name']


class Test(models.Model):
    questions = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.questions

    class Meta:
        verbose_name_plural = 'Тесты'
        verbose_name = 'Тест'
