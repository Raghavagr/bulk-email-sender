# 📧 Bulk Email Sender - Simple & Secure

A powerful yet simple Python script to send personalized emails to multiple recipients using Gmail. Perfect for newsletters, announcements, invitations, or any bulk email needs without paying for expensive email marketing tools.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Gmail](https://img.shields.io/badge/Gmail-SMTP-red)](https://mail.google.com)

## 🌟 Features

- ✅ **Simple & Easy to Use** - Console-based interface with step-by-step prompts
- ✅ **Secure Authentication** - Uses Gmail App Passwords (no plain text password storage)
- ✅ **CSV Support** - Load email lists from CSV files easily
- ✅ **Attachment Support** - Send PDF, DOCX, images, and more (up to 5 files, 25MB total)
- ✅ **Rate Limiting** - Built-in delays to avoid spam detection
- ✅ **Progress Tracking** - Real-time updates on email sending progress
- ✅ **Error Handling** - Detailed error messages and failed email tracking
- ✅ **Multi-line Messages** - Support for formatted email bodies
- ✅ **Sender Personalization** - Add custom sender name
- ✅ **Smart Validation** - Validates files, checks sizes, prevents errors
- ✅ **No Dependencies** - Uses only Python standard library

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Gmail Setup](#gmail-setup)
- [Usage](#usage)
- [CSV File Format](#csv-file-format)
- [Example Usage](#example-usage)
- [Common Issues](#common-issues)
- [Best Practices](#best-practices)
- [Gmail Sending Limits](#gmail-sending-limits)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Prerequisites

Before you begin, ensure you have the following:

- **Python 3.8 or higher** installed on your system
- A **Gmail account** with 2-Step Verification enabled
- A **Gmail App Password** (instructions below)
- Basic knowledge of using Command Prompt/Terminal

### Check Python Installation

Open Command Prompt (Windows) or Terminal (Mac/Linux) and run:

```bash
python --version
```

You should see something like `Python 3.13.9` or higher.

**Don't have Python?** Download it from [python.org](https://www.python.org/downloads/)

## 📥 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/bulk-email-sender.git
cd bulk-email-sender
```

Or download the ZIP file and extract it.

### Step 2: Verify Files

Ensure you have these files:
- `email_sender.py` - Main script
- `README.md` - This file
- `LICENSE` - License information

### Step 3: No Additional Dependencies!

This script uses only Python's standard library, so no pip installations needed! 🎉

## 🔐 Gmail Setup

To use Gmail with this script, you need to create an **App Password**. This is different from your regular Gmail password and is more secure.

### Step 1: Enable 2-Step Verification

1. Go to your [Google Account Security Page](https://myaccount.google.com/security)
2. Find **"2-Step Verification"** and click on it
3. Follow the prompts to enable it (you'll need your phone)

### Step 2: Create App Password

1. **Go directly to:** [App Passwords Page](https://myaccount.google.com/apppasswords)
2. You might need to sign in again (security verification)
3. You'll see a page titled **"App passwords"**
4. If you see "Select app" dropdown:
   - Select **"Mail"**
   - Select **"Other (Custom name)"**
   - Type a name: **"Bulk Email Sender"**
   - Click **"Generate"**
5. Google will display a 16-character password like: `abcd efgh ijkl mnop`
6. **IMPORTANT:** Copy this password immediately and save it securely
7. You won't be able to see it again (but you can create new ones anytime)

### Troubleshooting App Passwords

**Can't find "App passwords" option?**

- Make sure 2-Step Verification is fully enabled and working
- Try the direct link: https://myaccount.google.com/apppasswords
- If using a work/school account, contact your admin (they might have disabled it)
- If enrolled in Advanced Protection Program, you'll need to use standard 2FA instead

## 🚀 Usage

### Step 1: Prepare Your Email List

Create a CSV file (e.g., `emails.csv`) with your recipients:

```csv
email
john.doe@example.com
jane.smith@company.com
contact@business.org
```

Place this CSV file in the same folder as `email_sender.py`

### Step 2: Run the Script

**Windows:**
```bash
python email_sender.py
```

**Mac/Linux:**
```bash
python3 email_sender.py
```

### Step 3: Follow the Prompts

The script will guide you through:

1. **Gmail Login**
   - Enter your Gmail address
   - Enter your App Password (typing will be hidden for security)

2. **Load Email List**
   - Provide the path to your CSV file
   - Review the email list preview

3. **Compose Email**
   - Enter your name (optional)
   - Enter email subject
   - Type your message (type `END` on a new line when finished)

4. **Add Attachments (Optional)**
   - Add up to 5 files (25MB total limit)
   - Enter file paths separated by commas
   - Or press Enter to skip attachments

5. **Configure Sending**
   - Set delay between emails (default: 2 seconds)
   - Review and confirm

6. **Send Emails**
   - Watch real-time progress
   - View summary report at the end

## 📄 CSV File Format

Your CSV file must have a column named `email` (case-insensitive).

### Basic Format

```csv
email
recipient1@example.com
recipient2@example.com
recipient3@example.com
```

### Tips for CSV Files

- ✅ **Use Excel or Google Sheets** to create/edit your CSV
- ✅ **First row must be:** `email` (this is the header)
- ✅ **One email per row**
- ✅ **No empty rows** between emails
- ✅ **Remove duplicates** before sending
- ✅ **Validate emails** to avoid bounces

### Exporting from Excel

1. Open your Excel file
2. Make sure column A1 has: `email`
3. Add email addresses in cells below
4. File → Save As
5. Choose: **CSV (Comma delimited) (*.csv)**
6. Save in the same folder as the script

## 📖 Example Usage

Here's a complete example walkthrough:

### Scenario: Sending Job Application with Resume

**1. Prepare your resume:**
Place `John_Doe_Resume.pdf` in the same folder as the script.

**2. Create `hr_contacts.csv`:**
```csv
email
hr@techcorp.com
recruiter@startup.io
hiring@company.com
```

**3. Run the script:**
```bash
python email_sender.py
```

**4. Enter credentials:**
```
Enter your Gmail address: john.doe@gmail.com
Enter App Password: [your-16-char-password]
```

**5. Load CSV:**
```
Enter CSV file path: hr_contacts.csv
```

**6. Compose email:**
```
Enter your name: John Doe
Enter email subject: Application for Software Developer Position

Enter email body:
Dear Hiring Manager,

I am writing to express my interest in the Software Developer position 
at your company. I have 3 years of experience in Python development and 
would love to contribute to your team.

Please find my resume attached for your review.

I look forward to hearing from you.

Best regards,
John Doe
Phone: (555) 123-4567
END
```

**7. Add attachments:**
```
Enter attachment file path(s): John_Doe_Resume.pdf

📎 Validating attachments...
   ✅ John_Doe_Resume.pdf (245.67KB)

✅ All attachments valid! Total size: 0.24MB
```

**8. Review and send:**
```
📊 READY TO SEND:
   👤 From: John Doe
   📧 To: 3 recipients
   📝 Subject: Application for Software Developer Position
   📎 Attachments: 1 file(s)
      - John_Doe_Resume.pdf
   ⏱️  Delay: 2 seconds between emails

🚀 Start sending? yes
```

**9. Results:**
```
📎 Attachments to include: 1 file(s)
   - John_Doe_Resume.pdf

✅ [1/3] Sent to: hr@techcorp.com (with 1 attachment(s))
✅ [2/3] Sent to: recruiter@startup.io (with 1 attachment(s))
✅ [3/3] Sent to: hiring@company.com (with 1 attachment(s))

📊 SUMMARY
✅ Successfully sent: 3/3
❌ Failed: 0/3
📎 Attachments included: 1 file(s)
```

### More Attachment Examples

**Multiple attachments:**
```
Enter attachment file path(s): resume.pdf, cover_letter.docx, portfolio.pdf
```

**Full file paths:**
```
Enter attachment file path(s): C:\Users\John\Documents\resume.pdf, C:\Users\John\Desktop\certificate.pdf
```

**Mixed (filename and full path):**
```
Enter attachment file path(s): resume.pdf, C:\Documents\cover_letter.docx
```

**No attachments (press Enter):**
```
Enter attachment file path(s): 
📧 No attachments - sending text-only email
```

## 🐛 Common Issues

### Issue 1: "Authentication Failed"

**Symptoms:**
```
❌ Authentication failed! Check your email and app password.
```

**Solutions:**
- ✅ Make sure you're using **App Password**, not your regular Gmail password
- ✅ Check for typos in your Gmail address
- ✅ Verify the App Password is correct (16 characters)
- ✅ Create a new App Password and try again
- ✅ Ensure 2-Step Verification is enabled

### Issue 2: "File not found"

**Symptoms:**
```
❌ File not found: emails.csv
```

**Solutions:**
- ✅ Verify the CSV file is in the same folder as the script
- ✅ Check the filename (including file extension)
- ✅ Try providing the full path: `C:\Users\YourName\Desktop\emails.csv`
- ✅ Check for typos in the filename

### Issue 3: "No 'email' column found"

**Symptoms:**
```
❌ No 'email' column found in CSV file!
```

**Solutions:**
- ✅ Make sure the first row of your CSV is: `email`
- ✅ Don't add extra spaces or special characters
- ✅ Use lowercase: `email` not `Email` or `EMAIL`
- ✅ Re-save your CSV file

### Issue 4: Emails Going to Spam

**Symptoms:**
- Recipients not seeing your emails
- Emails landing in spam folder

**Solutions:**
- ✅ Use a professional subject line (avoid "FREE", "ACT NOW", etc.)
- ✅ Add a personal touch to your message
- ✅ Recipients should expect emails from you
- ✅ Ask recipients to add your email to contacts
- ✅ Don't send too many emails too quickly
- ✅ Include an unsubscribe option for marketing emails

### Issue 5: "'git' is not recognized"

**Symptoms:**
```
'git' is not recognized as an internal or external command
```

**Solutions:**
- ✅ Install Git from [git-scm.com](https://git-scm.com/)
- ✅ During installation, select "Git from the command line"
- ✅ Restart Command Prompt after installation
- ✅ Verify installation: `git --version`

### Issue 6: Attachment Too Large

**Symptoms:**
```
❌ File too large: resume.pdf (30.50MB)
💡 Gmail limit: 25MB per file
```

**Solutions:**
- ✅ Compress your PDF (use online PDF compressor)
- ✅ Reduce image quality in documents
- ✅ Split into multiple smaller files
- ✅ Use Google Drive link instead for very large files

### Issue 7: Attachment File Not Found

**Symptoms:**
```
❌ File not found: resume.pdf
```

**Solutions:**
- ✅ Check filename spelling and extension
- ✅ Use full path: `C:\Users\YourName\Documents\resume.pdf`
- ✅ Place file in same folder as script
- ✅ Remove quotes if you copied path

## ⚡ Best Practices

### Email Content

- ✅ **Keep it professional** - Proper grammar and spelling
- ✅ **Personalize** - Add recipient-specific details when possible
- ✅ **Be clear** - State your purpose early
- ✅ **Include contact info** - Make it easy to reply
- ✅ **Proofread** - Test with your own email first
- ✅ **Optimize attachments** - Compress large files, use clear filenames

### Sending Strategy

- ✅ **Test first** - Always send to yourself before bulk sending
- ✅ **Start small** - Send to 5-10 people first, verify delivery
- ✅ **Use delays** - 2-3 seconds between emails (script handles this)
- ✅ **Check sent folder** - Verify emails are being sent
- ✅ **Monitor bounces** - Remove invalid addresses from your list

### Security

- ✅ **Never share App Password** - Treat it like your regular password
- ✅ **Don't upload CSV to GitHub** - `.gitignore` already prevents this
- ✅ **Don't upload personal documents** - `.gitignore` blocks common file types
- ✅ **Revoke unused App Passwords** - Clean up periodically
- ✅ **Keep your list private** - Don't share recipient emails
- ✅ **Scan attachments** - Make sure files are virus-free before sending

### Legal Compliance

- ✅ **Get permission** - Only email people who expect it
- ✅ **Provide unsubscribe** - Required for marketing emails
- ✅ **Follow CAN-SPAM Act** - Include physical address for commercial emails
- ✅ **Respect GDPR** - Get consent for EU recipients
- ✅ **Honor opt-outs** - Remove unsubscribers immediately

## 📊 Gmail Sending Limits

Be aware of Gmail's sending limits to avoid account suspension:

| Account Type | Daily Limit | Recommendation |
|-------------|-------------|----------------|
| **Free Gmail** | 500 emails/day | Send max 100-150 per batch |
| **Google Workspace** | 2,000 emails/day | Send max 500 per batch |

### Tips to Stay Within Limits

- ✅ **Split large lists** - Break 1,000 emails into 2-3 days
- ✅ **Use delays** - Script automatically adds 2-3 second delays
- ✅ **Monitor your account** - Watch for warning signs
- ✅ **Warm up new accounts** - Start with small batches

### Warning Signs

If Gmail suspects spam:
- ⚠️ Temporary sending restrictions (24-48 hours)
- ⚠️ Warning emails from Google
- ⚠️ Emails automatically going to spam

**If this happens:**
- Stop sending immediately
- Wait 24-48 hours
- Resume with smaller batches
- Improve email content quality

## 🎯 Future Enhancements

Want to contribute? Here are some ideas:

- [ ] HTML email templates
- [x] ~~Attachment support~~ ✅ **COMPLETED!**
- [ ] Personalization with names from CSV
- [ ] Email scheduling
- [ ] Outlook/Yahoo support
- [ ] GUI interface
- [ ] Email tracking (open rates)
- [ ] Retry failed emails automatically
- [ ] Progress save/resume
- [ ] Multiple recipient columns (CC, BCC)
- [ ] Batch attachment compression
- [ ] Cloud storage integration (Google Drive links)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Guidelines

- Write clean, readable code
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation if needed
- Follow existing code style

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### What this means:

- ✅ Use for personal projects
- ✅ Use for commercial projects
- ✅ Modify the code
- ✅ Distribute the code
- ❌ No warranty provided
- ❌ Author not liable for issues

## ⚠️ Disclaimer

**Important Legal Notice:**

- This tool is for **legitimate bulk emailing only**
- **Never use for spam or unsolicited emails**
- You are responsible for complying with:
  - CAN-SPAM Act (USA)
  - GDPR (Europe)
  - Local email regulations
- Get explicit permission before sending marketing emails
- Include unsubscribe options in commercial emails
- Respect recipient privacy and preferences

**Author is not responsible for misuse of this tool.**

## 🙏 Acknowledgments

- Thanks to the Python community for excellent documentation
- Inspired by the need for affordable email automation
- Built with standard library only for maximum compatibility

## 📞 Support

Having issues or questions?

1. **Check the [Common Issues](#common-issues) section**
2. **Read the [Best Practices](#best-practices)**
3. **Open an issue** on GitHub with:
   - Detailed description of your problem
   - Error messages (if any)
   - Your Python version (`python --version`)
   - Your operating system

## 🌟 Star This Repository

If this tool helped you, please give it a ⭐ on GitHub!

It helps others discover the project and motivates continued development.

---

**Made with ❤️ by developers, for developers**

**Happy Emailing! 📧**