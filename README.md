# Gaze-Glide 👁️🦽
### Eye-Gaze Controlled Wheelchair

## 📌 Project Overview
Gaze-Glide is an assistive mobility system designed to give individuals with limited physical movement — particularly ALS patients — autonomous control over a wheelchair using only eye movements. The system uses an IR camera to capture gaze direction, a custom-trained deep learning model to classify that gaze, and a Raspberry Pi-based control system to translate it into safe, smooth wheelchair movement.

## 🎯 Objectives
- Design a highly accurate eye-gaze detection system that works across varied lighting conditions
- Develop a smooth motion/acceleration model to prevent abrupt, unsafe movement
- Enhance user safety and comfort through obstacle detection and an intuitive interface

## 🛠️ Tech Stack & Components
- **Software:** Python, CNN (with attention-based layers) for gaze classification
- **Hardware:** IR camera, Raspberry Pi, motor drivers, servo mechanism, microcontroller
- **Techniques:** Computer vision, real-time signal processing, state machine-based movement decisions

## 🏗️ System Architecture
`User → IR Camera → Raspberry Pi → Deep Learning Model (gaze classification) → State Machine → Motor Driver → Wheelchair Movement`, with a parallel path for remote monitoring via a server and microcontroller.

*(Insert the architecture diagram image here — pull it out of the PDF as `architecture.png` and embed with `![Architecture](architecture.png)`)*

## 🧠 Methodology
1. Collected eye-movement data (left/right/up/down/center) in both simulated and real environments
2. Trained a CNN with attention mechanisms to classify gaze direction robustly across lighting conditions
3. Deployed the model on a Raspberry Pi for real-time inference
4. Translated gaze output into directional motor commands, with safety protocols (obstacle detection, smooth acceleration)

## 📊 Target Performance Metrics
- **Gaze detection accuracy:** ≥ 90%
- **Response time:** < 500 ms (gaze input → movement)
- **Battery life:** 4+ hours continuous operation
- **Usability:** < 10 min learning curve

## 👥 Team
- Siva NS
- Snehith Sujish
- Sreelakshmi TR
- Nanda Kishore A
- **Guide:** Anu TP

*Vidya Academy of Science and Technology*

## 📄 Project Report
Full project presentation/report available in [`Gaze-Glide-Project-Report.pdf`](./Gaze-Glide-Project-Report.pdf)

## 🔭 Future Work
- Obstacle avoidance and autonomous navigation
- Scaling from prototype to a full-sized wheelchair
