from django.contrib import admin
from home.models import UserSignupDb,UserImage,UserQuery
# Register your models here.
admin.site.register(UserSignupDb)
admin.site.register(UserImage)
admin.site.register(UserQuery)