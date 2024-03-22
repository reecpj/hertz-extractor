import os
import requests
import subprocess

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
        if line.strip().startswith('Video URL:'):
            video_url = line.split(':', 1)[1].strip()
            break
    
    if not video_url:
        print("No video URL found in the issue body.")
        return
    
    # Download the video
    video_filename = f"video_{issue_number}.mp4"
    download_video(video_url, video_filename)
    
    # Process the video
    video_info = video_filename
    print("Video Information:")
    print(video_info)

    # Clean up downloaded video file
    os.remove(video_filename)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python process_video.py <issue_number> <issue_body>")
        sys.exit(1)
    issue_number = sys.argv[1]
    issue_body = sys.argv[2]
    main(issue_number, issue_body)
