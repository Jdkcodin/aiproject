from flask import Flask, render_template, request, send_file
from flask_mail import Mail, Message
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "knowledgehub132@gmail.com" 
app.config["MAIL_PASSWORD"] = "xsztdosinudrgnmy"  


mail = Mail(app)

# Paths 
TEMPLATE_PATH = os.path.join("static", "WhatsApp Image 2025-04-11 at 21.25.01_e4b0b716.jpg")
FONT_PATH = os.path.join("static", "ABeeZee-Regular.otf")
OUTPUT_PATH = os.path.join("static", "generated_certificate.png")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form inputs
        name = request.form.get("name", "Unnamed")
        course = request.form.get("course", "No Course Provided")
        date = request.form.get("date", "No Date Provided")
        email = request.form.get("email")  # Get recipient email

        if not email:
            return "Error: Email address is required!"

        # Open the certificate template
        if not os.path.exists(TEMPLATE_PATH):
            return "Error: Certificate template not found!"

        img = Image.open(TEMPLATE_PATH)
        draw = ImageDraw.Draw(img)

        try:
            # Load font
            if not os.path.exists(FONT_PATH):
                return "Error: Font file not found!"
            font_large = ImageFont.truetype(FONT_PATH, 60)
            font_small = ImageFont.truetype(FONT_PATH, 40)

            # Set positions
            name_position = (470, 420)
            course_position = (1242, 1111)
            date_position = (713, 1090)

            # Auto-center name
            text_width, _ = draw.textbbox((0, 0), name, font=font_large)[2:]
            #name_position = ((img.width - text_width) // 2, 380)

            # Draw text on the certificate
            text_color = (0, 0, 0)
            draw.text(name_position, name, fill=text_color, font=font_large)
            draw.text(course_position, f"Completed: {course}", fill=text_color, font=font_small)
            draw.text(date_position, f"Date: {date}", fill=text_color, font=font_small)

            # Save the generated certificate
            img.save(OUTPUT_PATH)

            # Send email with attachment
            msg = Message("Your Certificate", recipients=[email])
            msg.body = f"Hello {name},\n\nPlease find your certificate attached.\n\nBest regards,\nPowered by AI "
            with open(OUTPUT_PATH, "rb") as cert:
                msg.attach("certificate.png", "image/png", cert.read())
            mail.send(msg)

            return f"Certificate sent to {email}!"

        except Exception as e:
            return f"Error: {e}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
