import cv2
import numpy as np
import urllib.request
import requests
import time
from gtts import gTTS
from playsound import playsound
import os
import pygame

class ObjectDetector:
    def __init__(self, url, token, chat_id):
        self.url = url
        self.token = token
        self.chat_id = chat_id
        self.classes = self.load_classes('coco.names')  # Load the COCO class names

    def load_classes(self, class_file_name):
        with open(class_file_name, 'r') as f:
            classes = [line.strip() for line in f.readlines()]
        return classes

    def send_telegram_message(self, message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={message}"
        response = requests.get(url)
        return response.json()

    def send_telegram_photo(self, photo_path):
        url = f"https://api.telegram.org/bot{self.token}/sendPhoto"
        files = {'photo': open(photo_path, 'rb')}
        data = {'chat_id': self.chat_id}
        response = requests.post(url, files=files, data=data)
        self.send_telegram_message("Location: https://maps.app.goo.gl/F5mHT6k8527D4Gdy7")
        return response.json()

    def text_to_speech(self, text, filename):
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        # Initialize pygame
        pygame.init()

        # Specify the path to your MP3 file
        mp3_file_path = "detected_objects.mp3"

        # Load the MP3 file
        pygame.mixer.music.load(mp3_file_path)

        # Play the MP3 file
        pygame.mixer.music.play()

        # Keep the program running until the music finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(1)  # Adjust the delay as needed

        # Quit pygame
        pygame.quit()
        os.remove(filename)

    def detect_objects(self):
        cv2.namedWindow("Latest Frame", cv2.WINDOW_AUTOSIZE)
        net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
        layers_names = net.getLayerNames()
        output_layers = [layers_names[i - 1] for i in net.getUnconnectedOutLayers()]

        last_sent_time = time.time() - 10  # Ensure the first detection sends immediately

        while True:
            img_resp = urllib.request.urlopen(self.url)
            imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
            frame = cv2.imdecode(imgnp, -1)

            if frame is None:
                print("Failed to capture frame from URL")
                break

            blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)

            class_ids = []
            confidences = []
            boxes = []

            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        center_x = int(detection[0] * frame.shape[1])
                        center_y = int(detection[1] * frame.shape[0])
                        w = int(detection[2] * frame.shape[1])
                        h = int(detection[3] * frame.shape[0])
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)
                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
            font = cv2.FONT_HERSHEY_PLAIN
            colors = np.random.uniform(0, 255, size=(len(self.classes), 3))

            detected_labels = []

            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    class_id = class_ids[i]
                    class_name = self.classes[class_id]
                    label = f"{class_name}"
                    color = colors[class_id % len(colors)]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    cv2.putText(frame, label, (x, y + 30), font, 3, color, 3)
                    detected_labels.append(class_name)

            if detected_labels:
                text = ", ".join([f"{label} detected nearby" for label in detected_labels])
                self.text_to_speech(text, "detected_objects.mp3")

            cv2.imshow("Latest Frame", frame)
            key = cv2.waitKey(1)

            current_time = time.time()
            if detected_labels and (current_time - last_sent_time >= 10):
                cv2.imwrite("detected_frame.jpg", frame)
                self.send_telegram_photo("detected_frame.jpg")
                last_sent_time = current_time

            if key == ord('q'):
                break

        cv2.destroyAllWindows()


if __name__ == '__main__':
    TOKEN = '6999747461:AAETugIvrYsFGFu0B_eMRmpoXRD8csK9rSc'
    CHAT_ID = '6218964388'
    detector = ObjectDetector('http://192.168.60.42/cam-hi.jpg', TOKEN, CHAT_ID)
    detector.detect_objects()
