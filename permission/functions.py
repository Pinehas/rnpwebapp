def handle_piece_justif(f):
    with open('APPLICATION/static/files/piece_justif/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

