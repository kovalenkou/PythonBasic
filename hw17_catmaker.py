# homework 17 - Cat maker
import argparse
from pathlib import Path
from random import randint
import requests

parser = argparse.ArgumentParser(description='Process to save some cats.')
parser.add_argument('amount', type=int, help='Integers that show the amount of created files')
parser.add_argument('out_dir', nargs='?', default='.', type=Path, help='Destination folder to saves created files')
parser.add_argument('--gray', action='store_true', help='Creates files with black-white cats')

args = parser.parse_args()
out_dir = Path(args.out_dir)
out_dir.mkdir(exist_ok=True)
if out_dir == Path('.'):
    print(f"Hi! This is the cat maker v_0.1.\nNow you will get {args.amount} cat image files in current directory.")
else:
    print(f"Hi! This is the cat maker v_0.1.\nNow you will get {args.amount} cat image files in '{out_dir}' directory.")

for i in range(0, args.amount):
    out_file = Path.joinpath(out_dir, f'img{i + 1}.jpeg')

    base = 'http://placekitten.com'
    width = randint(100, 1000)
    height = randint(100, 1000)

    gray_color = ''
    if args.gray:
        url = f'{base}/g/{width}/{height}'
        gray_color = 'black-white '
    else:
        url = f'{base}/{width}/{height}'

    print(f'Creating {gray_color}cat number {i + 1} with size {width}*{height}')

    response = requests.get(url)
    assert response.status_code == 200, "Can't open the site"

    with open(out_file, 'wb') as img_file:
        img_file.write(response.content)
print('Creation completed successfully!')
