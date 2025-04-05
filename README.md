# 🧠 Facial Recognition Attendance System

A complete **Python + MySQL** based attendance system that uses **real-time facial recognition** to automate and manage student attendance efficiently.

---

## 🔥 Highlight Features

- 🧑‍🎓 **Student Manager** – Register, update, and delete student details via GUI.
- 📷 **Face Dataset Generator** – Capture multiple images per student using webcam.
- 🧠 **Face Model Trainer** – Train recognition model using OpenCV’s LBPH algorithm.
- 🧾 **Real-Time Recognition** – Detect and identify faces live from webcam.
- 📅 **Attendance Logger** – Automatically logs attendance with time and date.
- 📁 **CSV Export** – Save daily attendance in spreadsheet-friendly format.
- 🛢️ **MySQL Backend** – Securely store student and attendance data.

---

## ⚙️ Technologies Used

| Tech             | Role                               |
|------------------|-------------------------------------|
| **Python 3.x**   | Main Programming Language           |
| **OpenCV**       | Face Detection & Recognition        |
| **Tkinter**      | GUI Framework                       |
| **MySQL**        | Backend Database                    |
| **Pillow**       | Image Processing                    |
| **NumPy**        | Numerical Operations                |
| **CSV, Datetime**| Attendance Logging & Export         |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shivakantkurmi/Face-Recognition.git
cd Facial-Recognition-Attendance
```

### 2️⃣ Install Required Libraries

```bash
pip install opencv-python mysql-connector-python numpy pillow
```
### Connect Mysql Workbench 


## 🧩 Module Breakdown

| Module File           | Purpose                                     |
|------------------------|---------------------------------------------|
| `main.py`              | GUI Homepage for navigation                 |
| `student.py`           | Add / Edit / Delete student info            |
| `dataset_generator.py` | Capture facial images for training dataset  |
| `trainer.py`           | Train recognizer using LBPHFaceRecognizer   |
| `recognizer.py`        | Recognize faces and log attendance          |
| `attendance.py`        | View and export attendance records          |

---

## 📸 UI Preview

| Main Menu | Register Student | Face Detection |
|-----------|------------------|----------------|
| ![Main](https://github.com/user-attachments/assets/455cd9a2-adbf-4ff7-b64b-886603f6b53d) | ![Register](https://github.com/user-attachments/assets/1fdaa51e-3b27-407b-b1eb-356ff3fc9d12) | ![Detect](https://github.com/user-attachments/assets/937afb00-95ee-4b1a-897e-a9cbc4276fe5) |

---

## 📜 License

Licensed under the **MIT License**.

---

## 🙌 Contributions

Pull requests are welcome! For major changes, open an issue to discuss improvements first.

---

**Built with 💻 Python and ❤️ for smart automation in education.**

