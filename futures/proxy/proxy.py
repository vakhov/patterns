from abc import ABC, abstractmethod
from typing import Iterable

from futures.proxy.change import YouTubeLibraryProxy


class YouTubeVideo:
    vid: str
    name: str
    content: bytearray


# default interface from library, we can not change it
class YouTubeLibrary(ABC):
    @abstractmethod
    def download_video(self, vid: str) -> YouTubeVideo:
        pass

    @abstractmethod
    def popular_videos(self) -> Iterable[YouTubeVideo]:
        pass


# default implementation from library, we can not change it
# does not cache
class YouTubeVideoDefaultImpl(YouTubeLibrary):
    def download_video(self, vid: str) -> YouTubeVideo:
        pass

    def popular_videos(self) -> Iterable[YouTubeVideo]:
        pass


# our application, which uses YouTubeVideoDefaultImpl
class OurApp:
    def __init__(self, yt_lib: YouTubeLibrary) -> None:
        self.yt_lib = yt_lib

    def work(self, vid: str):
        self.yt_lib.download_video(vid=vid)

    def work_2(self):
        self.yt_lib.popular_videos()


if __name__ == '__main__':
    yt_lib = YouTubeVideoDefaultImpl()
    my_yt_lib = YouTubeLibraryProxy(default_yt_impl=yt_lib)
    app = OurApp(yt_lib=my_yt_lib)
