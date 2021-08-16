from django.db import models


class Person_type(models.Model):
    relacao = models.CharField('Vínculo', max_length=32)

    class Meta:
        verbose_name = 'Vínculo'

    def __str__(self):
        return self.relacao


class Person_media_type(models.Model):
    media_type = models.CharField('Mídia', max_length=32)

    class Meta:
        verbose_name = 'Tipo de Mídia'

    def __str__(self):
        return self.media_type


class Add_update(models.Model):
    AddOrUpdate = models.CharField('Status', max_length=32)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = "Status"

    def __str__(self):
        return self.AddOrUpdate


class Person(models.Model):
    name = models.CharField('Nome', max_length=32)
    type = models.ForeignKey(Person_type, related_name='vinculo', on_delete=models.CASCADE)
    cpf = models.CharField('CPF', max_length=14, unique=True, help_text="Ex: '000.000.000-00' ou '00000000000'")
    phone = models.CharField('Phone', max_length=15, blank=True, default="")
    company = models.CharField('Empresa', max_length=32)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Nome'
        verbose_name_plural = 'Nome'


    def __str__(self):
        return self.name


class Person_media(models.Model):
    person_id = models.OneToOneField(Person, related_name='midia', on_delete=models.CASCADE)
    media_id = models.ForeignKey(Person_media_type, related_name='midia', on_delete=models.CASCADE)
    object_media = models.TextField()

    class Meta:
        verbose_name = 'Mídia pessoal'
        verbose_name_plural = 'Mídia pessoal'

    def __str__(self):
        return f'{self.media_id}'


class Person_audit(models.Model):
    person_id = models.OneToOneField(Person, related_name='editar', on_delete=models.CASCADE)
    cpf_new = models.CharField('Novo CPF', max_length=14, help_text="Máximo 14 caractéres")
    cpf_old = models.CharField('Antigo CPF', max_length=14, help_text="Máximo 14 caractéres", blank=True, default="")
    add_id = models.ForeignKey(Add_update, related_name='atualizacao', on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Editar"
        verbose_name_plural = "Editar"

    def __str__(self):
        return f'{self.add_id}'
