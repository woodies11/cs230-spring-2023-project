import os
from moviepy.editor import VideoFileClip
from moviepy.video.tools.drawing import color_gradient, TextClip


def add_timestamp(video_path):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Get the video duration
    duration = video_clip.duration

    # Define the text properties
    text_color = 'white'
    font_size = 30
    padding = 10

    # Iterate over each frame and add the timestamp
    timestamped_frames = []
    for t in range(int(duration * video_clip.fps)):
        frame = video_clip.get_frame(t / video_clip.fps)
        timestamp = video_clip.get_time() + 2  # Add 2 seconds to compensate for video loading time

        # Format the timestamp
        timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')

        # Create the text clip with the timestamp
        text_clip = TextClip(timestamp_str, fontsize=font_size, color=text_color,
                             method='label', size=video_clip.size)

        # Add a black semi-transparent background to the text clip
        bg = color_gradient(text_clip.size, p1=(0, 0), p2=(0, text_clip.h), col1=(0, 0, 0, 0), col2=(0, 0, 0, 0.7))
        bg_clip = TextClip("", size=text_clip.size).set_mask(bg)

        # Set the position of the timestamp at the bottom right corner
        timestamp_clip = CompositeVideoClip([bg_clip, text_clip.set_position(("right", "bottom"))])

        # Overlay the timestamp clip on the current frame
        result_frame = CompositeVideoClip([frame, timestamp_clip])

        # Append the modified frame to the list of timestamped frames
        timestamped_frames.append(result_frame)

    # Create a new video clip with the modified frames
    timestamped_video = concatenate_videoclips(timestamped_frames)

    # Get the original video file name and extension
    file_name, file_extension = os.path.splitext(video_path)

    # Generate the output file path
    output_path = f"{file_name}_timestamped{file_extension}"

    # Save the modified video clip to the same directory
    timestamped_video.write_videofile(output_path, codec='libx264', audio_codec="aac")


add_timestamp('./data/IMG_0005.MOV')
