from django.db import models


# Create your models here.

class Task(models.Model):
    description = models.TextField(max_length=3000, verbose_name='Описание')
    status = models.CharField(max_length=50, verbose_name='Статус', default='new')
    completion_date = models.CharField(max_length=50, blank=True, verbose_name='Дата выполнения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f'{self.id}. {self.description}: {self.status}'

    class Meta:
        db_table = 'tasks'
        verbose_name = "Задача"
        verbose_name_plural = 'Задачи'
