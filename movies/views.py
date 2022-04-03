from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import ListView, DetailView

from movies.models import Movie, Actor
from django.views import View


class HomepageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'number_of_movies': Movie.objects.all().count(),
            'number_of_actors': Actor.objects.all().count(),
            'page_name': 'Homepage'
        }
        return TemplateResponse(request, 'homepage.html', context=context)


# def homepage_view(request):
#     if request.method == 'GET':
#         context = {
#             'number_of_movies': Movie.objects.all().count(),
#             'number_of_actors': Actor.objects.all().count(),
#             'page_name': 'Homepage'
#         }
#         return TemplateResponse(request, 'homepage.html', context=context)
#     elif request.method == 'POST':
#         return HttpResponse(request, 'method not allowed')


class ActorListView(ListView):
    model = Actor
    template_name = 'actors.html'
    extra_context = {'page_name': 'Actors'}


# def actors_view(request):
#     actors = Actor.objects.all()
#     context = {
#         'all_actors': actors,
#         'page_name': 'Actors',
#     }
#     return TemplateResponse(request, 'actors.html', context=context)


class MovieListView(ListView):
    queryset = Movie.objects.all().order_by('-rating')
    template_name = 'movies.html'
    extra_context = {
        'best_movies': Movie.objects.filter(rating__gte=80).order_by('-rating'),
        'worst_movies': Movie.objects.filter(rating__lte=20).order_by('rating'),
        'page_name': 'Movies',
    }


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context.update({'page_name': self.object.name})
        return context


# def movies_view(request):
#     all_movies = Movie.objects.all().order_by('-rating')  # SELECT * FROM movies_movie;
#     best_movies = Movie.objects.filter(rating__gte=80).order_by('-rating')  # SELECT * FROM movies_movie WHERE rating GTE 80;
#     worst_movies = Movie.objects.filter(rating__lte=20).order_by('rating')
#     context = {
#         'all_movies': all_movies,
#         'best_movies': best_movies,
#         'worst_movies': worst_movies,
#         'page_name': 'Movies',
#     }
#     return TemplateResponse(request, 'movies.html', context=context)


def jinja2_testing_view(request):
    index_list = ['index_1', 'index_2', 'index_3']
    index_1 = index_list[0]

    testing_dict = {'key_1': 'value_1', 'key_2': 'value_2'}
    value_1 = testing_dict['key_1']

    context = {
        'testing_list': index_list,
        'testing_dict': testing_dict,
        'testing_queryset': Movie.objects.all(),
    }
    return TemplateResponse(request, 'jinja2_testing.html', context=context)
