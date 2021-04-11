def handle_image_service(f):
    with open('APPLICATION/static/files/image_service/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

