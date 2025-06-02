# Face Recognition Attendance System

## Overview
This is a face recognition system that can register new faces, recognize known faces, and maintain attendance records. The system uses Python and popular computer vision libraries to perform these tasks.

## Project Structure
```
face-recognition-system/
├── encodings/
│   ├── encodings.pkl          # Stores facial encodings of registered users
├── known_faces/
│       └── Dev_1028.jpg        # Sample registered face image
├── src/
│   ├── __init__.py            # Python package initialization
│   ├── attendance.csv         # Attendance records
│   ├── attendance.py          # Attendance management module
│   ├── recognize.py           # Face recognition module
│   ├── register.py            # Face registration module
│   ├── utils.py               # Utility functions
│   └── requirements.txt       # Project dependencies
```

## Features
- Register new faces with name and ID
- Recognize registered faces in real-time
- Maintain attendance records with timestamps
- Simple and intuitive command-line interface

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/tirgardev/face-recognition-system.git
   cd face-recognition-system
   ```

2. Install the required dependencies:
   ```bash
   pip install -r src/requirements.txt
   ```

3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r src/requirements.txt
   ```

## Usage

### Register a New Face
1. Run the registration script:
   ```bash
   python src/register.py
   ```

2. Follow the on-screen prompts:
   - Enter your name and ID when prompted
   - Look directly at the camera
   - Press 'q' to capture your face

3. The system will save your facial encodings for future recognition

### Recognize Faces
1. Run the recognition script:
   ```bash
   python src/recognize.py
   ```

2. The system will:
   - Access your webcam
   - Detect and recognize any registered faces
   - Mark attendance automatically
   - Display the recognized name and ID

3. Press 'q' to exit the recognition mode

### View Attendance
1. Attendance records are automatically saved to `src/attendance.csv`
2. You can open this file with any spreadsheet software or text editor

## Future Improvements
1. **Enhanced Security**: Add liveness detection to prevent spoofing with photos
2. **Database Integration**: Replace CSV files with a proper database system
3. **Web Interface**: Develop a Flask/Django web interface for remote access
4. **Multi-face Detection**: Improve handling of multiple faces in frame
5. **Performance Optimization**: Implement GPU acceleration for faster processing
6. **Mobile Compatibility**: Develop an Android/iOS version of the system
7. **Cloud Integration**: Add cloud storage for face encodings and attendance records
8. **Advanced Analytics**: Add reporting features and attendance analytics
9. **Access Control**: Integrate with door locks or access control systems
10. **Mask Detection**: Add functionality to detect face masks

## Troubleshooting
1. **Webcam not working**:
   - Ensure no other application is using the webcam
   - Check camera permissions for your operating system

2. **Dependency errors**:
   - Make sure you're using Python 3.8+
   - Try reinstalling requirements with `pip install --force-reinstall -r src/requirements.txt`

3. **Face not recognized**:
   - Ensure proper lighting during registration and recognition
   - Try registering again with different angles

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is open-source and available under the MIT License.

---
