from django.contrib import admin
from .models import Test
from .models import Profile


class TestAdmin(admin.ModelAdmin):
    list_display = ('question', "option_1", "option_2", 'option_3', 'option_4', "answer")


admin.site.register(Test, TestAdmin)
admin.site.register(Profile)


