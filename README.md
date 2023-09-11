# Body Measurement Model
This Python script captures video from a webcam and measures various body dimensions using pose detection. It utilizes the `cvzone` PoseModule along with OpenCV to identify key body points and compute measurements.

## Dependencies

- Python 3.x
- OpenCV
- `cvzone` library

## Usage

- Make sure you have all the required dependencies installed.
- Run the script.
- A window will open, displaying the webcam feed with rectangles around detected body parts.
- Stand in front of the webcam with your full body visible for accurate measurements.
- Keep still for a few seconds to allow the script to capture your pose.
- After a short period, the script will print out various body measurements.

## Constants

- `BODY_PARTS`: This dictionary maps body part names to their respective index numbers as identified by the PoseDetector.

## Adjustable Parameters

- `rect_size`: This parameter sets the size of rectangles drawn around detected body parts. Adjusting it can improve the precision of measurements.

## Body Measurements

The script provides the following measurements:

- Shoulder to Hip Length
- Shoulder to Shoulder Length
- Waist Measurement
- Neck Girth
- Right Forearm Length
- Left Forearm Length
- Right Upperarm Length
- Left Upperarm Length
- Arm Length
- Sleeve Length

## Example Output
<img width="473" alt="image" src="https://github.com/Dhriti-Roy/Body-Measurement-Model/assets/74097309/478bfbd0-3577-4e01-a250-c7c7eeb1232a">
<img width="473" alt="image" src="https://github.com/Dhriti-Roy/Body-Measurement-Model/assets/74097309/f947056a-8d7e-491a-8069-b5e370e5721e">





## Notes

- Ensure good lighting conditions and stand with a clear background for accurate measurements.
- The measurements may vary based on the pose detection accuracy.

## Author

- Dhriti

## License

This code is provided under the [MIT License](LICENSE). Feel free to use and modify it for your own purposes.

---

For any questions or issues, please contact [Author](mailto:author@email.com).

