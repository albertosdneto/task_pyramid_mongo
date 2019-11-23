from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    # return {'project': 'tasks_mongo'}
    tasks = request.db['tasks'].find()
    return {
        'tasks': tasks,
        'project': 'tasks_mongo',
    }
