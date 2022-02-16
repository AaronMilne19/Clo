
from django.contrib import admin
from home.models import Magazine, UserProfile, MagazineIssue, Hashtag, DiscountCode



class MagazineAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}




admin.site.register(Magazine, MagazineAdmin)
admin.site.register(MagazineIssue)
admin.site.register(UserProfile)
admin.site.register(Hashtag)
admin.site.register(DiscountCode)





