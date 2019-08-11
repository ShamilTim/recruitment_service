from django.contrib import admin

from rservice.models import Recruit, Sith, Planet, Test


class RecruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'planet_habitat', 'age', 'email', 'published')
    list_display_links = ('name', 'planet_habitat')
    search_fields = ('name', 'planet_habitat__planet_name')


class SithAdmin(admin.ModelAdmin):
    list_display = ('sith_name', 'learning_planet', 'shadow_hand')
    list_display_links = ('sith_name', 'learning_planet')
    search_fields = ('sith_name', 'learning_planet__planet_name')


admin.site.register(Recruit, RecruitAdmin)
admin.site.register(Sith, SithAdmin)
admin.site.register(Planet)
admin.site.register(Test)
