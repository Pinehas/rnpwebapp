def handle_piece_chat(f):
    with open('APPLICATION/static/files/piece_chat/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_piece_note(f):
    with open('APPLICATION/static/files/piece_note/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_piece_annonce(f):
    with open('APPLICATION/static/files/piece_annonce/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)