echo "Python <= 3.10 only!"
uv pip install -r requirements-gfx1010.txt --extra-index-url https://download.pytorch.org/whl/rocm5.2
echo
echo "Example usage:"
echo "HSA_OVERRIDE_GFX_VERSION=10.3.0 python3 insanely-fast-whisper.py --model distil-whisper/distil-medium.en audio.mp3"
