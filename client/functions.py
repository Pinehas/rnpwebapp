def handle_piece_service(f):
    with open('APPLICATION/static/files/piece_service/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)