# StegoHide

StegoHide is a desktop application for hiding and extracting text inside digital images using **least significant bit (LSB) steganography**. It provides a simple graphical interface for selecting an image, embedding a message, saving the resulting image, and recovering the hidden message later.

The project was developed as an educational demonstration of how information can be concealed in image pixels while keeping the image visually similar to the original.

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-1f6feb)
![Image Processing](https://img.shields.io/badge/Image%20Processing-Pillow-8A2BE2)

## Features

- Hide plain-text messages inside PNG, JPG, and JPEG images.
- Extract hidden messages from encoded images.
- Use a graphical interface built with CustomTkinter.
- Preview the selected image before encoding or decoding.
- Save encoded output as a PNG file.
- Switch between light and dark appearance modes.
- Validate whether the selected image has enough pixel capacity for a message.

## How It Works

StegoHide uses RGB images and stores one message bit in the least significant bit of each color channel:

1. The message is converted into 8-bit character values.
2. A delimiter is appended to mark the end of the message.
3. The message bits are written into the red, green, and blue channels of the image pixels.
4. During extraction, the least significant bits are read in the same order.
5. The delimiter identifies where the original message ends.

Because only the least significant bit of each color channel is changed, the encoded image should look almost identical to the source image under normal viewing conditions.

### Capacity

For an image with width $W$ and height $H$, the current implementation provides approximately:

```text
W x H x 3 bits
```

of storage before accounting for the delimiter and character encoding. Larger images can therefore store longer messages.

## Project Structure

```text
steganography_G/
|-- backend.py       # Image selection, encoding, decoding, and file operations
|-- main.py          # CustomTkinter graphical user interface and application entry point
|-- module1.py       # Earlier duplicate implementation retained for reference
|-- requirements.txt  # Python dependencies
|-- README.md         # Project documentation
```

`main.py` is the recommended entry point. The active application imports its functionality from `backend.py`.

## Requirements

- Python 3.9 or newer
- Tkinter, usually included with standard Python installations
- Pillow
- CustomTkinter

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/steganography_G.git
cd steganography_G
```

Replace `<your-username>` with your GitHub username and adjust the repository name if necessary.

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Running the Application

```bash
python main.py
```

### Encoding a message

1. Select **Encode** from the home screen.
2. Choose a source image.
3. Enter the message to hide.
4. Select **Save Encoded Image**.
5. Save the result as a PNG file.

### Decoding a message

1. Select **Decode** from the home screen.
2. Choose an encoded image.
3. Select **Extract Message**.
4. Read the recovered message in the text area.

## Important Limitations

- This is a steganography demonstration, not an encryption system. Messages are stored as plain text bits and are not cryptographically protected.
- The current implementation is intended for lossless output, especially PNG. Saving an encoded image through a lossy JPEG workflow can destroy hidden bits.
- The message format currently converts each Python character to 8 bits using `ord()`. Non-ASCII text may not round-trip reliably.
- Extraction depends on the delimiter used by the current implementation. An image without that delimiter may produce an empty or unexpected result.
- The application does not currently authenticate or verify that an image was produced by StegoHide.

For sensitive information, encrypt the message before embedding it and use a secure key-management method.

## Development Notes

The encoding and decoding logic is separated from the user interface in `backend.py`, making the core functionality easier to test or reuse in another interface. A future production-oriented version could add automated tests, UTF-8 message support, password-based encryption, capacity reporting, and stronger message-integrity checks.

## Academic Context

This project demonstrates:

- Basic digital image representation through RGB pixels.
- Binary conversion and bitwise operations.
- Least significant bit steganography.
- Event-driven GUI programming with Tkinter and CustomTkinter.
- Separation of presentation logic from image-processing logic.
- File handling and user-input validation in a desktop application.

## License

No license has been specified yet. Add a license before accepting external contributions or presenting the repository as reusable open-source software.
