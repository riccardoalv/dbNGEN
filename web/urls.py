from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="index"),
    path("api/snp/<str:snpid>/hgvs", views.snp_hgvs, name="snp_hgvs"),
    path("api/snp/<str:snpid>/abstracts",
         views.snp_abstracts, name="snp_abstracts"),
    path("api/gene/<str:geneid>/abstracts",
         views.gene_abstracts, name="gene_abstracts"),
]
