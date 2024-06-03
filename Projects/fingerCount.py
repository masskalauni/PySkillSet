import cv2
import numpy as np
import math

def get_contours(frame):
    """
    Convert the frame to a binary image and find contours.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (35, 35), 0)
    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours, thresh

def count_fingers(frame, contours, thresh):
    """
    Count the number of fingers shown in the frame.
    """
    if len(contours) == 0:
        return 0

    max_contour = max(contours, key=cv2.contourArea)
    hull = cv2.convexHull(max_contour)
    hull_indices = cv2.convexHull(max_contour, returnPoints=False)
    defects = cv2.convexityDefects(max_contour, hull_indices)

    if defects is None:
        return 0

    finger_count = 0
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(max_contour[s][0])
        end = tuple(max_contour[e][0])
        far = tuple(max_contour[f][0])

        a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
        b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
        c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)

        angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))

        if angle <= math.pi / 2:
            finger_count += 1
            cv2.line(frame, start, end, [0, 255, 0], 2)
            cv2.circle(frame, far, 5, [0, 0, 255], -1)

    return finger_count

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        frame = cv2.flip(frame, 1)
        contours, thresh = get_contours(frame)
        finger_count = count_fingers(frame, contours, thresh)

        cv2.putText(frame, f'Fingers: {finger_count}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Finger Counting', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
