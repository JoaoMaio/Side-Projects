from moviepy.editor import ImageClip, AudioFileClip, concatenate_audioclips, CompositeVideoClip

# Load the image
image = ImageClip("img.jpg")

music = "music"
# Load the audio tracks
audio1 = AudioFileClip(f"{music}/purrple-cat-equinox.mp3")
audio2 = AudioFileClip(f"{music}/purrple-cat-green-tea.mp3")
#audio3 = AudioFileClip("track3.mp3")


# Concatenate the audio tracks
combined_audio = concatenate_audioclips([audio1, audio2])

# Set the duration of the video clip to match the combined audio
video = image.set_duration(combined_audio.duration)

# Set the audio to the video
video = video.set_audio(combined_audio)

# Set the resolution (optional, if you want to resize)
#video = video.resize(height=720)  # You can specify width or height

# Export the video to an MP4 file
video.write_videofile("final_video.mp4", codec="libx264", fps=2)