# EchoSight-Vision-For-Blind


This project introduces a revolutionary IoT-based smart blind stick designed to empower visually impaired individuals by providing real-time information about their environment. The device utilizes a combination of ultrasonic sensors, a soil moisture sensor, an ESP32 microcontroller, and a YOLOv3-powered camera to detect obstacles, measure soil moisture levels, and identify objects in the user's surroundings.

**Key Features:**

**Obstacle Detection**: Ultrasonic sensors provide accurate detection of obstacles in the user's path, generating audible alerts of varying frequency to indicate the proximity of objects.

**Soil Moisture Measurement:** A soil moisture sensor enables users to assess the moisture content of their surroundings, aiding in tasks such as gardening or navigating through potentially wet areas.

**Object Identification**: An ESP32-powered camera, equipped with the YOLOv3 object detection model, identifies objects in the user's field of vision. The device then provides verbal descriptions of detected objects and their approximate locations through a built-in speaker.

**Telegram Integration**: Real-time information, including object descriptions and locations, is transmitted to a pre-configured Telegram bot. This allows users to share their environment with caregivers or friends, fostering a sense of connectedness and independence.


**Technical Implementation:**

**Hardware Components:** 
                        ESP32 microcontroller, ultrasonic sensors, soil moisture sensor, camera, buzzer, and speaker.

**Software:** 
             YOLOv3 object detection model, custom firmware for the ESP32, Telegram bot integration,Arduino IDE and Embedded C, Python.

**Workflow:** 
             Ultrasonic sensors detect obstacles, triggering audible alerts. The soil moisture sensor measures moisture levels and provides corresponding feedback. The camera captures images, which are processed by the YOLOv3 model to identify objects. Object descriptions and locations are then transmitted to the Telegram bot.


**Benefits:**

**Enhanced Safety**: The smart blind stick significantly improves the safety and mobility of visually impaired individuals by providing timely information about their surroundings.

**Increased Independence**: By enabling users to navigate their environment more confidently, the device promotes a greater sense of independence and self-sufficiency.

**Environmental Awareness**: The soil moisture sensor empowers users to make informed decisions about their interactions with the environment, such as gardening or avoiding potentially hazardous areas.

**Social Connection**: The integration with Telegram allows users to share their experiences and connect with others, fostering a sense of community and support.

**Future Work:**

Explore additional sensor modalities, such as temperature and humidity sensors, to provide more comprehensive environmental information.
Investigate the potential for integrating haptic feedback to enhance the user experience.
Expand the object detection capabilities to include a wider range of objects and environments.
Investigate the feasibility of integrating with other assistive technologies, such as smart home systems.


 
**Research Paper Publish Link** - https://ijircce.com/admin/main/storage/app/pdf/uTl4zznb7H4FInG2oSPw1KDaX0JYOcEfT39hCt1a.pdf
