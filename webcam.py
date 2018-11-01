import cv2

from actor import Actor


class WebcamActor(Actor):
    def __init__(self, *args, source=0, processing_pipeline=None, source_capabilities=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._source = cv2.VideoCapture(source)
        self.processing_pipeline = processing_pipeline or []

        if source_capabilities:
            for setting, value in source_capabilities.items():
                self._source.set(setting, value)

    def render(self):
        ret, frame = self._source.read()
        if ret:
            self.frame = frame

        for handler in self.processing_pipeline:
            frame = handler.apply(frame)

        return self.frame

    def __del__(self):
        self._source.release()
