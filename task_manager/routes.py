def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('tadd', '/add', factory='task_manager.security.TaskFactory')
    config.add_route('tedit', '/edit/{id}', factory='task_manager.security.TaskFactory')
    config.add_route('tdelete', '/delete/{id}', factory='task_manager.security.TaskFactory')
    config.add_route('auth', '/sign/{action}')
