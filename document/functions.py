def handle_doc(f):
    with open('APPLICATION/static/files/doc/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)