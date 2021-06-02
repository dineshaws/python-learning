from PIL import Image

word_matrix = Image.open('13-working-with-images/word_matrix.png', 'r')

mask = Image.open('13-working-with-images/mask.png', 'r')
mask = mask.resize(((1015,559)))
mask.putalpha(200)
word_matrix.paste(mask,(0,0),mask)

word_matrix.show()