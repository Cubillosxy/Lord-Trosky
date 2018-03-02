from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=200, verbose_name='título')
    description = models.CharField(max_length=600, verbose_name='Descripción')

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación',
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'


class Article(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    content = models.TextField(max_length=1000, verbose_name='contenido')

    user = models.ForeignKey(
        'user.User',
        verbose_name='autor',
        null=True,
        on_delete=models.SET_NULL,
    )

    publication = models.ForeignKey(
        Publication,
        verbose_name='publicación',
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'


class Qualification(models.Model):
    user = models.ForeignKey(
        'user.User',
        verbose_name='autor',
        null=True,
        on_delete=models.SET_NULL,
    )

    article = models.ForeignKey(
        Article,
        verbose_name='artículo calificado',
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación',
    )

    score = models.PositiveSmallIntegerField(
        default=5,
        verbose_name='Ponderado',
    )

    def __str__(self):
        return self.user.email

    class Meta:
        ordering = ['id']
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'
