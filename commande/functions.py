def handle_piece_cmd(f):
    with open('APPLICATION/static/files/piece_cmd/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_piece_dmd(f):
    with open('APPLICATION/static/files/piece_dmd/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

