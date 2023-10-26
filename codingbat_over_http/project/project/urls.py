# project/urls.py
from django.contrib import admin
from django.urls import path, include
from app.views import near_hundred, string_splosion, cat_dog, lone_sum

urlpatterns = [
    path("admin/", admin.site.urls),
    path("warmup-1/near-hundred/<int:n>/", near_hundred, name="near_hundred"),
    path("warmup-2/string-splosion/<str:s>/", string_splosion, name="string_splosion"),
    path("string-2/cat-dog/<str:s>/", cat_dog, name="cat_dog"),
    path("logic-2/lone-sum/<int:a>/<int:b>/<int:c>/", lone_sum, name="lone_sum"),
]
