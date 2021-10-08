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


# Página de home
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
    pass


#Utilizo el decorador para evitar que entre a las páginas sin estar logueado
#se debe cambiar en settings settings.LOGIN_URL='/' The URL or named URL pattern where requests are redirected
# for login when using the login_required() decorator

#@login_required


# Controladores para CRUD de Empleados
def edit_employee(request, id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Employee.objects.filter(id=id).exists():
        employee = Employee.objects.get(id=id)
        return HttpResponse(f'Editando a Employee: {employee}')
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
    return HttpResponse(f"Vista de Empleado Detalles {id}")


def create_employee(request):
    
    return render(request, 'home/create_emp.html')


def employee_add(request):
    #Ejemplo de request.POST
    #'name': ['Usuario Uno'], 'last_name': ['Gonzalez'], 'position': ['Albañil'], 'area': ['OOCC'], 
    # 'active': ['on'], '_save': ['Guardar']

    #TODO: Añadir validaciones antes de crear emplado
    if request.POST:
        new_employe=Employee.objects.create(
            name=request.POST['name'],
            last_name=request.POST['last_name'],
            position=request.POST['position'],
            area=request.POST['area'])
        if request.POST['active'] == "off":
            new_employe.active = False
        if '_save' in request.POST:
            return redirect('/home/employees')
        elif '_addanother' in request.POST:
            return redirect('/home/create/employe')
    else:
        return redirect('/home/')


# Controladores para CRUD de Herramientas
def edit_tools(request, id):
    #Verifico que exista el id para no explotar la app con Employee.objects.get() con id que no exista
    if Tool.objects.filter(id=id).exists():
        tool = Tool.objects.get(id=id)
        return HttpResponse(f'Editando a Tools: {tool} asignada a {tool.assigned_at}----{tool_not_assigned_at}')
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
    
    if request.POST:
        #TODO add validation with ToolManager
        new_tool = Tool.objects.create(
            name=request.POST['name'],
            serie=request.POST['serie'],
            model=request.POST['model'],
            provider=request.POST['provider'],
            cost=int(request.POST['cost']),
            #assigned_at=Employee.objects.get(id=request.POST['assigned_at']),
            belong_to=Warehouse.objects.get(id=request.POST['belong_to']))
        if request.POST['active'] == "off":
            new_tool.active = False
        if '_save' in request.POST:
            return redirect('/home/tools')
        elif '_addanother' in request.POST:
            return redirect('/home/create/tool')
    else:
        return redirect('/home/')


def view_tools(request, id):
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
    

    if request.POST:
        #TODO add validation with MoveManager
        tool=Tool.objects.get(id=request.POST['tool'])
        employee=Employee.objects.get(id=request.POST['employee'])
        new_move = Move.objects.create(
            move_type=MovesType.objects.get(id=request.POST['move_type']),
            tool=tool,
            description=request.POST['description'],
            employee=employee)
        #Asigno la herramienta al Employee indicado
        tool.assigned_at=employee
        tool.save()
        if '_save' in request.POST:
            return redirect('/home/moves')
        elif '_addanother' in request.POST:
            return redirect('/home/create/moves')
    else:
        return redirect('/home/moves')
    #print(request.POST)
    #return HttpResponse(f"Creado")


def view_moves(request, id):
    return HttpResponse(f"Visualizar el movimiento {id} ")