from bson.objectid import ObjectId
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from pyramid.url import route_url
from pyramid.view import view_config

from .forms import TaskForm, TaskUpdateForm


@view_config(route_name='home', renderer='templates/home.jinja2')
def task_list(request):
    tasks = request.db['tasks'].find()
    return {
        'tasks': tasks,
        'project': 'task_manager',
    }


@view_config(route_name='tadd', renderer='templates/add.jinja2', permission='create')
def task_add(request):
    form = TaskForm(request.POST, None)

    if request.POST and form.validate():
        entry = form.data
        request.db['tasks'].save(entry)
        return HTTPFound(route_url('home', request))

    return {'form': form}


@view_config(route_name='tedit', renderer='templates/edit.jinja2', permission='edit')
def task_edit(request):

    id_task = request.matchdict.get('id', None)
    item = request.db['tasks'].find_one({'_id': ObjectId(id_task)})
    form = TaskUpdateForm(request.POST,
                          id=id_task, name=item['name'],
                          active=item['active'])

    if request.method == 'POST' and form.validate():
        entry = form.data
        entry['_id'] = ObjectId(entry.pop('id'))
        request.db['tasks'].save(entry)
        return HTTPFound(route_url('home', request))

    return {'form': form}


@view_config(route_name='tdelete', permission='delete')
def task_delete(request):
    id_task = request.matchdict.get('id', None)
    if id_task:
        request.db['tasks'].remove({'_id': ObjectId(id_task)})
    return HTTPFound(route_url('home', request))


@view_config(route_name='auth', match_param='action=in', renderer='string', request_method='POST')
@view_config(route_name='auth', match_param='action=out', renderer='string')
def sign_in_out(request):
    username = request.POST.get('username')
    if username:
        user = request.db['users'].find_one({'name': username})
        if user and user['password'] == request.POST.get('password'):
            headers = remember(request, user['name'])
        else:
            headers = forget(request)
    else:
        headers = forget(request)
    return HTTPFound(location=request.route_url('home'), headers=headers)
