from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login.models import *
from home.models import *
from django.contrib.auth.decorators import login_required


#Funcion para validar la session en cada una de las views
def validate_session(session):
    if 'id' in session:
        return True
    else:
        return False


# Controladores para Menu de Aplicación

def home(request):
    if validate_session(request.session):
        reg_user = User.objects.get(id=request.session['id'])
        employees = Employee.objects.all()
        tools = Tool.objects.all()
        context = {
            'active_user': reg_user,
            'employees': employees,
            'tools': tools,
        }
        return render(request, 'home/home.html', context)
    else:
        return redirect('/')


def create(request):
    return redirect('/home/')


def read(request):
    return HttpResponse("read")


def update(request):
    return redirect('/home/')


def delete(request):
    return redirect('/home/')


def employees(request):
    if validate_session(request.session):
        employees = Employee.objects.all()
        context = {
            'active_user':User.objects.get(id=request.session['id']),
            'employees': employees,
        }
        return render(request, 'home/employees.html', context)
    else:
        return redirect('/')


def tools(request):
    if validate_session(request.session):
        tools = Tool.objects.all()
        context = {
            'active_user':User.objects.get(id=request.session['id']),
            'tools': tools,
        }
        return render(request, 'home/tools.html', context)
    else:
        return redirect('/')


def certification(request):
    context = {
            'active_user':User.objects.get(id=request.session['id']),
            'employees': employees,
        }
    return render(request, 'home/certification.html', context)


#@login_required(login_url='/')
def moves(request):
    if validate_session(request.session):
        tools = Tool.objects.all()
        moves = Move.objects.all().order_by('-created_at') #Ordenados de manera inversa
        context = {
            'active_user':User.objects.get(id=request.session['id']),
            'tools': tools,
            'moves': moves,
        }
        return render(request, 'home/moves.html', context)
    else:
        return redirect('/')


def movetype(request):
    pass


def inform(request):
    return HttpResponse(f"Informes")



# . FIN Controladores para Menu de Aplicación


# Controladores para CRUD de Empleados
def edit_employee(request, id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Employee.objects.filter(id=id).exists():
        context={
            'employee': Employee.objects.get(id=id),
            'active_user':User.objects.get(id=request.session['id']),
        }
        
        return render(request, 'home/edit_emp.html',context)
    else:
        return redirect('/home/')


def delete_employee(request, id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Employee.objects.filter(id=id).exists():
        employee = Employee.objects.get(id=id)
        employee.delete()
        return redirect('/home/employees')
    else:
        return redirect('/home/employees')


def view_employee(request, id):
    #TODO : Verificar de mejor manera la respuesta cuando se solicita un id que no existe
    if validate_session(request.session) & Employee.objects.filter(id=id).exists():
        reg_user = User.objects.get(id=request.session['id'])
        employee = Employee.objects.get(id=id)
        tools = Tool.objects.filter(assigned_at=employee).order_by('-created_at')
        context = {
            'active_user': reg_user,
            'employee': employee,
            'tools': tools,
        }
        return render(request, 'home/view_emp.html', context)
    else:
        return redirect('/')
    #return render(request, 'home/view_emp.html')
    #return HttpResponse(f"Vista de Empleado Detalles {id}")


def create_employee(request):
    
    return render(request, 'home/create_emp.html')

#Para Añadir o Editar
def employee_add(request):
    #Ejemplo de request.POST
    #'name': ['Usuario Uno'], 'last_name': ['Gonzalez'], 'position': ['Albañil'], 'area': ['OOCC'], 
    # 'active': ['on'], '_save': ['Guardar']
    #print(request.POST)

    #TODO: Añadir validaciones antes de crear emplado

    #Valido que es una petición POST
    if request.POST:
        if 'id' in request.POST:
        #Estoy editando
            employee_edit=Employee.objects.get(id=request.POST['id'])
            employee_edit.name=request.POST['name']
            employee_edit.last_name=request.POST['last_name']
            employee_edit.position=request.POST['position']
            employee_edit.area=request.POST['area']
            if 'active' in request.POST:
                employee_edit.active = True
            if '_save' in request.POST:
                employee_edit.save()
                return redirect('/home/employees')
            elif '_addanother' in request.POST:
                employee_edit.save()
                return redirect('/home/create/employe')
        else:
        #Estoy creando uno nuevo
            new_employe=Employee.objects.create(
                name=request.POST['name'],
                last_name=request.POST['last_name'],
                position=request.POST['position'],
                area=request.POST['area'])
            if 'active' in request.POST:
                new_employe.active = True
            if '_save' in request.POST:
                return redirect('/home/employees')
            elif '_addanother' in request.POST:
                return redirect('/home/create/employe')
    else:
        return redirect('/home/')

#. FIN Controladores para CRUD de Empleados


# Controladores para CRUD de Herramientas
def edit_tools(request, id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Tool.objects.filter(id=id).exists():
        context = {
        'active_user':User.objects.get(id=request.session['id']),
        "employees": Employee.objects.all(),
        "warehouses": Warehouse.objects.all(),
        'tool': Tool.objects.get(id=id),
        }
        return render(request, 'home/edit_tool.html', context=context)
    else:
        return redirect('/home/')


def delete_tools(request, id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Tool.objects.filter(id=id).exists():
        tool = Tool.objects.get(id=id)
        tool.delete()
        return redirect('/home/')
    else:
        return redirect('/home/')


def create_tools(request):
    context = {
        'active_user':User.objects.get(id=request.session['id']),
        "employees": Employee.objects.all(),
        "warehouses": Warehouse.objects.all()
    }
    return render(request, 'home/create_tool.html', context=context)


def tool_add(request):
    # request.POST='name': [''], 'serie': [''], 'model': [''], 'provider': [''], 'cost': [''], 'assigned_at': [''], 'belong_to': [''],
    # 'active': ['on'], '_save': ['Guardar']
    if validate_session(request.session): #Validando session
        if request.POST:
            #TODO add validation with ToolManager
            if 'id' in request.POST: #Editando Tools
                edit_tool = Tool.objects.get(id =request.POST['id'])
                edit_tool.name=request.POST['name']
                edit_tool.serie=request.POST['serie']
                edit_tool.model=request.POST['model']
                edit_tool.provider=request.POST['provider']
                edit_tool.cost=int(request.POST['cost'])
                #assigned_at=Employee.objects.get(id=request.POST['assigned_at']),
                edit_tool.belong_to=Warehouse.objects.get(id=request.POST['belong_to'])
                edit_tool.created_for=User.objects.get(id=request.session['id'])
                if 'active' in request.POST['active']:
                    edit_tool.active = True
                if '_save' in request.POST:
                    edit_tool.save()
                    return redirect('/home/tools')
                elif '_addanother' in request.POST:
                    edit_tool.save()
                    return redirect('/home/create/tool')
            else: #Creando Tools
                new_tool = Tool.objects.create(
                    name=request.POST['name'],
                    serie=request.POST['serie'],
                    model=request.POST['model'],
                    provider=request.POST['provider'],
                    cost=int(request.POST['cost']),
                    #assigned_at=Employee.objects.get(id=request.POST['assigned_at']),
                    belong_to=Warehouse.objects.get(id=request.POST['belong_to']),
                    created_for=User.objects.get(id=request.session['id']))
                if 'active' in request.POST['active']:
                    new_tool.active = True
                if '_save' in request.POST:
                    return redirect('/home/tools')
                elif '_addanother' in request.POST:
                    return redirect('/home/create/tool')
        else:
            return redirect('/home/')
    else:
        return redirect('/')


def view_tools(request, id):
    #TODO : Verificar de mejor manera la respuesta cuando se solicita un id que no existe
    if validate_session(request.session) & Tool.objects.filter(id=id).exists():
        reg_user = User.objects.get(id=request.session['id'])
        tool = Tool.objects.get(id=id)
        moves = Move.objects.filter(tool=tool).order_by('-created_at')
        context = {
            'active_user': reg_user,
            'moves': moves,
            'tool': tool,
        }
        return render(request, 'home/view_tool.html', context)
    else:
        return redirect('/')
    return HttpResponse(f"Visualizar detalles de herramienta {id} ")


# Controladores para CRUD de Movimientos
def edit_moves(request, id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Move.objects.filter(id=id).exists():
        move = Move.objects.get(id=id)
        return HttpResponse(f'Editando a Moves: {move}')
    else:
        return redirect('/home/')


def delete_moves(request, id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Move.objects.filter(id=id).exists():
        move = Move.objects.get(id=id)
        move.delete()
        #Visualizar mensaje para indicar que fue efectiva la acción
        return redirect('/home/')
    else:
        return redirect('/home/')


def create_moves(request, type):
    #TODO Realizar la lógica para cuando existan entradas o salidas
    if type == 'in':
        context = {
            'active_user':User.objects.get(id=request.session['id']),
            "employees": Employee.objects.all(),
            "tools": Tool.objects.filter(assigned_at__isnull=False),
            "moves_type": MovesType.objects.filter(type='ENTRADA'),
            "warehouses": Warehouse.objects.all(),
        }
        return render(request, 'home/create_move.html', context=context)
    elif type=='out':
        context = {
            'active_user':User.objects.get(id=request.session['id']),
            "employees": Employee.objects.all(),
            "tools": Tool.objects.filter(assigned_at__isnull=True),
            "moves_type": MovesType.objects.filter(type='SALIDA'),
            "warehouses": Warehouse.objects.all(),
        }
        return render(request, 'home/create_move.html', context=context)


def move_add(request):
    # Ejemplo de request.POST
    # POST DATA 'move_type': ['1'], 'tool': ['2'], 'employee': ['2'], 'description': ['Vino'], '_save': ['Guardar']
    if validate_session(request.session):
        if request.POST:
            #TODO add validation with MoveManager
            tool=Tool.objects.get(id=request.POST['tool'])
            employee=Employee.objects.get(id=request.POST['employee'])
            new_move = Move.objects.create(
                move_type=MovesType.objects.get(id=request.POST['move_type']),
                tool=tool,
                description=request.POST['description'],
                employee=employee,
                approved_for=User.objects.get(id=request.session['id']))
            #Asigno la herramienta al Employee indicado
            if request.POST['move_type']=='1':
                tool.assigned_at=None
                tool.belong_to=Warehouse.objects.get(id=request.POST['belong_to'])
                print("Entrada")
            else:
                tool.assigned_at=employee
                print("Salida")
            tool.save()
            if '_save' in request.POST:
                return redirect('/home/moves')
            elif '_addanother' in request.POST:
                return redirect('/home/create/moves')
        else:
            return redirect('/home/moves')
    else:
        return redirect('/')
    #print(request.POST)
    #return HttpResponse(f"Creado")


def view_moves(request, id):
    return HttpResponse(f"Visualizar el movimiento {id} ")


def edit_certification(request, id):
    return HttpResponse(f"Editar certificación {id} ")


def create_certification(request):
    context = {
            'active_user':User.objects.get(id=request.session['id']),
            "tools": Tool.objects.all(),
        }
    return render(request, 'home/create_certification.html', context=context)

def delete_certification(request, id):
    return HttpResponse(f"Eliminar certificación {id} ")


def certification_add(request):
    return HttpResponse(f"Agregar certificación ")


def view_certification(request, id):
    return HttpResponse(f"Visualizar certificación {id} ")