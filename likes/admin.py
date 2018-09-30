from django.contrib import admin
from .models import LikeCount


# Register your models here.
@admin.register(LikeCount)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'liked_num')
