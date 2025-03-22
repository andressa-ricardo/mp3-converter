import os
from moviepy.editor import VideoFileClip  

def video_to_audio(video_path: str, output_folder: str) -> str:
    os.makedirs(output_folder, exist_ok=True)  

    audio_filename = os.path.splitext(os.path.basename(video_path))[0] + ".mp3"
    audio_path = os.path.join(output_folder, audio_filename)

    try:
        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile(audio_path) 
        return audio_path
    except Exception as e:
        raise RuntimeError(f"Erro ao converter vídeo para áudio: {e}")
