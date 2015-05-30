from django.contrib import admin
from .models import *

admin.site.register(Profiel)
admin.site.register(Groep)
admin.site.register(Ketzer)
admin.site.register(Kring)
admin.site.register(Werkgroep)
admin.site.register(Lichting)
admin.site.register(Ondervereniging)
admin.site.register(Verticale)
admin.site.register(Activiteit)
admin.site.register(Bestuur)

admin.site.register(GroepsLid)
admin.site.register(KetzerDeelnemer)
admin.site.register(KringLid)
admin.site.register(WerkgroepDeelnemer)
admin.site.register(LichtingLid)
admin.site.register(OnderverenigingsLid)
admin.site.register(VerticaleLid)
admin.site.register(ActiviteitDeelnemer)
admin.site.register(BestuursLid)
