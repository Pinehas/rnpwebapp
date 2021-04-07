def handle_cv(f):
    with open('APPLICATION/static/files/cv/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_photo(f):
    with open('APPLICATION/static/files/photo/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def handle_contrat(f):
    with open('APPLICATION/static/files/contrat/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)