import multiprocessing
import py_avataaars
from django.shortcuts import render
from nft.forms import AvatarForm
from nft.models import Collection, Image
import os, random, time
from django.core.files import File
from multiprocessing import Pool
from functools import partial
import threading
from .options import *

def generate_random_avatar(filepath):

    avatar = py_avataaars.PyAvataaar(

        style=random.choice(AVATAR_STYLE_OPTIONS),

        skin_color=random.choice(SKIN_COLOR_OPTIONS),

        hair_color=random.choice(HAIR_OPTIONS),

        facial_hair_type=random.choice(FACIAL_HAIR_TYPE_OPTIONS),

        facial_hair_color=random.choice(FACIAL_HAIR_COLOR_OPTIONS),

        top_type=random.choice(TOP_OPTIONS),

        hat_color=random.choice(SKIN_COLOR_OPTIONS),

        mouth_type=random.choice(MOUTH_TYPE_OPTIONS),

        eye_type=random.choice(EYE_TYPE_OPTIONS),

        eyebrow_type=random.choice(EYE_BROW_TYPE_OPTIONS),

        nose_type=py_avataaars.NoseType.DEFAULT,

        accessories_type=random.choice(ACCESSORIES_OPTIONS),

        clothe_type=random.choice(CLOTHE_TYPE_OPTIONS),

        clothe_color=random.choice(CLOTHE_COLOR_OPTIONS),

        clothe_graphic_type=random.choice(CLOTHE_GRAPHIC_TYPE_OPTIONS),

    )

    avatar.render_png_file(filepath)



def create_collection_images(collection, i):

    name = collection.name

    filename = f'{name}-avatar-{i}'

    filepath = f"{filename}.png"

    generate_random_avatar(filepath)

    img = Image.objects.create(name=filename)

    img.image.save(filepath, File(open(filepath, 'rb')), save=True)

    img.save()

    collection.images.add(img)

    os.remove(filepath)

    collection.save()

    return collection


def generate_avatars(request, context):

    context = {}

    if request.method == "POST":

        form = AvatarForm(request.POST or None)

        if form.is_valid():

            collection = form.save()

            quantity = form.cleaned_data.get("quantity")

            for i in range(quantity):

                thread = threading.Thread(name="thread", target=create_collection_images, args=[collection,  i])

                thread.daemon = True

                thread.start()

                time.sleep(0.1)

    

            context.update({

                "collection":collection

            })

    return context