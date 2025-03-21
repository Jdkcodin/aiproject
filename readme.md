# 🎓 Certificate Generator with Email Sending

This project is a **Flask-based web application** that generates certificates based on user input and sends them via **email** as an attachment.

## 📌 Features
👉 User enters **Name, Course, Date, and Email**.  
👉 Generates a **certificate image** with the provided details.  
👉 **Automatically sends the certificate** as an email attachment.  
👉 Uses **Flask-Mail** for email functionality.  

---

## 🛠️ Installation & Setup

### ** Step 1: Clone the Repository**
```sh
git clone https://github.com/your-username/certificate-generator.git
cd certificate-generator
```

### ** Step 2: Install Dependencies**
```sh
pip install -r requirements.txt
```
(If `requirements.txt` is not available, install manually)
```sh
pip install Flask Flask-Mail Pillow
```

### **🔹Step 3: Set Up Email Configuration**
1. Go to [Google Account Security](https://myaccount.google.com/security) and **enable 2-Step Verification**.  
2. Generate an **App Password** from [Google App Passwords](https://myaccount.google.com/apppasswords).  
3. Copy the **16-character App Password** and **update `app.py`**:

```python
app.config["MAIL_USERNAME"] = "your-email@gmail.com"
app.config["MAIL_PASSWORD"] = "your-app-password"
```

---

## 🚀 Running the Application
Run the Flask app:
```sh
python app.py
```
Then, open in your browser:
```sh
http://127.0.0.1:5000/
```


---

## 📄 File Structure
```
📺 certificate-generator
│── 📂 static
│   ├── certificate_template.png  # Template for certificates
│   ├── generated_certificate.png # Generated certificates
│   ├── arial.ttf                 # Font file for text placement
│── 📂 templates
│   ├── index.html                 # HTML form for input
│── app.py                          # Flask application
│── requirements.txt                 # Dependencies
│── README.md                        # Project documentation
```

---

## ⚙️How It Works
🔢 User **fills out the form** with Name, Course, Date, and Email.  
🔢 Flask **generates a certificate image** with the details.  
🔢 The generated certificate **is saved** in `/static/`.  
🔢 Flask-Mail **sends the certificate** as an email attachment.  

---

## 📧 Email Setup Guide
- The sender **must use an App Password**, NOT their real Gmail password.  
- If using another email provider (Yahoo, Outlook), update SMTP settings in `app.py`.  

---

## ❓ Troubleshooting
🚫 **App Password Not Working?**  
👉 Ensure **2-Step Verification** is enabled.  
👉 Use the **correct generated App Password**.  

🚫 **Email Not Sending?**  
👉 Check SMTP settings.  
👉 Make sure **Less Secure Apps** is enabled (for some providers).  

🚫 **Certificate Not Generating?**  
👉 Ensure `certificate_template.png` **exists** in `/static/`.  
👉 Check **font file path** (`arial.ttf`).  

---

