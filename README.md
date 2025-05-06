
# 🗣️ Whisper Transcriber - Setup Guide (macOS & Windows)

This guide covers the exact steps we followed in this chat to install and run [OpenAI Whisper](https://github.com/openai/whisper) on **macOS** and **Windows**, using a virtual environment and avoiding interference with an existing Python 3.13 installation.

---

## ✅ Requirements

- Python 3.8 - 3.11 (Whisper is not compatible with Python 3.13)
- FFmpeg
- pip

---

## 🍎 macOS Setup

### 1. Install Homebrew (if not already installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo >> /Users/cartagenacorp/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/cartagenacorp/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
brew help
```

### 2. Install Python 3.10 with pyenv (recommended)

```bash
brew install pyenv
pyenv install 3.10.12
pyenv virtualenv 3.10.12 whisper-env
pyenv activate whisper-env
```

Or manually create a virtual environment:

```bash
python3.10 -m venv whisper-env
source whisper-env/bin/activate
```

### 3. Install FFmpeg

```bash
brew install ffmpeg
```

### 4. Install dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install torch torchaudio torchvision
pip install git+https://github.com/openai/whisper.git
```

---

## 🪟 Windows Setup

### 1. Install Python 3.10 or 3.11
Download from: https://www.python.org/downloads/

> ✅ Make sure to check "Add Python to PATH" during installation.

### 2. Create a virtual environment without affecting Python 3.13

```cmd
py -3.10 -m venv whisper-env
whisper-env\Scripts\activate
```

### 3. Install FFmpeg

1. Download FFmpeg from: https://www.gyan.dev/ffmpeg/builds/
2. Extract and copy the `bin` path (e.g., `C:\ffmpeg\bin`)
3. Add it to your system environment **Path** variable:
   - Control Panel → System → Advanced system settings → Environment Variables → Edit `Path`

4. Confirm installation:

```cmd
ffmpeg -version
```

### 4. Install dependencies

```cmd
pip install --upgrade pip setuptools wheel
pip install torch torchaudio torchvision
pip install git+https://github.com/openai/whisper.git
```

---

## ✅ Test Your Setup

With the virtual environment active, run your script or:

```bash
whisper yourfile.mp3 --model medium --language English
```

---

## 🧹 Deactivate Environment

```bash
deactivate
```
