from bson.objectid import ObjectId
from pyramid.httpexceptions import HTTPFound
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


@view_config(route_name='tadd', renderer='templates/add.jinja2')
def task_add(request):
    form = TaskForm(request.POST, None)

    if request.POST and form.validate():
        entry = form.data
        request.db['tasks'].save(entry)
        return HTTPFound(route_url('home', request))

    return {'form': form}


@view_config(route_name='tedit', renderer='templates/edit.jinja2')
def task_edit(request):

    id = request.matchdict.get('id', None)
    item = request.db['tasks'].find_one({'_id': ObjectId(id)})
    form = TaskUpdateForm(request.POST,
                          id=id, name=item['name'],
                          active=item['active'])

    if request.method == 'POST' and form.validate():
        entry = form.data
        entry['_id'] = ObjectId(entry.pop('id'))
        request.db['tasks'].save(entry)
        return HTTPFound(route_url('home', request))

    return {'form': form}


@view_config(route_name='tdelete')
def task_delete(request):
    id = request.matchdict.get('id', None)
    if id:
        request.db['tasks'].remove({'_id': ObjectId(id)})
    return HTTPFound(route_url('home', request))
