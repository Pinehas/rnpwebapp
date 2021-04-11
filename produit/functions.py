def handle_img_prod(f):
    with open('APPLICATION/static/files/img_prod/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)