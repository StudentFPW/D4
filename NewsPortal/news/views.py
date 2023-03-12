# Он импортирует общие представления из Django.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Функция, которая возвращает URL-адрес данного представления.
from django.urls import reverse_lazy

# Импорт класса PostFilter из файла filter.py.
from .filters import PostFilter
# Импорт классов NWForm и ATForm из файла forms.py.
from .forms import NWForm, ATForm
# Он импортирует модель Post из текущего каталога.
from .models import Post


# ----------------------------------------------------------------------------------------------------------------------

# Используется для отображения всех сообщений из базы данных.
class AllPost(ListView):
    model = Post
    ordering = 'datetime'
    template_name = 'flatpages/all_post.html'
    context_object_name = 'ALL'
    paginate_by = 10


########################################################################################################################

# Он используется для отображения всех новостей из базы данных.
class NewsList(ListView):
    model = Post
    ordering = 'datetime'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    paginate_by = 10


# Отображающее всех статьей из базы данных.
class ArticleList(ListView):
    model = Post
    ordering = 'datetime'
    template_name = 'flatpages/articles.html'
    context_object_name = 'article'
    paginate_by = 10


########################################################################################################################

class NewsDetail(DetailView):
    model = Post
    template_name = 'flatpages/new.html'
    context_object_name = 'news'


class ArticleDetail(DetailView):
    model = Post
    template_name = 'flatpages/article.html'
    context_object_name = 'article'


########################################################################################################################

# Представление на основе классов, которое используется для поиска сообщений в базе данных.
class Search(ListView):
    model = Post
    ordering = 'datetime'
    template_name = 'flatpages/search.html'
    context_object_name = 'info'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def only_news(self):
        for _ in Post.objects.filter(article_or_news__iexact='NW'):
            pass


########################################################################################################################

# Создание новой новости.
class NWCreate(CreateView):
    form_class = NWForm
    model = Post
    template_name = 'flatpages/post_edit.html'
    success_url = reverse_lazy("news")

    def form_valid(self, form):
        post = form.save(commit=False)
        post.article_or_news = "NW"
        return super().form_valid(form)


class NWEdit(UpdateView):
    form_class = NWForm
    model = Post
    template_name = 'flatpages/post_edit.html'
    success_url = reverse_lazy("news")


########################################################################################################################

# Создание новой статьи.
class ATCreate(CreateView):
    form_class = ATForm
    model = Post
    template_name = 'flatpages/post_edit.html'
    success_url = reverse_lazy("article")

    def form_valid(self, form):
        post = form.save(commit=False)
        post.article_or_news = "AT"
        return super().form_valid(form)


class ATEdit(UpdateView):
    form_class = ATForm
    model = Post
    template_name = 'flatpages/post_edit.html'
    success_url = reverse_lazy("article")


########################################################################################################################

# Удаление поста.
class PostDel(DeleteView):
    model = Post
    template_name = 'flatpages/post_del.html'
    success_url = reverse_lazy('allpost')

########################################################################################################################
