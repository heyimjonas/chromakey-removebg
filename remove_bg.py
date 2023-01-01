import cv2
import numpy as np


def remove_background(video_path, background_image_path, output_path):
    # Load the background image
    background = cv2.imread(background_image_path)
    if background is None:
        print("Error: Background image not found.")
        return

    # Initialize video capture
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Resize background to match video frame size
    background = cv2.resize(background, (frame_width, frame_height))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"wav1")
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Define the green color range for chroma keying
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to HSV for better color segmentation
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask for green color
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # Refine the mask
        mask = cv2.medianBlur(mask, 5)
        mask_inv = cv2.bitwise_not(mask)

        # Extract the foreground
        foreground = cv2.bitwise_and(frame, frame, mask=mask_inv)

        # Extract the background from the background image
        background_part = cv2.bitwise_and(background, background, mask=mask)

        # Combine foreground and new background
        combined = cv2.add(foreground, background_part)

        # Write the frame to the output video
        out.write(combined)

        # Display the result in real-time
        cv2.imshow("Dynamic Background Removal", combined)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Processed video saved as {output_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Dynamic Background Removal using Chroma Keying."
    )
    parser.add_argument(
        "--video",
        type=str,
        required=True,
        help="Path to the input video with green screen.",
    )
    parser.add_argument(
        "--background", type=str, required=True, help="Path to the background image."
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output.mp4",
        help="Path to save the output video.",
    )
    args = parser.parse_args()

    remove_background(args.video, args.background, args.output)
