from youtube.pipeline.steps.get_video_list import GetVideoList
from youtube.pipeline.steps.step import StepException
from youtube.pipeline.pipeline import Pipeline

CHANNEL_ID = "UC5H-l11nc7q5XqMRtaU-oYA"


def main():
    inputs = {'channel_id': CHANNEL_ID}

    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
