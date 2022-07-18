from django.contrib import admin
from .models import Category, Post
"""
list_display = la lista de campos que vemos en el admin
ordering = primero los ordena por autor y luego dentro de cada autor por fecha de publicacion.
Hay que poner author__username porque queremos buscar el nombre del author.
"""

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']
    list_display = ('name','id')
    ordering = ('id',)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    # Los campos many to many son mas dificiles de mostrar
    list_display = ('id','title','author','published','post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'author__username', 'content', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')

    # Creamos un metodo que nos pueda mostrar las categorias
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    # Para cambiar el nombre de post_categories
    post_categories.short_description = 'Catergorias'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)