from PIL import Image
import random as rd
import getpass

username = getpass.getuser()

outfile = f'/Users/{username}/find-bananas/banana-thumbnail.png'
outfile_rotated = f'/Users/{username}/find-bananas/banana-thumbnail_rotated.png'
image1 = f"/Users/{username}/find-bananas/django_find_bananas/find_bananas/static/images/bananas_of_the_day_round1.png"
image2 = f"/Users/{username}/find-bananas/django_find_bananas/find_bananas/static/images/bananas_of_the_day_round2.png"
image3 = f"/Users/{username}/find-bananas/django_find_bananas/find_bananas/static/images/bananas_of_the_day_round3.png"

#Convert bananas.png in thumbnail :

# img = Image.open('/Users/{username}/find-bananas/banana.png', 'r').convert("RGBA")
# img_w, img_h = img.size
# img_w = img_w/4
# img_h = img_h/4
# size = (img_w, img_h)

# img.thumbnail(size, Image.ANTIALIAS)
# img.save(outfile, "PNG")

def bananas_of_the_day():

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
	print("Round 1 : ", nb_bananas_round1)
	print("Round 2 : ", nb_bananas_round2)
	print("Round 3 : ", nb_bananas_round3)
	dico_bananas = {
		"round1": {"number": nb_bananas_round1, "image": image1},
		"round2": {"number": nb_bananas_round2, "image": image2},
		"round3": {"number": nb_bananas_round3, "image": image3}
	}
	return dico_bananas

