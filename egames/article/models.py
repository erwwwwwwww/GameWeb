from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.urls import reverse

# Create your models here.

# --处理用户上传头像
class UserModel(AbstractUser):
    nickname = models.CharField(max_length=8, null=True, blank=True, verbose_name='昵称', help_text='昵称最大长度为8字符')
    mobile_phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码', help_text='手机号码')
    qq = models.CharField(max_length=15, null=True, blank=True, verbose_name='QQ', help_text='QQ')
    company = models.CharField(max_length=50, verbose_name='工作单位', help_text='工作单位')
    avater = models.ImageField(upload_to='users', verbose_name='用户头像', default='users/defaultAvater.jpg')


# 文章 --内容添加富文本功能
class Articles(models.Model):
    title = models.CharField(max_length=80, help_text='标题')
    image = models.ImageField(upload_to="articleimage", verbose_name="文章主图片", null=True, blank=True)
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')   # 是否推荐
    add_time = models.DateTimeField(auto_now_add=True) # 创建时间
    edit_time = models.DateTimeField(auto_now=True)  # 修改时间
    author = models.ForeignKey(UserModel, verbose_name='作者', related_name='art_author')
    text = models.TextField(verbose_name='内容', help_text='内容')


    class Meta:
        verbose_name = '游戏文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('article:postdetial', kwargs={'pk': self.pk})




# 游戏
class GamesReviews(models.Model):
    name = models.CharField(max_length=50, verbose_name='游戏名称')
    game_tag = models.CharField(max_length=50, verbose_name='游戏类型')
    date_publi = models.CharField(max_length=100 ,verbose_name='发布日期')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # body = models.TextField(verbose_name='信息')
    game_brief = models.TextField(verbose_name='游戏简介')
    buy_address = models.CharField(max_length=100,verbose_name='购买地址')
    official_web = models.CharField(max_length=100, verbose_name='官方主页')
    frame = models.PositiveIntegerField(verbose_name='画面')
    sound_effect = models.PositiveIntegerField(verbose_name='音效')
    plot = models.PositiveIntegerField(verbose_name='剧情')
    operation = models.PositiveIntegerField(verbose_name='操作')
    total_score = models.IntegerField(verbose_name='总评分')
    isTop = models.BooleanField(default=False, verbose_name='是否主页')
    backImage = models.ImageField(upload_to='gameimage', verbose_name='游戏背景图', default='')
    isRecom = models.BooleanField(default=False, verbose_name='编辑推荐')

    class Meta:
        verbose_name = '游戏信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article:gamedetail', kwargs={'pk': self.pk})


#评论
# 不注册可以评论
class Comments(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称', help_text='名称', null=True, blank=True)
    email = models.EmailField(verbose_name='邮件', help_text='邮件', null=True, blank=True)
    obj = models.CharField(max_length=50, verbose_name='标题', help_text='标题')
    body = models.TextField(verbose_name='内容', help_text='内容')
    post = models.ForeignKey(Articles, related_name='articleComments') # 关联文章外键
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    active = models.BooleanField(default=True, verbose_name='是否显示')


    class Meta:
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GameImage(models.Model):
    """
    游戏图库
    """
    game = models.ForeignKey(GamesReviews, verbose_name="游戏", related_name="images")
    image = models.ImageField(upload_to="gameimage", verbose_name="商品图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '游戏图库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.game.name


# 留言
class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name='名字', help_text='名字')
    email = models.EmailField(verbose_name='邮箱', help_text='邮箱')
    obj = models.CharField(max_length=50, verbose_name='主题', help_text='主题')
    text = models.TextField(verbose_name='内容', help_text='内容')
    time = models.DateTimeField(auto_now_add=True, verbose_name='时间')

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s用户留言'%self.name






































