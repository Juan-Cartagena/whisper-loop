import os
import whisper

def transcribir_videos(directorio, salida):
    model = whisper.load_model("medium")  # Usa "medium" large o "small" si tienes menos recursos
    
    for i in range(2, 17):  # Clases de 1 a 16
        archivo_video = os.path.join(directorio, f"Clase {i}.mp4")
        archivo_salida = os.path.join(salida, f"Clase_{i}.txt")
        
        if os.path.exists(archivo_video):
            print(f"Transcribiendo {archivo_video}...")
            resultado = model.transcribe(archivo_video)
            
            with open(archivo_salida, "w", encoding="utf-8") as f:
                f.write(resultado["text"])
            print(f"Transcripción guardada en {archivo_salida}")
        else:
            print(f"Archivo no encontrado: {archivo_video}")

# Configura las rutas
directorio_videos = "./videos"  # Cambia esto a donde estén los archivos
directorio_salida = "./transcripciones"
os.makedirs(directorio_salida, exist_ok=True)

# Ejecuta la transcripción
transcribir_videos(directorio_videos, directorio_salida)
