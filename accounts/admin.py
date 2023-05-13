from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','username','date_joined','last_login','is_active') # Một tuple chứa tên các trường của model Account sẽ được hiển thị trên trang quản trị.
    list_display_links=('email','first_name','last_name') # chứa tên các trường của model Account sẽ được liên kết tới trang chỉnh sửa bản ghi tương ứng.
    readonly_fields=('last_login','date_joined') #  tên các trường của model Account sẽ được hiển thị dưới dạng trường chỉ đọc trên trang quản trị. 
    ordering=('date_joined',) #  tên trường của model Account sẽ được sử dụng để sắp xếp các bản ghi trên trang quản trị
    filter_horizontal=()
    list_filter=()
    fieldsets=() # Một tuple rỗng được sử dụng để ẩn các trường của model Account 
class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')
    
admin.site.register(Account,AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

 