from pathlib import Path
import shutil

from dozen_days_generator import object_image_scraper, image_creator
from dozen_days_detector import detector, classifier

_ROOT = Path(__file__).parent


if __name__ == '__main__':
    # Part 1
    scrape = input('Scrape for new images? [y/n]: ')
    if scrape.lower() == 'y':
        object_image_scraper.scrape_images()
    image_creator.sing_the_song()

    # copy images to Part 2
    src_dir = _ROOT / 'dozen_days_generator' / 'data' / 'days-images'
    src_files = list(src_dir.glob('*.png'))
    for filepath in src_files:
        dest = _ROOT / 'dozen_days_detector' / 'data' / filepath.name
        shutil.copy(filepath, dest)

    # Part 2
    path = _ROOT / 'dozen_days_detector' / 'data'
    images = list(path.glob('*.png'))
    image_object_counts = detector.detect_multiple_images(images)
    matching = classifier.classify_images(image_object_counts)
    print(matching)
