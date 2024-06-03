import cv2
import numpy as np

def detect_traffic_light(frame):
    """
    Detect the color of the traffic light in the frame.
    Returns 'red', 'yellow', 'green', or 'unknown'.
    """
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color ranges for red, yellow, and green in HSV
    red_lower = np.array([0, 70, 50])
    red_upper = np.array([10, 255, 255])
    yellow_lower = np.array([15, 150, 150])
    yellow_upper = np.array([35, 255, 255])
    green_lower = np.array([36, 50, 70])
    green_upper = np.array([89, 255, 255])

    # Create masks for each color
    red_mask = cv2.inRange(hsv_frame, red_lower, red_upper)
    yellow_mask = cv2.inRange(hsv_frame, yellow_lower, yellow_upper)
    green_mask = cv2.inRange(hsv_frame, green_lower, green_upper)

    # Calculate the number of pixels for each mask
    red_count = cv2.countNonZero(red_mask)
    yellow_count = cv2.countNonZero(yellow_mask)
    green_count = cv2.countNonZero(green_mask)

    # Determine which color has the most pixels
    if red_count > yellow_count and red_count > green_count:
        return 'red'
    elif yellow_count > red_count and yellow_count > green_count:
        return 'yellow'
    elif green_count > red_count and green_count > yellow_count:
        return 'green'
    else:
        return 'unknown'

def main():
    # Open a connection to the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Detect the traffic light color in the frame
        light_color = detect_traffic_light(frame)

        # Display the detected color on the frame
        cv2.putText(frame, f'Traffic Light: {light_color}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Show the frame
        cv2.imshow('Traffic Light Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
