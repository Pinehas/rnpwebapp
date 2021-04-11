def handle_piece_offre(f):
    with open('APPLICATION/static/files/piece_offre/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_lettre(f):
    with open('APPLICATION/static/files/lettre/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_piece_licenciement(f):
    with open('APPLICATION/static/files/piece_licenciement/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_cv_candidat(f):
    with open('APPLICATION/static/files/cv_candidat/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_piece_jointe_cand(f):
    with open('APPLICATION/static/files/piece_jointe_cand/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

