from .forms import TaskForm
from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url
from pyramid.view import view_config


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
