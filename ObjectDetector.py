# # import cv2
# # import numpy as np
# # import cvlib as cv
# # from cvlib.object_detection import draw_bbox
# # import urllib.request
# # import subprocess
# #
# #
# # class LiveObjectDetector:
# #     def __init__(self, url):
# #         self.url = url
# #         self.window_name = "Object Detection"
# #
# #     def detect_objects(self):
# #         cv2.namedWindow(self.window_name, cv2.WINDOW_AUTOSIZE)
# #
# #         while True:
# #             # Read image from URL
# #             img_resp = urllib.request.urlopen(self.url)
# #             imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
# #             frame = cv2.imdecode(imgnp, -1)
# #
# #             # Perform object detection
# #             bbox, label, conf = cv.detect_common_objects(frame, confidence=0.5, model='yolov4')
# #
# #             # Draw bounding boxes and labels on the image
# #             output_image = draw_bbox(frame, bbox, label, conf)
# #
# #             # Display the resulting image
# #             cv2.imshow(self.window_name, output_image)
# #
# #             # Print object names and convert to speech
# #             if label:
# #                 object_name = label[0]  # Assuming only one object is detected
# #                 print("Detected Object:", object_name)
# #
# #                 # Convert object name to speech and play it using 'say' command
# #                 subprocess.run(['say', object_name])
# #
# #             # Press 'q' to exit
# #             if cv2.waitKey(1) & 0xFF == ord('q'):
# #                 break
# #
# #         cv2.destroyAllWindows()
# #
# #
# # if __name__ == "__main__":
# #     url = 'http://192.168.1.104/cam-hi.jpg'
# #     detector = LiveObjectDetector(url)
# #     detector.detect_objects()
#
#
# # import cv2
# # import numpy as np
# # import cvlib as cv
# # from cvlib.object_detection import draw_bbox
# # import urllib.request
# # import subprocess
# #
# #
# # class LiveObjectDetector:
# #     def __init__(self, url):
# #         self.url = url
# #         self.window_name = "Object Detection"
# #
# #     def detect_objects(self):
# #         cv2.namedWindow(self.window_name, cv2.WINDOW_AUTOSIZE)
# #
# #         while True:
# #             # Read image from URL
# #             img_resp = urllib.request.urlopen(self.url)
# #             imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
# #             frame = cv2.imdecode(imgnp, -1)
# #
# #             # Perform object detection
# #             bbox, label, conf = cv.detect_common_objects(frame, confidence=0.5, model='yolov4')
# #
# #             # Draw bounding boxes and labels on the image
# #             output_image = draw_bbox(frame, bbox, label, conf)
# #
# #             # Rotate the image (e.g., 90 degrees clockwise)
# #             output_image = cv2.rotate(output_image, cv2.ROTATE_90_CLOCKWISE)
# #
# #             # Display the resulting image
# #             cv2.imshow(self.window_name, output_image)
# #
# #             # Print object names and convert to speech
# #             if label:
# #                 object_name = label[0]  # Assuming only one object is detected
# #                 print("Detected Object:", object_name)
# #
# #                 # Convert object name to speech and play it using 'say' command
# #                 subprocess.run(['say', object_name])
# #
# #             # Press 'q' to exit
# #             if cv2.waitKey(1) & 0xFF == ord('q'):
# #                 break
# #
# #         cv2.destroyAllWindows()
# #
# #
# # if __name__ == "__main__":
# #     url = 'http://192.168.1.104/cam-hi.jpg'
# #     detector = LiveObjectDetector(url)
# #     detector.detect_objects()
#
#
# import cv2
# import numpy as np
# import cvlib as cv
# from cvlib.object_detection import draw_bbox
# import urllib.request
# import subprocess
#
#
# class LiveObjectDetector:
#     def __init__(self, url):
#         self.url = url
#         self.window_name = "Object Detection"
#
#     def detect_objects(self):
#         # Create a full-screen window
#         cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
#
#
#         # Set the window properties to full screen
#
#
#         while True:
#             # Read image from URL
#             img_resp = urllib.request.urlopen(self.url)
#             imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
#             frame = cv2.imdecode(imgnp, -1)
#
#             # Perform object detection
#             bbox, label, conf = cv.detect_common_objects(frame, confidence=0.5, model='yolov4')
#
#             # Draw bounding boxes and labels on the image
#             output_image = draw_bbox(frame, bbox, label, conf)
#
#             output_image = cv2.rotate(output_image, cv2.ROTATE_90_ANTICLOCKWISE)
#
#
#
#             # Display the resulting image
#             cv2.imshow(self.window_name, output_image)
#
#             # Print object names and convert to speech
#             if label:
#                 object_name = label[0]  # Assuming only one object is detected
#                 print("Detected Object:", object_name)
#
#                 # Convert object name to speech and play it using 'say' command
#                 subprocess.run(['say', object_name])
#
#             # Press 'q' to exit
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#
#         cv2.destroyAllWindows()
#
#
# if __name__ == "__main__":
#     url = 'http://192.168.1.104/cam-hi.jpg'
#     detector = LiveObjectDetector(url)
#     detector.detect_objects()


import cv2
import numpy as np
import cvlib as cv
from cvlib.object_detection import draw_bbox
import urllib.request
import subprocess


class LiveObjectDetector:
    def __init__(self, url):
        self.url = url
        self.window_name = "Object Detection"

    def detect_objects(self):
        # Create a window
        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)

        # Set the window properties to full screen
        cv2.setWindowProperty(self.window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        while True:
            # Read image from URL
            img_resp = urllib.request.urlopen(self.url)
            imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
            frame = cv2.imdecode(imgnp, -1)

            # Perform object detection
            bbox, label, conf = cv.detect_common_objects(frame, confidence=0.5, model='yolov3')

            # Draw bounding boxes and labels on the image
            output_image = draw_bbox(frame, bbox, label, conf)

            # Rotate the image (270 degrees clockwise)
            output_image = cv2.rotate(output_image, cv2.ROTATE_90_CLOCKWISE)
            output_image = cv2.rotate(output_image, cv2.ROTATE_90_CLOCKWISE)
            output_image = cv2.rotate(output_image, cv2.ROTATE_90_CLOCKWISE)

            # Display the resulting image
            cv2.imshow(self.window_name, output_image)

            # Print object names and convert to speech
            if label:
                object_name = label[0]  # Assuming only one object is detected
                print("Detected Object:", object_name)

                # Convert object name to speech and play it using 'say' command
                subprocess.run(['say', object_name])

            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()


if __name__ == "__main__":
    url = 'http://192.168.91.42/cam-hi.jpg'
    detector = LiveObjectDetector(url)
    detector.detect_objects()
