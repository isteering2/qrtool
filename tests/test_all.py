from app.generate import generate_qr
from app.scan import scan_qr
import os

def main():
    test_text = "Hello World!"
    qr_filename = "test_qr.png"

    print("1️⃣ Generating QR code...")
    generate_qr(test_text, qr_filename)

    print("2️⃣ Scanning QR code...")
    decoded_text = scan_qr(qr_filename)
    print(f"Decoded text: {decoded_text}")

    if decoded_text == test_text:
        print("✅ Test passed: decoded text matches original text")
    else:
        print("❌ Test failed: decoded text does not match")

    # Cleanup
    if os.path.exists(qr_filename):
        os.remove(qr_filename)
        print("🗑️ Test QR image removed")

if __name__ == "__main__":
    main()
