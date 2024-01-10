from .step import Step
from .step import StepException
from yt_dlp import YoutubeDL


class DownloadCaptions(Step):
    def process(self, data, inputs):
        for url in data:
            ydl_opts = {
                 'writesubtitles': True,
                 'writeautomaticsub': True,
                 'skip_download': True,  # 只下載字幕
                 'subtitleslangs': ['en'],
                 'outtmpl': get_video_id()+".txt"
            }



            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                # subtitles = ydl.download([url])
                subtitles = info.get('subtitles', {})
                if subtitles:
                    # get subtitle
                    subtitles_text = ""
                    for lang, subtitle_list in subtitles.items():
                        for subtitle_info in subtitle_list:
                            subtitles_text += f"{subtitle_info['ext']} subtitles ({lang}):\n"
                            subtitles_text += subtitle_info['url'] + '\n\n'
                        # 將字幕文本保存到文件
                        output_file = f"subtitles_{info['id']}.txt"
                        with open(output_file, 'w', encoding='utf-8') as f:
                            f.write(subtitles_text)

                    break

