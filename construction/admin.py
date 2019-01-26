# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from construction.models import Contact,Worker,Nation

# Register your models here.
admin.site.register(Contact)
admin.site.register(Worker)
admin.site.register(Nation)