from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Author(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=128)
    author = Author.author
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name="categories")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class PostInLine(admin.TabularInLine):
    model = Post


class CategoryInLine(admin.TabularInLine):
    model = Category


class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        PostInLine,
        CategoryInLine,
    ]
