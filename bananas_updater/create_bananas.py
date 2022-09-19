from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import random as rd
from datetime import datetime
import os

from django_find_bananas.settings import BASE_DIR
from find_bananas.models import Bananas

outfile = os.path.join(BASE_DIR, 'find_bananas/static/images/banana-thumbnail.png')
outfile_rotated = os.path.join(BASE_DIR, 'find_bananas/static/images/banana-thumbnail_rotated.png')
image1 = os.path.join(BASE_DIR, 'find_bananas/static/images/bananas_of_the_day_round1.png')
image2 = os.path.join(BASE_DIR, 'find_bananas/static/images/bananas_of_the_day_round2.png')
image3 = os.path.join(BASE_DIR, 'find_bananas/static/images/bananas_of_the_day_round3.png')

#Convert bananas.png in thumbnail :

# img = Image.open('/Users/{username}/find-bananas/banana.png', 'r').convert("RGBA")
# img_w, img_h = img.size
# img_w = img_w/4
# img_h = img_h/4
# size = (img_w, img_h)

# img.thumbnail(size, Image.ANTIALIAS)
# img.save(outfile, "PNG")

def bananas_of_the_day(first_time = False):

  img_thumb = Image.open(outfile, 'r').convert("RGBA")

  background1 = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
  background2 = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
  background3 = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
  bg_w, bg_h = background1.size

  nb_bananas_round1 = rd.randint(20, 50)
  nb_bananas_round2 = rd.randint(50, 100)
  nb_bananas_round3 = rd.randint(100, 200)

  for i in range(nb_bananas_round1):
    img_thumb = Image.open(outfile, 'r').convert("RGBA")
    img_thumb.rotate(rd.randint(0, 360), expand=True).save(outfile_rotated)
    img_thumb_rotate = Image.open(outfile_rotated, 'r').convert("RGBA")
    img_w, img_h = img_thumb_rotate.size
    background1.paste(img_thumb_rotate, (rd.randint(0, 1440-img_w), rd.randint(0, 900-img_h)), img_thumb_rotate)

  for i in range(nb_bananas_round2):
    img_thumb = Image.open(outfile, 'r').convert("RGBA")
    img_thumb.rotate(rd.randint(0, 360), expand=True).save(outfile_rotated)
    img_thumb_rotate = Image.open(outfile_rotated, 'r').convert("RGBA")
    img_w, img_h = img_thumb_rotate.size
    background2.paste(img_thumb_rotate, (rd.randint(0, 1440-img_w), rd.randint(0, 900-img_h)), img_thumb_rotate)

  for i in range(nb_bananas_round3):
    img_thumb = Image.open(outfile, 'r').convert("RGBA")
    img_thumb.rotate(rd.randint(0, 360), expand=True).save(outfile_rotated)
    img_thumb_rotate = Image.open(outfile_rotated, 'r').convert("RGBA")
    img_w, img_h = img_thumb_rotate.size
    background3.paste(img_thumb_rotate, (rd.randint(0, 1440-img_w), rd.randint(0, 900-img_h)), img_thumb_rotate)
  #background.show()
  background1.save(image1)
  background2.save(image2)
  background3.save(image3)

  dico_bananas = {
    "round1": {"number": nb_bananas_round1, "image": image1},
    "round2": {"number": nb_bananas_round2, "image": image2},
    "round3": {"number": nb_bananas_round3, "image": image3}
  }
  try:
    if first_time == False:
      Bananas.objects.latest('timestamp').delete()
    new_bananas = Bananas()
    new_bananas.timestamp = datetime.utcnow()
    new_bananas.nb_bananas_1 = dico_bananas["round1"]["number"]
    new_bananas.nb_bananas_2 = dico_bananas["round2"]["number"]
    new_bananas.nb_bananas_3 = dico_bananas["round3"]["number"]
    new_bananas.image_1 = dico_bananas["round1"]["image"]
    new_bananas.image_2 = dico_bananas["round2"]["image"]
    new_bananas.image_3 = dico_bananas["round3"]["image"]
    new_bananas.save()
    print("New bananas created")

  except Exception as e:
    print(e)
    pass
  #return dico_bananas

