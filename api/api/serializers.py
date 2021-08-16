from rest_framework import serializers
from re import match


from .models import (
    Person_type,
    Person_media_type,
    Add_update,
    Person, Person_media,
    Person_audit)


def cpf_validator(value):
    if not match(r"^(\d{3}.){2}\d{3}-\d{2}$", value):
        raise serializers.ValidationError('CPF não válido')


class PersonTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person_type
        fields = (
            'id',
            'relacao',
        )


class PersonMediaTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person_media_type
        fields = (
            'id',
            'media_type'
        )


class AddUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Add_update
        fields = (
            'id',
            'AddOrUpdate')


class PersonMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person_media
        fields = (
            'id',
            'person_id',
            'media_id',
            'object_media')


    def to_representation(self, instance):
        """Convert text to image"""
        ret = super(PersonMediaSerializer, self).to_representation(instance)

        media = Person_media.objects.get()

        ret['object_media'] = media.object_media
        return ret

    object_media = serializers.FileField()


class PersonAuditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person_audit
        fields = (
            'id',
            'person_id',
            'cpf_new',
            'cpf_old',
            'add_id',
            'last_update')

    cpf_new = serializers.CharField(validators=[cpf_validator])
    cpf_old = serializers.CharField(validators=[cpf_validator])


class PersonSerializer(serializers.ModelSerializer):
    #Nested Relationship
    midia = PersonMediaSerializer(read_only=True)
    editar = PersonAuditSerializer(read_only=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'name',
            'type',
            'cpf',
            'phone',
            'company',
            'midia',
            'editar',
            'last_update')

    cpf = serializers.CharField(validators=[cpf_validator])
