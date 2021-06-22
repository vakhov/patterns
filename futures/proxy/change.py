from typing import Iterable, Dict, List

from futures.proxy.proxy import YouTubeLibrary, YouTubeVideo


class YouTubeLibraryProxy(YouTubeLibrary):
    cached_videos: Dict[int, YouTubeVideo] = {}
    cached_popular_videos: List[YouTubeVideo] = []

    def __init__(self, default_yt_impl: YouTubeLibrary) -> None:
        self.default_yt_impl = default_yt_impl

    def download_video(self, vid: str) -> YouTubeVideo:
        if vid in self.cached_videos:
            return self.cached_videos[vid]
        non_cached_vid = self.default_yt_impl.download_video(vid=vid)
        self.cached_videos[vid] = non_cached_vid
        return non_cached_vid

    def popular_videos(self) -> Iterable[YouTubeVideo]:
        if len(self.cached_popular_videos) > 0:
            return self.cached_popular_videos
        return self.default_yt_impl.popular_videos()
