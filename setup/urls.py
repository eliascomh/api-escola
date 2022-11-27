from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Aluno')
router.register('cursos', CursosViewSet, basename='Curso')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
