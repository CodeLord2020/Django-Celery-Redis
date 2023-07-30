from django.contrib import admin

# Register your models here.
# from .models import UserAccountManager, MyUser

# admin.site.register(UserAccountManager)
# admin.site.register(MyUser)

from .models import MyUser
@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    pass