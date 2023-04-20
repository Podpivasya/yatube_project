from django.contrib import admin
from .models import Post, Group
# https://postimg.cc/GTDZ1xkd у меня выдает какие то ошибки,
#  я все поняла, все скачала,
# но у меня незапускается сервер, ошибки из файлов,
# которые я не должна троогать или джанго невидит файл, я разберусь,
# но мне надо дальше пройти, иначе исключат


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    list_editable = ('group',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description',)
    search_fields = ('title',)



admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
