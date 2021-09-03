from django.db import models
import re
import bcrypt

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errores = {}
        if len(User.objects.filter(email=postData['email'])) > 0:
            errores['existe'] = "Email ya registrado"
        else:
            if len(postData['name']) == 0:
                errores['name'] = "Nombre es obligatorio"
            if len(postData['last_name']) == 0:
                errores['last_name'] = "Apellido es obligatorio"
            EMAIL = re.compile(
                r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL.match(postData['email']):
                errores['email'] = "email invalido"
            if len(postData['password']) < 6:
                errores['password'] = "Password debe ser mayor a 6 caracteres"
            if postData['password'] != postData['password2']:
                errores['password'] = "Password no son iguales"
        return errores

    def encriptar(self, password):
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return password

    def validar_login(self, postData, usuario ):
        errores = {}
        if len(usuario) > 0:
            pw_given = postData['password']
            pw_hash = usuario[0].password

            if bcrypt.checkpw(pw_given.encode(), pw_hash.encode()) is False:
                errores['pass_incorrecto'] = "password es incorrecto"
        else:
            errores['usuario_invalido'] = "Usuario no existe"
        return errores

class User(models.Model):
    id = models.AutoField(db_column='user_id',primary_key=True)
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    rol = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    class Meta:
        managed = False
        db_table = 'user'


class Employees(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    area = models.CharField(max_length=45, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class Tools(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    serie = models.CharField(max_length=30, blank=True, null=True)
    model = models.CharField(max_length=45, blank=True, null=True)
    provider = models.CharField(max_length=45, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    active = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tools'


class MovesType(models.Model):
    type = models.CharField(max_length=45, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moves_type'


class Roles(models.Model):
    description = models.CharField(max_length=45, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'roles'

class Moves(models.Model):
    move_type_id = models.ForeignKey(MovesType,related_name='moves_type_has_tools', on_delete=models.CASCADE) #models.IntegerField()
    tool_id = models.ForeignKey(Tools,related_name='moves_type_has_tools', on_delete=models.CASCADE)#models.IntegerField()
    employee_id =models.ForeignKey(Employees,related_name='moves_type_has_tools', on_delete=models.CASCADE) #models.PositiveIntegerField()
    user_email = models.CharField(max_length=255)
    create_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moves_type_has_tools'






