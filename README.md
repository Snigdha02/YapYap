# YapYap  : The Audio-to-Text Conversion App

This Python app converts audio files into text using the Whisper model and saves the transcribed text into a Word document.

## Requirements

To install the necessary Python libraries, run:
``` pip install -r requirements.txt ```

### How to Use

1. Place your audio file (preferably `.mp3` or `.m4a` or `.wav`) in the `audio` directory and provide the filename when prompted.
2. Run the app using the following command:

``` python app.py ```

3. The app will:
   - Convert the audio file into text.
   - Prompt you to enter a filename for the Word document.
   - Save the transcribed text in the specified Word document created in `output`.

### Example

You can test the app with a sample audio file, `Sample.m4a`, provided in the `audio` folder.

### Notes

- This app uses Whisper model by OpenAI.
- You can use other formats like `.mp3` or `.flac` or `.m4a`, but they will be converted to `.wav` format during processing.
- This app also handles multiple languages.

### Future Aspects

 - Adding the feature of real time transcribing
 - Improving the model without additional loads on CPU