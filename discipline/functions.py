def handle_piece_expl(f):
    with open('APPLICATION/static/files/piece_expl/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)