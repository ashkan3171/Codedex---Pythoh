import imageio.v3 as iio

filenames = ['dino1.png', 'dino2.png', 'dino3.png', 'dino4.png']

def create_gif(files):
    images = []

    for i in files:
        images.append(iio.imread(i))
    
    iio.imwrite('dino_animation.gif', images, duration=500, loop=0)

create_gif(filenames)
