from django.core.files.storage import default_storage


def is_jpg(filename):
    if type(filename) != 'string':
        data = filename.read()[0:11]
    else:
        data = default_storage.open(filename).read()[0:11]

    if data[:4] != '\xff\xd8\xff\xe0': return False
    if data[6:] != 'JFIF\0': return False
    return True