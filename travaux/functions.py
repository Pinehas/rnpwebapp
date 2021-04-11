def handle_contrat_projet(f):
    with open('APPLICATION/static/files/contrat_projet/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_tdr_projet(f):
    with open('APPLICATION/static/files/tdr_projet/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_cahier_projet(f):
    with open('APPLICATION/static/files/cahier_projet/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

