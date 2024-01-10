from youtube.pipeline.steps.get_video_list import GetVideoList
from youtube.pipeline.steps.step import StepException
from youtube.pipeline.pipeline import Pipeline
from youtube.pipeline.steps.download_caption import DownloadCaptions

CHANNEL_ID = "UCxJGMJbjokfnr2-s4_RXPxQ"


def main():
    inputs = {'channel_id': CHANNEL_ID}

    steps = [
        GetVideoList(),
        DownloadCaptions(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
