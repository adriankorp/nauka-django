from django.shortcuts import render

# Create your views here.
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from .models import Post, Category
from .forms import PostForm
from logging import getLogger

LOGGER = getLogger()


class PostView(ListView):
    template_name = 'post.html'
    model = Post
    paginate_by = 3
    ordering = '-created_at'


class CategoryView(ListView):
    template_name = 'category.html'
    model = Category
    extra_context = {'categorys': Category.objects.all()}


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post


class CategoryDetailView(DetailView):
    template_name = 'post.html'
    model = Category

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        search = self.kwargs.get('slug')
        if search:
            queryset = Post.objects.all().filter(category__slug=search)
            print(queryset)
            return queryset
        else:
            return queryset.none()




class PostCreateView(FormView):
    template_name = 'form.html'
    form_class = PostForm
    success_url = reverse_lazy('post_view')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        post = Post(title=cleaned_data['title'],
                    category=cleaned_data['category'],
                    created_at=cleaned_data['created_at'],
                    text=cleaned_data['text'],
                    )
        post.save()
        return result

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


def home_page_view(request):
    return render(request, template_name='home.html')
