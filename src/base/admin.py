from django.contrib import admin
from .models import *

class GroepsLidInline(admin.TabularInline):
    model = GroepsLid

class GroepAdmin(admin.ModelAdmin):
    inlines = [
        GroepsLidInline,
    ]

class KetzerDeelnemerInline(admin.TabularInline):
    model = KetzerDeelnemer

class KetzerAdmin(admin.ModelAdmin):
    inlines = [
        KetzerDeelnemerInline,
    ]

class KringLidInline(admin.TabularInline):
    model = KringLid

class KringAdmin(admin.ModelAdmin):
    inlines = [
        KringLidInline,
    ]

class WerkgroepDeelnemerInline(admin.TabularInline):
    model = WerkgroepDeelnemer

class WerkgroepAdmin(admin.ModelAdmin):
    inlines = [
        WerkgroepDeelnemerInline,
    ]

class LichtingLidInline(admin.TabularInline):
    model = LichtingLid

class LichtingAdmin(admin.ModelAdmin):
    inlines = [
        LichtingLidInline,
    ]

class OnderverenigingsLidInline(admin.TabularInline):
    model = OnderverenigingsLid

class OnderverenigingAdmin(admin.ModelAdmin):
    inlines = [
        OnderverenigingsLidInline,
    ]

class VerticaleLidInline(admin.TabularInline):
    model = VerticaleLid

class VerticaleAdmin(admin.ModelAdmin):
    inlines = [
        VerticaleLidInline,
    ]

class ActiviteitDeelnemerInline(admin.TabularInline):
    model = ActiviteitDeelnemer

class ActiviteitAdmin(admin.ModelAdmin):
    inlines = [
        ActiviteitDeelnemerInline,
    ]

class BestuursLidInline(admin.TabularInline):
    model = BestuursLid

class BestuurAdmin(admin.ModelAdmin):
    inlines = [
        BestuursLidInline,
    ]

admin.site.register(Profiel)
admin.site.register(Groep, GroepAdmin)
admin.site.register(Ketzer, KetzerAdmin)
admin.site.register(Kring, KringAdmin)
admin.site.register(Werkgroep, WerkgroepAdmin)
admin.site.register(Lichting, LichtingAdmin)
admin.site.register(Ondervereniging, OnderverenigingAdmin)
admin.site.register(Verticale, VerticaleAdmin)
admin.site.register(Activiteit, ActiviteitAdmin)
admin.site.register(Bestuur, BestuurAdmin)
