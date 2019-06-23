from django import template
from article.models import Articles, GamesReviews, GameImage
from django.contrib.auth import get_user_model


User = get_user_model()
register = template.Library()

# 最新文章
@register.simple_tag
def lastarticles():
    showNum = 3
    result = Articles.objects.order_by('-add_time')[:showNum]
    return  result


# 游戏top
@register.simple_tag
def top_game():
    showNum = 3
    game_list = GamesReviews.objects.filter(isTop=True)[:showNum]
    return game_list


# 编辑推荐游戏
@register.simple_tag
def gameRecom():
    result = GamesReviews.objects.filter(isRecom=True)
    return result


# 最新游戏
@register.simple_tag
def gamelast():
    showNum = 5
    result = GamesReviews.objects.order_by('-created')[:showNum]
    return result


# 热门游戏
@register.simple_tag
def gamepopular():
    showNum = 5
    result = GamesReviews.objects.order_by('total_score')[:showNum]
    return result


# 验证用户登入
# @register.simple_tag
# def userAuth():
#     currentRequest = GlobalRequestMiddleware.getRequest()
#     username = currentRequest.session.get('username', None)
#     print('------------用户名:%s-----------'%username)
#     if username :
#         user = User.objects.get(username=username)
#         return user
#     else:
#         return False





