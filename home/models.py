from django.db import models
#from login.models import *

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    area = models.CharField(max_length=45, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)+'. - '+self.name+' '+self.last_name

    class Meta:
        managed = False
        db_table = 'employees'


class Tool(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    serie = models.CharField(max_length=30, blank=True, null=True)
    model = models.CharField(max_length=45, blank=True, null=True)
    provider = models.CharField(max_length=45, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)  # This field type is a guess.

    def __str__(self):
        return 'N°: '+self.serie+'-'+self.name

    class Meta:
        managed = False
        db_table = 'tools'


class MovesType(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.type

    class Meta:
        managed = False
        db_table = 'moves_type'


class Role(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'roles'

class Move(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)
    move_type = models.ForeignKey(MovesType, related_name='moves_type_has_tools', on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, related_name='moves_type_has_tools', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='moves_type_has_tools', on_delete=models.CASCADE)
    create_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.move_type.type+' - '+self.tool.name+' - '+self.employee.name

    class Meta:
        managed = False
        db_table = 'moves_type_has_tools'
