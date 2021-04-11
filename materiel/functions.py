def handle_guide(f):
    with open('APPLICATION/static/files/guide/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)