import os
import whisper
import subprocess
import time

def obtener_duracion_video(ruta_video):
    """Retorna la duración del video en segundos usando ffprobe."""
    try:
        resultado = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries",
             "format=duration", "-of",
             "default=noprint_wrappers=1:nokey=1", ruta_video],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        return float(resultado.stdout)
    except Exception as e:
        print(f"No se pudo obtener la duración del video: {e}")
        return 0.0

def transcribir_videos(directorio, salida):
    model_name = "small"  # Cambia a "medium" o "large" si es necesario
    model = whisper.load_model(model_name)

    for archivo in os.listdir(directorio):
        if archivo.lower().endswith((".mp4", ".mov", ".mkv", ".avi", ".flv", ".webm")):
            ruta_video = os.path.join(directorio, archivo)
            nombre_base = os.path.splitext(archivo)[0]
            archivo_salida = os.path.join(salida, f"{nombre_base}.srt")

            duracion = obtener_duracion_video(ruta_video)
            print(f"\n📁 Procesando: {archivo}")
            print(f"🕒 Duración del video: {duracion:.2f} segundos")
            print(f"🧠 Modelo usado: Whisper {model_name}")

            inicio = time.time()
            resultado = model.transcribe(ruta_video, task="transcribe", fp16=False)
            fin = time.time()
            tiempo_transcripcion = fin - inicio

            with open(archivo_salida, "w", encoding="utf-8") as f:
                for segmento in resultado["segments"]:
                    f.write(f"{segmento['id'] + 1}\n")
                    f.write(f"{formatear_tiempo(segmento['start'])} --> {formatear_tiempo(segmento['end'])}\n")
                    f.write(f"{segmento['text'].strip()}\n\n")

            print(f"✅ Subtítulos guardados en: {archivo_salida}")
            print(f"⏱️ Tiempo de transcripción: {tiempo_transcripcion:.2f} segundos")

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
