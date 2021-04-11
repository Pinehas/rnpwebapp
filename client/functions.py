def handle_piece_service(f):
    with open('APPLICATION/static/files/piece_service/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_piece_client(f):
    with open('APPLICATION/static/files/piece_client/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_img_client(f):
    with open('APPLICATION/static/files/img_client/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

