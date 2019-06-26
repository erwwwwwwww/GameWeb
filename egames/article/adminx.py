from .models import Articles, GamesReviews, Comments, GameImage, Contact
import xadmin


# 文章
class ArticleAdmin():
    # 后台显示字段
    list_display = ['title', 'image', 'add_time', 'edit_time', 'author', 'is_recommend']
    # 搜索字段
    search_fields = ['title', ]
    # 过滤字段
    list_filter = ['add_time']
    # 列表中直接修改字段
    list_editable = ['is_recommend']
    # 自动刷新
    # refresh_time = [5, 7]
    # 配置插件效果
    style_fields = {'detail': 'ueditor'}


# 游戏
class GameAdmin():
    # 后台显示字段
    list_display = ['name', 'game_tag', 'date_publi', 'updated', 'total_score', 'isTop', 'isRecom']
    # 搜索字段
    search_fields = ['name', 'game_tag']
    # 过滤字段
    list_filter = ['created']
    # 列表中直接修改字段
    list_editable = ['isTop', 'reRecom']
    # 自动刷新
    # refresh_time = [5, 7]
    # 配置插件效果
    # style_fields = {'content': 'ueditor'}


# 用户留言
class ContactAdmin():
    list_display = ['name', 'email', 'obj']


xadmin.site.register(Articles, ArticleAdmin)
xadmin.site.register(GamesReviews, GameAdmin)
xadmin.site.register(Contact, ContactAdmin)

