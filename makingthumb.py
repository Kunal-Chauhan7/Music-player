from PIL import Image
imag = Image.open('Hatsune3.png')
imag.thumbnail((250,225))
imag.save('Imagebg.png')