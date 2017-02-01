def deployment_mode(request):

    server_name = request.META['SERVER_NAME']
    
    if server_name == 'dev.transdeco.fi':
        dmode = 'staging'
    elif server_name == 'www.transdeco.fi':
        dmode = 'production'
    else:
        dmode = 'production'
        
    return {'dmode':dmode}