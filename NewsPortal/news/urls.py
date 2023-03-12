from django.urls import path
from .views import NewsList, \
    NewsDetail, \
    ArticleList, \
    ArticleDetail, \
    Search, \
    PostDel, \
    AllPost, \
    NWCreate, \
    ATCreate, \
    NWEdit, \
    ATEdit

urlpatterns = [
    path('portal/', AllPost.as_view(), name="allpost"),

    path('news/', NewsList.as_view(), name="news"),
    path('news/<int:pk>', NewsDetail.as_view()),
    path('articles/', ArticleList.as_view(), name="article"),
    path('articles/<int:pk>', ArticleDetail.as_view()),

    path('news/search/', Search.as_view()),

    path('news/create/', NWCreate.as_view()),
    path('news/<int:pk>/edit/', NWEdit.as_view()),
    path('news/<int:pk>/delete/', PostDel.as_view()),

    path('articles/create/', ATCreate.as_view()),
    path('articles/<int:pk>/edit/', ATEdit.as_view()),
    path('articles/<int:pk>/delete/', PostDel.as_view()),
]
