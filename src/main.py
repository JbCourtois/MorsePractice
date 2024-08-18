import os
import random

from player import init_transmission, morsecode
from messages import read_and_process_file


if __name__ == "__main__":
    paragraphs = read_and_process_file(f'Ressources/extraits.txt')
    random.shuffle(paragraphs)

    init_transmission()
    for paragraph in paragraphs:
        morsecode(paragraph)
