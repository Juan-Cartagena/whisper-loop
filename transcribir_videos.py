import os
import whisper

def transcribir_videos(directorio, salida):
    model = whisper.load_model("medium")  # Puedes usar "small" o "large" según tus recursos

    # Buscar todos los archivos de video en la carpeta
    for archivo in os.listdir(directorio):
        if archivo.lower().endswith((".mp4", ".mov", ".mkv", ".avi", ".flv", ".webm")):
            ruta_video = os.path.join(directorio, archivo)
            nombre_base = os.path.splitext(archivo)[0]
            archivo_salida = os.path.join(salida, f"{nombre_base}.srt")

            print(f"Transcribiendo {ruta_video}...")
            resultado = model.transcribe(ruta_video, task="transcribe", fp16=False)

            # Guardar en formato SRT
            with open(archivo_salida, "w", encoding="utf-8") as f:
                for segmento in resultado["segments"]:
                    f.write(f"{segmento['id'] + 1}\n")
                    f.write(f"{formatear_tiempo(segmento['start'])} --> {formatear_tiempo(segmento['end'])}\n")
                    f.write(f"{segmento['text'].strip()}\n\n")

            print(f"Subtítulos guardados en {archivo_salida}")

def formatear_tiempo(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segundos_restantes = segundos % 60
    return f"{horas:02}:{minutos:02}:{segundos_restantes:06.3f}".replace('.', ',')

# Configura las rutas
directorio_videos = "./videos"
directorio_salida = "./subtitulos"
os.makedirs(directorio_salida, exist_ok=True)

# Ejecuta la transcripción
transcribir_videos(directorio_videos, directorio_salida)
