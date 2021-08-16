from django.contrib import admin

from .models import (
    Person_type,
    Person_media_type,
    Add_update,
    Person, Person_media,
    Person_audit)


@admin.register(Person_type)
class PersonTypeAdmin(admin.ModelAdmin):
    list_display = ('relacao',)


@admin.register(Person_media_type)
class PersonMediaTypeAdmin(admin.ModelAdmin):
    list_display = ('media_type',)


@admin.register(Add_update)
class PersonAddOrUpdateAdmin(admin.ModelAdmin):
    list_display = ('AddOrUpdate',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'cpf', 'phone', 'company', 'last_update')


@admin.register(Person_media)
class PersonMediaAdmin(admin.ModelAdmin):
    list_display = ('person_id', 'media_id', 'object_media')


@admin.register(Person_audit)
class PersonAuditAdmin(admin.ModelAdmin):
    list_display = ('person_id', 'cpf_new', 'cpf_old', 'add_id', 'last_update')


