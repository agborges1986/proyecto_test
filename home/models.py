from django.db import models
from login.models import *

class EmployeeManager(models.Manager):

    def basic_validator(self, postData):
        pass


class Employee(models.Model):

    #id = models.AutoField(db_column='id',primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    area = models.CharField(max_length=45, blank=True, null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=EmployeeManager()


    def __str__(self):
        return str(self.id) + '. - ' + self.name + ' ' + self.last_name

    #class Meta:
    #    db_table = 'employees'


class Warehouse(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)


class ToolManager(models.Manager):
    #TODO do validation basic_validator
    def basic_validator(self, postData):
        pass


class Tool(models.Model):
    #Incluir las fechas de certificación, vencimiento y períodos y accesos a documentos
    #id = models.AutoField(db_column='id',primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    serie = models.CharField(max_length=30, blank=True, null=True)
    model = models.CharField(max_length=45, blank=True, null=True)
    provider = models.CharField(max_length=45, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    assigned_at = models.ForeignKey(Employee,
                                    related_name='assigned_at',
                                    on_delete=models.DO_NOTHING,
                                    null=True)
    belong_to = models.ForeignKey(Warehouse,
                                related_name='belong_to',
                                on_delete=models.DO_NOTHING,
                                null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    objects = ToolManager()


    def __str__(self):
        return 'N°: ' + self.serie + '-' + self.name

    #class Meta:
    #    db_table = 'tools'


class CertificationManager(models.Manager):

    def basic_validator(self, postData):
        pass

class Certification(models.Model):
    tool = models.OneToOneField(Tool,
                            related_name='certification',
                            on_delete=models.DO_NOTHING,
                            null=True)
    is_necessary = models.BooleanField(default=False)
    last_certification = models.DateTimeField()
    certification_period = models.IntegerField(
        default=180)  #180 dìas (6 meses) de certificación por defecto
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=CertificationManager()


class MovesType(models.Model):
    #id = models.AutoField(db_column='id',primary_key=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type

    #class Meta:
    #    db_table = 'moves_type'


class Role(models.Model):
    #id = models.AutoField(db_column='id',primary_key=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_email = models.CharField(max_length=255)

    #class Meta:
    #    db_table = 'roles'


class MoveManager(models.Manager):

    def basic_validator(self, postData):
        pass


class Move(models.Model):
    #id = models.AutoField(db_column='id',primary_key=True)
    move_type = models.ForeignKey(MovesType,
                                related_name='moves_type_has_tools',
                                on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool,
                            related_name='moves_type_has_tools',
                            on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,
                                related_name='moves_type_has_tools',
                                on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.move_type.type + ' - ' + self.tool.name + ' - ' + self.employee.name

    #class Meta:
    #    db_table = 'moves_type_has_tools'
