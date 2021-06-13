from django.contrib import admin
from blogging.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


inlines = [CategoryInLine]
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
