class Image:
    total = 0

    def __init__(self, resolution: str, size: int, extension: str):
        self.resolution = resolution
        self.size = size
        self.extension = extension
        Image.total += 1

    def __add__(self, other):
        return (f"{self.resolution[:self.resolution.find("x")]}"
                f"{other.resolution[other.resolution.find("x"):]}",
                self.size + other.size)

    # def __eq__(self, __value):
    #     return super().__eq__(__value)

    def __eq__(self, other):
        return self.resolution == other.resolution and self.size == other.size and self.extension == other.extension

    def resize(self, resolution: str):
        self.resolution = resolution

    @staticmethod
    def merge(first, second):
        return first + second


class ImageEx(Image):
    def print_attr(self):
        print(self.__dict__)


print(__name__)

# i1 = ImageEx("640x480", 1000, "jpg")
# i1.resize("1024x768")
# i1.print_attr()
#
# i2 = ImageEx("800x600", 5000, "jpg")
# i2.print_attr()
#
# print(Image.__subclasses__())
