from PIL import Image
from pathlib import Path
from uuid import uuid4
import random


_ROOT = Path(__file__).parent.absolute()


def _create_day(image_path, n):
    img = Image.open(image_path)
    dst = Image.new('RGB', (img.width * n, img.height))
    for i in range(n):
        dst.paste(img, (img.width * i, 0))
    dst.save(_ROOT / 'data' / 'days-images' / f'{uuid4()}.png')


def sing_the_song():
    path = _ROOT / 'data' / 'object-images'
    object_images = list(path.glob('*.png'))
    for day in range(1, 13):
        image = random.choice(object_images)
        _create_day(image, day)
