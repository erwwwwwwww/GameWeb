from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import GamesReviews, Articles, Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactForm, RegisterForm, LoginForm, CommentsForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.generic import ListView, DetailView,TemplateView


User = get_user_model()

# Create your views here.


# 访问主页 --视图函数
def index(request):
    return render(request, 'article/index.html')


#访问主页 --类视图
class IndexView(TemplateView):
    template_name = 'article/index.html'


# 游戏详情页
def gameDetail(request, pk):
    game = get_object_or_404(GamesReviews, pk=pk)
    gameImage = game.images.all()
    return render(request, 'article/gameDetail.html', context={'game': game, 'gameImage': gameImage, })


# 游戏详情页 -- 类视图
class GameDetailView(DetailView):
    model = GamesReviews
    template_name = 'article/gameDetail.html'
    context_object_name = 'game'


# 文章详情页
def postDetail(request, pk):
    post = get_object_or_404(Articles, pk=pk)
    user = request.user

    if request.method == 'POST':
        commentsData = CommentsForm(request.POST)
        if commentsData.is_valid():
            if user.is_authenticated():
                commentsData.save(commit=False)
                commentsData.instance.name = user.nickname
                commentsData.instance.post_id = post.pk
                commentsData.save()
            else:
                commentsData.save(commit=False)
                commentsData.instance.post_id = post.id
                commentsData.save()

            return redirect('/egame/post/%s' % pk)


        else:
            return HttpResponse('<p>数据验证错误%s</p>'%commentsData.errors)
    else:
        comments = CommentsForm()

        if user.is_authenticated():
            return render(request, 'article/postDetail.html', context={'post': post,'comments': comments,'user': user},)
        else:
            return render(request, 'article/postDetail.html', context={'post': post,'comments': comments, 'user': None})




# 游戏类 -- 函数视图
def gamecategory(request):
    gameList = GamesReviews.objects.all()
    paginator = Paginator(gameList, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'article/gameCategory.html', context={'gamecategory': contacts})


# 游戏 -- 类视图
class GameCategoryView(ListView):
    template_name = 'article/gameCategory.html'
    model = GamesReviews
    paginate_by = 5
    ordering = '-created'
    context_object_name = 'gamecategory'



# 文章分类 --函数视图
def postcategory(request):
    articleList = Articles.objects.all()
    paginator = Paginator(articleList, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'article/postCategory.html', context={'postcategory': contacts})


# 文章分类 -- 类视图
class PostCategoryView(ListView):
    template_name = 'article/postCategory.html'
    model = Articles
    paginate_by = 5
    ordering = '-add_time'
    context_object_name = 'postcategory'


# 联系
def contact(request):
    if request.method == 'POST':
        contactData = ContactForm(request.POST)
        if contactData.is_valid():
            contactData.save()

            return redirect('/egame/')

    else:
        contactForm = ContactForm()

        return render(request, 'article/contact.html', context={'contact': contactForm})


# 注册
def userRegister(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            username = registerForm.cleaned_data['username']
            password = registerForm.cleaned_data['password1']
            mobilePhone = registerForm.cleaned_data['mobilePhone']
            User.objects.create_user(username=username, password=password, mobile_phone = mobilePhone )

            return redirect('/egame/login/')
        else:
            return HttpResponse('账户注册失败')
    else:
        registerForm = RegisterForm()

        return render(request, 'article/register.html', context={'contact': registerForm})


# 登入
def userLogin(request):
    emptyForm = LoginForm()
    # post请求
    if request.method == 'POST':
        loginData = LoginForm(request.POST)

        if loginData.is_valid():
            username = loginData.cleaned_data['username']
            password = loginData.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/egame/')
            # 用户认证失败
            else:
                return render(request, 'article/login.html', context={'contact': '用户不存在'})
        # 表单验证失败
        else:
            return render(request, 'article/login.html', context={'contact': emptyForm})

    # get请求
    else:
        return render(request, 'article/login.html', context={'contact': emptyForm})


# 退出
def userLogout(request):
    logout(request)
    return redirect('/egame/')


# 用户信息
def userInfo(request):
    user = request.user
    if user.is_authenticated():
        userModel = User.objects.get(username=user.username)
        return render(request, 'article/userInfo.html', context={'contact': userModel})
    # 重新登入
    else:
        return redirect('/egame/login/')









