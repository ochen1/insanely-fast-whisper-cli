# Insanely Fast Whisper (CLI)

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ochen1/insanely-fast-whisper-cli/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/downloads/)

Powered by 🤗 *Transformers* & *Optimum* and based on **[Vaibhavs10/insanely-fast-whisper](https://github.com/Vaibhavs10/insanely-fast-whisper)**.

**TL;DR** - 🎙️ Transcribe **300** minutes (5 hours) of audio in less than **10** minutes - with [OpenAI's Whisper Large v2](https://huggingface.co/openai/whisper-large-v2). Blazingly fast transcription is now a reality!⚡️

## Features

✨ **ASR Model**: Choose from different 🤗 Hugging Face ASR models, including all sizes of [openai/whisper](https://github.com/openai/whisper) and even use an English-only variant (for non-large models).

🚀 **Performance**: Customizable optimizations ASR processing with options for batch size, data type, and BetterTransformer, all from the comfort of your terminal! 😎

📝 **Timestamps**: Get an SRT output file with accurate timestamps, allowing you to create subtitles for your audio or video content.

## Installation

- Clone git repository with `git clone https://github.com/ochen1/insanely-fast-whisper-cli`
- Switch to that folder with `cd insanely-fast-whisper-cli/`
- (optional) Create a new Python environment with `python -m venv venv`
- (optional) Activate environment with `source venv/bin/activate`
- Install packages from requirements with `pip install -r requirements.txt`
- Run program with `python insanely-fast-whisper.py`

## Usage

```bash
insanely-fast-whisper --model openai/whisper-base --device cuda:0 --dtype float32 --batch-size 8 --better-transformer --chunk-length 30 your_audio_file.wav
```

- `model`: Specify the ASR model (default is "openai/whisper-base").
- `device`: Choose the computation device (default is "cuda:0").
- `dtype`: Set the data type for computation ("float32" or "float16").
- `batch-size`: Adjust the batch size for processing (default is 8).
- `better-transformer`: Use BetterTransformer for improved processing (flag).
- `chunk-length`: Define audio chunk length in seconds (default is 30).

## Example

Transcribing an audio file with English-only Whisper model and returning timestamps:

```bash
insanely-fast-whisper --model openai/whisper-base.en your_audio_file.wav
```

## Output

The tool will save an SRT transcription of your audio file in the current working directory.

## License

This project is licensed under the [MIT License](https://github.com/ochen1/insanely-fast-whisper-cli/blob/main/LICENSE).

## Acknowledgments

- This tool is powered by Hugging Face's ASR models, primarily Whisper by OpenAI.
- Optimizations are developed by [Vaibhavs10/insanely-fast-whisper](https://github.com/Vaibhavs10/insanely-fast-whisper).
- Developed by [@ochen1](https://github.com/ochen1).

## 📞 Contact

Have questions or feedback? Feel free to create an issue!

🌟 **Star this repository if you find it helpful!**

[![Star History Chart](https://api.star-history.com/svg?repos=ochen1/insanely-fast-whisper-cli&type=Date)](https://star-history.com/#ochen1/insanely-fast-whisper-cli&Date)

---

[![GitHub Issues](https://img.shields.io/github/issues/ochen1/insanely-fast-whisper-cli.svg)](https://github.com/ochen1/insanely-fast-whisper-cli/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/ochen1/insanely-fast-whisper-cli.svg)](https://github.com/ochen1/insanely-fast-whisper-cli/pulls)

🚀 Happy transcribing with Insanely Fast Whisper! 🚀
