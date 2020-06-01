from django.utils.text import slugify
import random
import string


# generate unique slug for our object instance
def unique_slug_generator(instance, new_slug=None):
    # check if new_slug parameter is passed
    if new_slug:
        slug = new_slug
    else:
        # used for the User class in models
        # insert new conditionals for different class objects requiring slugs
        if instance.username:
            slug = slugify(instance.username)
        else:
            slug = slugify(str(instance))

    # reference the object class of the instance
    # check if any other instances of the class has identical slug
    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()

    # if duplicate slug exists, generate new slug with random_string_generator
    # pass new_slug recursively to ensure it is a valid and unique slug
    if qs_exists:
        new_slug = '%s-%s' % (slug, random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug)

    return slug


# generate random string made up of lowercase ascii letters and digits
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join([random.choice(chars) for _ in range(size)])


