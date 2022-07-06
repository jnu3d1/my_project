from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Task(BaseModel):
    status_choices = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Сделано')]
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, verbose_name='Описание')
    status = models.CharField(max_length=11, verbose_name='Статус', choices=status_choices, default='new')
    completion_date = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return f'{self.id}. {self.title}: {self.status}'

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Comment(BaseModel):
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.CharField(max_length=40, null=True, blank=True, default='Аноним', verbose_name='Автор')
    task = models.ForeignKey('webapp.Task', on_delete=models.CASCADE, related_name='comments', verbose_name='Статья')

    def __str__(self):
        return f'{self.id}. {self.author}: {self.text}'

    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

