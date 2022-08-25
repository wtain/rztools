import os
from typing import Dict

from PIL import Image
from PIL.ExifTags import TAGS

from FindDuplicateFiles.FileEnumerator import FileEnumerator


class ImageTagExtractor:

    def __init__(self, file_enumerator: FileEnumerator):
        self.file_enumerator = file_enumerator
        # todo: add Feedback interface

    def is_applicable(self, fileName) -> bool:
        _, extension = os.path.splitext(fileName)
        return str.lower(extension[1:]) in ['jpg', 'jpe', 'jpeg', 'png']

    def extractTags(self, fileName) -> Dict[str, str]:
        if not self.is_applicable(fileName):
            return {}
        try:
            file = self.file_enumerator.open_binary(fileName)
            # image = Image.open(fileName)
            image = Image.open(file)
            exifdata = image.getexif()
            result = {
                "Image_Size": image.size,
                "Image_Height": image.height,
                "Image_Width": image.width,
                "Image_Format": image.format,
                "Image_Mode": image.mode,
                "create_time": os.path.getctime(fileName)
            }
            for tag_id in exifdata:
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                if isinstance(data, bytes):
                    data = data.decode()
                tag = str(tag)
                data = str(data)
                result[tag] = data
            return result
        except OSError as e:
            print("*** ImageTagExtractor: *** ERROR: " + str(e.strerror))
            return {}
        except UnicodeDecodeError as e:
            print("*** ImageTagExtractor: *** ERROR: " + str(e.reason))
            return {}
