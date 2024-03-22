import moviepy.editor as mp
import time
from extraction_library import *

start_time = time.time()
# Path to your video file
video_path = 'D:/Videos/Downloaded/Theo/Coca-Cola Holidays Are Coming 2020.mp4'

# Load the video file and find the magnitude of various frequencies over ten second chunks
video = mp.VideoFileClip(video_path)
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