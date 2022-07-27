import os
from os.path import abspath, basename, dirname, exists, isdir, isfile, join
from pathlib import Path

from moviepy.editor import VideoFileClip

# Caminho para os arquivos de video
INPUT_FILES = abspath(r"C:\Users\luizl\...")


def recursive_search_files(input_path=None):
    """A recursive function to search files in diretory."""
    for file in os.listdir(input_path):
        joined_path = abspath(join(input_path, file))
        if isdir(joined_path):
            sub_paths = recursive_search_files(input_path=joined_path)
            for sub_path in sub_paths:
                yield sub_path
            continue
        yield joined_path


def main():
    """A main function."""
    files = recursive_search_files(input_path=INPUT_FILES)
    files_dir_name = basename(INPUT_FILES)
    print(files_dir_name)
    print()
    for mp4_path in files:
        if isfile(mp4_path):
            avi_path: list[str, str] = mp4_path.split(files_dir_name)
            avi_path[1] = avi_path[1].replace(".mp4", ".avi")
            avi_path.insert(1, f"{files_dir_name}_converted")
            avi_path = abspath("".join(avi_path))
            if not exists(dirname(avi_path)):
                Path(dirname(avi_path)).mkdir(parents=True)
            clip = VideoFileClip(mp4_path)
            clip.set_start(t=5)  # does nothing, changes are lost
            print(avi_path)
            clip.write_videofile(
                avi_path,
                fps=24,
                threads=100,
                bitrate="800k",
                audio_codec="mp3",
                audio_bitrate="128",
                codec="h264_nvenc",
                # verbose=False,
                # logger=None,
                # audio=False,
            )


if __name__ == "__main__":
    main()
