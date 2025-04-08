
# 🗣️ Whisper Transcriber - Instalación y Uso

Este proyecto utiliza [OpenAI Whisper](https://github.com/openai/whisper) para transcribir archivos de audio o video a texto de forma automática. A continuación encontrarás los pasos para instalarlo en **macOS** y **Windows**, asegurando compatibilidad sin afectar otras versiones de Python instaladas en el sistema (como Python 3.13).

---

## ✅ Requisitos

- Python 3.8 - 3.11 (NO es compatible con Python 3.13)
- FFmpeg
- pip

---

## 📦 Instalación en macOS

### 1. Instalar Python 3.10 (sin afectar el sistema)
Usamos `pyenv` para manejar múltiples versiones de Python.

```bash
brew install pyenv
pyenv install 3.10.12
pyenv virtualenv 3.10.12 whisper-env
pyenv activate whisper-env
```

> Si no tienes Homebrew:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Instalar FFmpeg

```bash
brew install ffmpeg
```

### 3. Clonar el proyecto y crear entorno virtual (si no usas pyenv)

```bash
python3.10 -m venv whisper-env
source whisper-env/bin/activate
```

### 4. Instalar dependencias

```bash
pip install --upgrade pip setuptools wheel
pip install torch torchaudio torchvision
pip install git+https://github.com/openai/whisper.git
```

---

## 🪟 Instalación en Windows

### 1. Instalar Python 3.10 o 3.11 desde:
👉 https://www.python.org/downloads/

> ⚠️ Asegúrate de activar la casilla **"Add Python to PATH"** durante la instalación.

### 2. Crear entorno virtual sin afectar Python 3.13

```cmd
py -3.10 -m venv whisper-env
whisper-env\Scripts\activate
```

### 3. Instalar FFmpeg

1. Descargar desde: https://www.gyan.dev/ffmpeg/builds/
2. Extraer y copiar la ruta del directorio `bin` (por ejemplo: `C:\ffmpeg\bin`)
3. Agregar esa ruta a la variable de entorno **PATH**:
   - Panel de control → Sistema → Configuración avanzada del sistema → Variables de entorno → Editar `Path`

4. Verifica con:

```cmd
ffmpeg -version
```

### 4. Instalar dependencias

```cmd
pip install --upgrade pip setuptools wheel
pip install torch torchaudio torchvision
pip install git+https://github.com/openai/whisper.git
```

---

## 🎬 Cómo usar

Con el entorno virtual activado:

```bash
whisper ruta/al/archivo.mp3 --model medium --language Spanish
```

Para uso dentro de scripts Python, asegúrate de que el entorno esté activo y usa:

```python
import whisper
model = whisper.load_model("medium")
result = model.transcribe("archivo.mp3", language="Spanish")
print(result["text"])
```

---

## 🧹 Recomendación

Cuando termines de usar el entorno virtual, puedes desactivarlo con:

```bash
deactivate
```

---

## 📂 Estructura sugerida del proyecto

```
whisper-loop/
├── whisper-env/         # Entorno virtual (exclúyelo del repositorio)
├── transcribir_videos.py
├── README.md
```

> Recuerda agregar `whisper-env/` a tu archivo `.gitignore`.

---

## 🚀 Créditos

- [OpenAI Whisper](https://github.com/openai/whisper)
- [FFmpeg](https://ffmpeg.org/)
