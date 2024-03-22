import os
import requests
import moviepy.editor as mp
import time
from extraction_library import *

def download_video(url, output_path):
    """
    Download video from the given URL.
    """
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

def main(issue_number, issue_body):
    # Extract video URL from issue body
    video_url = None
    for line in issue_body.split('\n'):
        if "hertz-extractor/assets" in line:
            video_url = line.strip()
            break
    
    if not video_url:
        print("No video URL found in the issue body.")
        return
    
    # Download the video
    video_filename = f"video_{issue_number}.mp4"
    download_video(video_url, video_filename)
    
    # Process the video
    video_filename
    start_time = time.time()

    # Load the video file and find the magnitude of various frequencies over ten second chunks
    video = mp.VideoFileClip(video_filename)
    print("loaded video at " + video_filename)
    _, _, sr, _, DB, freqs = process_audio(video)
    extract_frequency_magnitude(DB, freqs, sr, 10)
    extract_frequency_magnitude(DB, freqs, sr, 12)
    extract_frequency_magnitude(DB, freqs, sr, 14)
    extract_frequency_magnitude(DB, freqs, sr, 20)
    extract_frequency_magnitude(DB, freqs, sr, 60)
    extract_frequency_magnitude(DB, freqs, sr, 100)
    extract_frequency_magnitude(DB, freqs, sr, 400)

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time: ", execution_time, " seconds")

    # Clean up downloaded video file
    os.remove(video_filename)

if __name__ == "__main__":
    import sys
    issue_number = 2
    issue_body = "https://github.com/reecpj/hertz-extractor/assets/54263157/90e17a45-f522-4864-8729-035e9cea9ca1"
    if len(sys.argv) == 3:
        issue_number = sys.argv[1]
        issue_body = sys.argv[2]
    main(issue_number, issue_body)
