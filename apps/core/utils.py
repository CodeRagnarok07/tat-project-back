
from django.template.defaultfilters import slugify


def auto_slug(nombre_field, Model):
    original_slug = slugify(nombre_field) # creacion automatica apartir del titulo
    queryset = Model.objects.all().filter(slug__iexact=original_slug).count() 
    # "Busca si hay otro slug que conincida con el mismo original_slug"
    count = 1
    slug = original_slug
    # (queryset) si encuentra otro con este mismo slug
    while(queryset): 
        slug = original_slug + '-' + str(count)
        count += 1
        # vuelve a hacer la verificacion
        queryset = Model.objects.all().filter(slug__iexact=slug).count() 

    return slug