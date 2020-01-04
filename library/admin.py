from django.contrib import admin
from library.models import *

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Attrib)
admin.site.register(AuthorAndBook)
admin.site.register(Rate)
admin.site.register(Category)
admin.site.register(CategoryAndBook)
admin.site.register(Bookmark)
admin.site.register(History)
admin.site.register(Comment)
