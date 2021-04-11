def handle_rapport(f):
    with open('APPLICATION/static/files/rapport/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_ordre(f):
    with open('APPLICATION/static/files/ordre/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

