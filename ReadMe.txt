-----------------------------------------------------
Data Collection Report - Landslide
-----------------------------------------------------


Team Members:
1. Aditya Sharma - 2021A3PS2446P
2. Shivansh Jain - 2021AAPS1634P 
3. Aryan Bansal - 2021A7PS2776P


Sub-Topics:
1. California landslides
2. Ben Lomond Slide
3. Landslides of Highways 1 and 4
4. Landslides of Glenwood Canyon and King County


Introduction:
This report documents the collection of image data for deep learning assignment centered around  "Aerial Drone Footage of Landslides." 
Landslides are a critical geological hazard, and aerial drone footage provides a unique perspective for studying and understanding their dynamics. The dataset we have assembled aims to contribute valuable resources for research, analysis, and awareness in the field of geological and environmental sciences.
The directory encompasses 600 images that relate to the consequences of landslides within the aforementioned subtopics.




Data Collection Details:
------------------------
Video Sources:
- We sourced our data from the following video(s):
  - https://www.youtube.com/watch?v=WxuPIrbAx8Q 
  - https://www.youtube.com/watch?v=f7ZfpiuPzCA
  - https://www.youtube.com/watch?v=hcNd9_WkoTM
  - https://www.youtube.com/watch?v=Mi16DMgxyUU
  - https://www.youtube.com/watch?v=QzYjPU0Tp7w
  - https://www.youtube.com/shorts/M4xByCJtiqk
  - https://www.youtube.com/watch?v=CzrymETf9hY
  - https://youtu.be/kDYkPNrwQgo?si=6fToGl3cBePVqU_0
  - https://youtu.be/59JcDmbI1hw 


Image Extraction:
- We extracted frames from the video(s) to create the dataset.
- Frames were resized to meet the required specifications of 256x256 pixels.
- The following code was employed to extract and resize images:
    




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



Frame Naming Convention:
- Images in this dataset are named according to the following convention:
  - frame_[FrameNumber].jpg
  - Example: frame_001.jpg,frame_002.jpg, ...


Image Quality:
- We took great care to ensure high image quality.
- Screenshots were avoided to maintain image clarity.
- No watermarks or unnecessary text are present in the images.


Submission Details:
-------------------
- All 600 images are stored in the "landslide_dataset" folder within this directory.


Conclusion:
This dataset embodies an extensive compilation of top-quality images portraying the aftermath of a landslide , curated by our team. We have adhered to the assignment's requirements and guidelines to ensure the dataset's quality and relevance.
