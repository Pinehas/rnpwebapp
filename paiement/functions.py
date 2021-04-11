def handle_piece_facture(f):
    with open('APPLICATION/static/files/piece_facture/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_piece_recu(f):
    with open('APPLICATION/static/files/piece_recu/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_piece_entree(f):
    with open('APPLICATION/static/files/piece_entree/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_piece_credit(f):
    with open('APPLICATION/static/files/piece_credit/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_piece_remboursement(f):
    with open('APPLICATION/static/files/'+piece_remboursement/f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_piece_capital(f):
    with open('APPLICATION/static/files/piece_capital/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

