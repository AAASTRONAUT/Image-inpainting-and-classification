import cv2
import os

# Function to extract every 5th frame from a video and resize them
def extract_frames(video_path, output_folder, target_width, target_height , frame_frequency , v_num ,crop , crop_params = [1 ,1 , 1, 1]):
    # Opening the video file
    cap = cv2.VideoCapture(video_path)

    # Checking if the video opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video.")
        return

    # Creating the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_count = len(os.listdir("landslide_dataset"))

    frame_counter = 0

    # Loop through frames, resize, and save every 5th frame as an image
    while True:
        ret, frame = cap.read()

        if not ret:
            break  # Break the loop if we reach the end of the video

        if frame is None:
            print("Warning: Empty frame encountered.")
            continue

        # Only save every frame_frequency'th frame
        if frame_counter % frame_frequency == 0:
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            # Resizing the cropped frame to the target width and height
            resized_frame = cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_LINEAR)

            # Saving the resized frame as an image
            frame_filename = os.path.join(output_folder, f"Image_{frame_count}.jpg")
            cv2.imwrite(frame_filename, resized_frame)

            frame_count += 1

        frame_counter += 1

    # Releasing the video capture object and close any OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
    print(f"Extraction done")

output_folder = "landslide_dataset" 
target_width = 256
target_height = 256
v_num = 0

for video in os.listdir("/Users/shivansh/Downloads/videos"):
        video_path = os.path.join("/Users/shivansh/Downloads/videos" , video) 
        v_num += 1
        extract_frames(video_path, output_folder, target_width, target_height , 50 ,v_num ,False)