#!/usr/bin/env python3

import click
import os
import time

@click.command()
@click.option('--model', default='openai/whisper-base', help='ASR model to use for speech recognition. Default is "openai/whisper-base". Model sizes include base, small, medium, large, large-v2. Additionally, try appending ".en" to model names for English-only applications (not available for large).')
@click.option('--device', default='cuda:0', help='Device to use for computation. Default is "cuda:0". If you want to use CPU, specify "cpu".')
@click.option('--dtype', default='float32', help='Data type for computation. Can be either "float32" or "float16". Default is "float32".')
@click.option('--batch-size', type=int, default=8, help='Batch size for processing. This is the number of audio files processed at once. Default is 8.')
@click.option('--better-transformer', is_flag=True, help='Flag to use BetterTransformer for processing. If set, BetterTransformer will be used.')
@click.option('--chunk-length', type=int, default=30, help='Length of audio chunks to process at once, in seconds. Default is 30 seconds.')
@click.argument('audio_file', type=str)
def asr_cli(model, device, dtype, batch_size, better_transformer, chunk_length, audio_file):
    from transformers import pipeline
    import torch

    # Initialize the ASR pipeline
    pipe = pipeline("automatic-speech-recognition",
                    model=model,
                    device=device,
                    torch_dtype=torch.float16 if dtype == "float16" else torch.float32)

    if better_transformer:
        pipe.model = pipe.model.to_bettertransformer()

    # Perform ASR
    click.echo("Model loaded.")
    start_time = time.perf_counter()
    outputs = pipe(audio_file, chunk_length_s=chunk_length, batch_size=batch_size, return_timestamps=True)

    # Output the results
    click.echo(outputs)
    click.echo("Transcription complete.")
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    click.echo(f"ASR took {elapsed_time:.2f} seconds.")

    # Save ASR chunks to an SRT file
    audio_file_name = os.path.splitext(os.path.basename(audio_file))[0]
    srt_filename = f"{audio_file_name}.srt"
    with open(srt_filename, 'w') as srt_file:
        prev = 0
        for index, chunk in enumerate(outputs['chunks']):
            prev, start_time = seconds_to_srt_time_format(prev, chunk['timestamp'][0])
            prev, end_time = seconds_to_srt_time_format(prev, chunk['timestamp'][1])
            srt_file.write(f"{index + 1}\n")
            srt_file.write(f"{start_time} --> {end_time}\n")
            srt_file.write(f"{chunk['text'].strip()}\n\n")

def seconds_to_srt_time_format(prev, seconds):
    if not (isinstance(seconds, int) or isinstance(seconds, float)):
        seconds = prev
    else:
        prev = seconds
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    milliseconds = int((seconds - int(seconds)) * 1000)
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    return (prev, f"{hours:02d}:{minutes:02d}:{int(seconds):02d},{milliseconds:03d}")

if __name__ == '__main__':
    asr_cli()
