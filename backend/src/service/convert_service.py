import os
from moviepy.editor import VideoFileClip  
from pathlib import Path

def get_downloads_folder() -> str:
    downloads_path = str(Path.home() / "Downloads")
    return downloads_path

def video_to_audio(video_path: str) -> str:
    """converte o arquivo de vídeo em mp3 e salva na pasta de downloads."""
    output_folder = get_downloads_folder()
    os.makedirs(output_folder, exist_ok=True)  

    audio_filename = os.path.splitext(os.path.basename(video_path))[0] + ".mp3"
    audio_path = os.path.join(output_folder, audio_filename)

    print(f"[DEBUG] Caminho do arquivo: {audio_path}")

    try:
        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile(audio_path) 
        print(f"[SUCESSO] Arquivo salvo em: {audio_path}")
        return audio_path
    except Exception as e:
        print(f"[ERRO] Falha ao converter vídeo para áudio: {e}")
        raise RuntimeError(f"Erro ao converter vídeo para áudio: {e}")