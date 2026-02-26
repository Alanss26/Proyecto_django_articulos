from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleView.as_view(), name="articleslist"),
    path('all', views.ArticleListView.as_view(), name="all_articles"),
    path('new', views.NewArticleForm.as_view(), name="new_article"),
    path('edit/<int:id>', views.EditArticleView.as_view(), name="edit_article"),
    path('<int:pk>', views.ArticleDetailView.as_view(), name="article_detail"),
]