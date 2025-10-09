from django.contrib import admin
from .models import Listing
from django.forms import NumberInput
from django.db import models
from django import forms
from taggit.forms import TagWidget

# Register your models here.

class ListingAdminForm(forms.ModelForm):
    class Meta:
        model = Listing
        # fields = '__all__'
        fields = ['doctor', 'title', 'address', 'district', 'description',
                'services', 'service', 'screens', 'screen', 'professionals',
                'professional', 'rooms', 'photo_main', 'photo_1', 'photo_2',
                'photo_3', 'photo_4', 'photo_5', 'photo_6', 'is_published']
        widgets = {
            'services': TagWidget(),
        }

class ListingAdmin(admin.ModelAdmin):
    form = ListingAdminForm
    list_display = 'id', 'title', 'district', 'rooms', 'doctor', 'is_published', 'tag_list'
    list_display_links = 'id', 'title'
    list_filter = 'doctor', 'services'
    list_editable = 'is_published', 'rooms'
    search_fields = 'title', 'district', 'doctor__name', 'description', 'services__name'
    list_per_page = 25
    ordering = ['id']
    # prepopulated_fields = {'title': ('title',)}
    formfield_overrides = {
        models.IntegerField: {
            'widget': NumberInput(attrs={'size': '10'})
        }
    }
    show_facets=admin.ShowFacets.ALWAYS
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('services')

admin.site.register(Listing, ListingAdmin)