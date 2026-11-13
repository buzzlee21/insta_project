
from pathlib import Path
from fastapi import UploadFile
from PIL import Image, ImageOps
import uuid
import shutil


Path('media').mkdir(exist_ok=True)

def save_photo(photo: UploadFile):

    image = Image.open(photo.file)

    # 핸드폰 사진 회전문제
    image = ImageOps.exif_transpose(image)

    # png 파일 변환 
    image = image.convert('RGB')


    image = ImageOps.fit(image, (1080,1080))

    # ext = Path(photo.filename).suffix
    # name = f'{uuid.uuid4().hex}{ext}'

    # with open(f'media/{name}', 'wb') as f:
    #     shutil.copyfileobj(photo.file, f)

    name = f'{uuid.uuid4().hex}.jpg'
    image.save(f'media/{name}')


    return f'/media/{name}'