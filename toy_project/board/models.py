from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    writer = models.ForeignKey('users.Users', on_delete=models.CASCADE, verbose_name ="작성자")
    tags = models.ManyToManyField('tag.Tag', verbose_name="태그")
    registred_dttm = models.DateField(auto_now_add=True, verbose_name="게시일")

    def __str__(self):
        return self.title
    
    class Meta:
        db_table ="boards"
        verbose_name="게시글"
        verbose_name_plural="게시글"