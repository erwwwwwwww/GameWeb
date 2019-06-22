from django.contrib import admin
from .models import UserModel, Articles, GamesReviews, Comments, GameImage, Contact

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','image','add_time', 'edit_time', 'author')  #指定要显示的字段
    list_display_links=('title', )  #点击进入编辑
    search_fields=('title','text',)     #指定搜索字段
    ordering = ('id',)      #指定排序字段

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nickname', 'company', 'qq', 'mobile_phone', 'avater')
    search_fields = ('username', 'email', 'mobile_phone')
    ordering = ('id',)


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'game_tag', 'date_publi', 'updated', 'total_score', 'isTop', 'isRecom')
    list_editable = ('isTop', 'isRecom', )
    search_fields = ('name', 'game_tag', )
    ordering = ('id',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'obj')
    search_fields = ('name', 'email')
    ordering = ('id', )


class GameImageAdmin(admin.ModelAdmin):
    list_display = ('game', 'image')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'obj', )


admin.site.register(Articles, ArticleAdmin)
admin.site.register(UserModel, UserAdmin)
admin.site.register(GamesReviews, GameAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(GameImage, GameImageAdmin)
admin.site.register(Contact, ContactAdmin)

