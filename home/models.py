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
    objects = EmployeeManager()

    def __str__(self):
        return str(self.id) + '. - ' + self.name + ' ' + self.last_name


class Warehouse(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)


class ToolManager(models.Manager):
    # TODO do validation basic_validator
    def basic_validator(self, postData):
        pass

# El atributo assigned_at es nulo si la herramienta está disponible en Bodega de Almacenamiento

class Tool(models.Model):
    # Incluir las fechas de certificación, vencimiento y períodos y accesos a documentos
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
    created_for = models.ForeignKey(
        User, related_name='tool_created_for', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    objects = ToolManager()

    def __str__(self):
        return 'N°: ' + self.serie + '-' + self.name


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
        default=180)  # 180 dìas (6 meses) de certificación por defecto
    created_for = models.ForeignKey(
        User, related_name='certification_created_for', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CertificationManager()


class MovesType(models.Model):
    #id = models.AutoField(db_column='id',primary_key=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type


class Role(models.Model):
    #id = models.AutoField(db_column='id',primary_key=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_email = models.CharField(max_length=255)


class MoveManager(models.Manager):

    def basic_validator(self, postData):
        pass

# Se define que cualquier emplado puede realizar un movimiento de ENTRADA de una herramienta
# a una bodega asignada por quien recibe la misma. 
# Además se define que la persona que saque la herramienta automáticamente se convierte en el responsable del movimiento y la herramienta.
# La clase herramienta tien dos atributos assigned_at y belong_to, que se actualizan en el momento de la creación del movimiento.

class Move(models.Model):
    #id = models.AutoField(db_column='id',primary_key=True)
    move_type = models.ForeignKey(MovesType,
                                related_name='moves_type_has_tools',
                                on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool,
                            related_name='tool_moved',
                            on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,
                                related_name='moves_employee_tools',
                                on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    approved_for = models.ForeignKey(
        User, related_name='user_approved', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.move_type.type + ' - ' + self.tool.name + ' - ' + self.employee.name


