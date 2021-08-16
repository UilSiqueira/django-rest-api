from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import viewsets

import base64


from .models import (
    Person_type,
    Person_media_type,
    Add_update,
    Person, Person_media,
    Person_audit)

from .serializers import (
    PersonTypeSerializer,
    PersonMediaTypeSerializer,
    AddUpdateSerializer,
    PersonSerializer,
    PersonMediaSerializer,
    PersonAuditSerializer)


class PersonTypeViewSet(viewsets.ModelViewSet):
    queryset = Person_type.objects.all()
    serializer_class = PersonTypeSerializer


class PersonMediaTypeViewSet(viewsets.ModelViewSet):
    queryset = Person_media_type.objects.all()
    serializer_class = PersonMediaTypeSerializer


class AddUpdateViewSet(viewsets.ModelViewSet):

    queryset = Add_update.objects.all()
    serializer_class = AddUpdateSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @action(detail=True, methods=['get'])
    def midia(self, request, pk=None):
        person_id = self.get_object()
        serializer = PersonMediaSerializer(person_id.midia)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def editar(self, request, pk=None):
        person_id = self.get_object()
        serializer = PersonAuditSerializer(person_id.editar)
        return Response(serializer.data)


class PersonMediaViewSet(viewsets.ModelViewSet):

    queryset = Person_media.objects.all()
    serializer_class = PersonMediaSerializer

    def create(self, request, *args, **kwargs):
        post = request.data

        image = post['object_media']
        image_read = image.read()
        image_to_text = base64.encodebytes(image_read)

        post['object_media'] = image_to_text

        nome = Person.objects.get(pk=int(post["person_id"]))
        media = Person_media_type.objects.get(pk=int(post["media_id"]))

        new_media, created = Person_media.objects.get_or_create(person_id=nome, media_id=media,
                                                                object_media=post["object_media"])

        new_media.save()

        serializer = PersonMediaSerializer(new_media)

        return Response(serializer.data)


class PersonAuditViewSet(viewsets.ModelViewSet):
    queryset = Person_audit.objects.all()
    serializer_class = PersonAuditSerializer



