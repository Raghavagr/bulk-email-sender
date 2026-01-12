"""
Bulk Email Sender - Simple & Secure (WITH ATTACHMENT SUPPORT)
Created for: Sending personalized emails to multiple recipients
Author: Your AI Mentor
Version: 2.0 - Now with attachment support!
"""

import smtplib
import csv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
from datetime import datetime

class EmailSender:
    """Main class to handle email sending operations"""
    
    def __init__(self):
        self.server = None
        self.sender_email = None
        self.sender_name = None
        
    def connect_to_gmail(self, email, app_password):
        """
        Connect to Gmail SMTP server
        
        Args:
            email: Your Gmail address
            app_password: 16-character app password from Google
            
        Returns:
            True if connection successful, False otherwise
        """
        try:
            print("\n🔄 Connecting to Gmail server...")
            
            # Gmail SMTP server details
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            
            # Create SMTP session
            self.server = smtplib.SMTP(smtp_server, smtp_port)
            self.server.starttls()  # Secure the connection
            
            # Login to Gmail
            self.server.login(email, app_password)
            self.sender_email = email
            
            print("✅ Successfully connected to Gmail!")
            print(f"📧 Logged in as: {email}\n")
            return True
            
        except smtplib.SMTPAuthenticationError:
            print("❌ Authentication failed! Check your email and app password.")
            print("💡 Tip: Make sure you're using an App Password, not your regular password.")
            return False
        except Exception as e:
            print(f"❌ Connection error: {str(e)}")
            return False
    
    def read_emails_from_csv(self, csv_path):
        """
        Read email addresses from CSV file
        
        Args:
            csv_path: Path to CSV file
            
        Returns:
            List of email addresses
        """
        emails = []
        
        try:
            if not os.path.exists(csv_path):
                print(f"❌ File not found: {csv_path}")
                return None
            
            with open(csv_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                
                # Check if 'email' or 'emails' column exists
                fieldnames = csv_reader.fieldnames
                email_column = None
                
                for field in fieldnames:
                    if field.lower() in ['email', 'emails', 'e-mail', 'e-mails']:
                        email_column = field
                        break
                
                if not email_column:
                    print("❌ No 'email' column found in CSV file!")
                    print(f"Found columns: {', '.join(fieldnames)}")
                    return None
                
                # Read all emails
                for row in csv_reader:
                    email = row.get(email_column, '').strip()
                    if email and '@' in email:  # Basic email validation
                        emails.append(email)
                
            print(f"✅ Found {len(emails)} valid email addresses in CSV\n")
            return emails
            
        except Exception as e:
            print(f"❌ Error reading CSV: {str(e)}")
            return None
    
    def validate_attachments(self, attachment_paths):
        """
        Validate and prepare attachment files
        
        Args:
            attachment_paths: List of file paths
            
        Returns:
            List of valid attachment paths, or None if any file is invalid
        """
        if not attachment_paths:
            return []
        
        valid_attachments = []
        total_size = 0
        max_size = 25 * 1024 * 1024  # 25MB total limit for Gmail
        
        print("\n📎 Validating attachments...")
        
        for path in attachment_paths:
            path = path.strip().strip('"').strip("'")  # Remove quotes and whitespace
            
            # Check if file exists
            if not os.path.exists(path):
                print(f"❌ File not found: {path}")
                return None
            
            # Check if it's a file (not a directory)
            if not os.path.isfile(path):
                print(f"❌ Not a file: {path}")
                return None
            
            # Get file size
            file_size = os.path.getsize(path)
            total_size += file_size
            
            # Check individual file size (max 25MB per file)
            if file_size > max_size:
                size_mb = file_size / (1024 * 1024)
                print(f"❌ File too large: {path} ({size_mb:.2f}MB)")
                print("💡 Gmail limit: 25MB per file")
                return None
            
            valid_attachments.append(path)
            file_name = os.path.basename(path)
            size_kb = file_size / 1024
            print(f"   ✅ {file_name} ({size_kb:.2f}KB)")
        
        # Check total size
        if total_size > max_size:
            total_mb = total_size / (1024 * 1024)
            print(f"\n❌ Total attachments too large: {total_mb:.2f}MB")
            print("💡 Gmail limit: 25MB total")
            return None
        
        total_mb = total_size / (1024 * 1024)
        print(f"\n✅ All attachments valid! Total size: {total_mb:.2f}MB")
        
        return valid_attachments
    
    def create_email_message(self, recipient, subject, body, sender_name=None, attachments=None):
        """
        Create email message with proper formatting and attachments
        
        Args:
            recipient: Recipient email address
            subject: Email subject
            body: Email body (can include HTML)
            sender_name: Optional sender name
            attachments: List of file paths to attach
            
        Returns:
            MIMEMultipart message object
        """
        message = MIMEMultipart()
        message["Subject"] = subject
        message["From"] = f"{sender_name} <{self.sender_email}>" if sender_name else self.sender_email
        message["To"] = recipient
        
        # Add email body
        body_part = MIMEText(body, "plain")
        message.attach(body_part)
        
        # Add attachments if provided
        if attachments:
            for file_path in attachments:
                try:
                    # Get filename
                    filename = os.path.basename(file_path)
                    
                    # Open file in binary mode
                    with open(file_path, 'rb') as attachment_file:
                        # Create MIMEBase object
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment_file.read())
                    
                    # Encode file in ASCII characters
                    encoders.encode_base64(part)
                    
                    # Add header with filename
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename= {filename}'
                    )
                    
                    # Attach the file to message
                    message.attach(part)
                    
                except Exception as e:
                    print(f"⚠️  Warning: Could not attach {filename}: {str(e)}")
        
        return message
    
    def send_bulk_emails(self, emails, subject, body, sender_name=None, attachments=None, delay=2):
        """
        Send emails to multiple recipients
        
        Args:
            emails: List of recipient email addresses
            subject: Email subject
            body: Email body
            sender_name: Optional sender name
            attachments: List of file paths to attach
            delay: Delay between emails (seconds) to avoid spam detection
        """
        if not self.server:
            print("❌ Not connected to server. Please connect first.")
            return
        
        total_emails = len(emails)
        sent_count = 0
        failed_count = 0
        failed_emails = []
        
        # Show attachment info
        if attachments:
            print(f"\n📎 Attachments to include: {len(attachments)} file(s)")
            for att in attachments:
                print(f"   - {os.path.basename(att)}")
        
        print(f"\n📨 Starting to send {total_emails} emails...\n")
        print("=" * 60)
        
        for index, recipient in enumerate(emails, 1):
            try:
                # Create message
                message = self.create_email_message(
                    recipient, 
                    subject, 
                    body, 
                    sender_name,
                    attachments
                )
                
                # Send email
                self.server.send_message(message)
                sent_count += 1
                
                attachment_info = f" (with {len(attachments)} attachment(s))" if attachments else ""
                print(f"✅ [{index}/{total_emails}] Sent to: {recipient}{attachment_info}")
                
                # Add delay to avoid spam detection
                if index < total_emails:  # Don't delay after last email
                    time.sleep(delay)
                
            except Exception as e:
                failed_count += 1
                failed_emails.append(recipient)
                print(f"❌ [{index}/{total_emails}] Failed to send to {recipient}: {str(e)}")
        
        # Summary
        print("\n" + "=" * 60)
        print(f"\n📊 SUMMARY")
        print(f"✅ Successfully sent: {sent_count}/{total_emails}")
        print(f"❌ Failed: {failed_count}/{total_emails}")
        
        if attachments:
            print(f"📎 Attachments included: {len(attachments)} file(s)")
        
        if failed_emails:
            print(f"\n⚠️  Failed email addresses:")
            for email in failed_emails:
                print(f"   - {email}")
    
    def disconnect(self):
        """Close the SMTP connection"""
        if self.server:
            self.server.quit()
            print("\n✅ Disconnected from server")


def print_banner():
    """Print welcome banner"""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║           📧 BULK EMAIL SENDER - SIMPLE & SECURE 📧       ║
    ║                                                           ║
    ║          Your Personal Email Automation Tool v2.0         ║
    ║                  📎 Now with Attachments! 📎              ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """
    print(banner)


def get_multiline_input(prompt):
    """
    Get multi-line input for email body
    User types their message and enters 'END' on a new line to finish
    """
    print(prompt)
    print("💡 Type your message (press Enter for new lines)")
    print("💡 Type 'END' on a new line when finished\n")
    
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    
    return '\n'.join(lines)


def get_attachments():
    """
    Get attachment file paths from user
    Returns list of valid file paths or None
    """
    print("\n📎 ATTACHMENTS (Optional)")
    print("-" * 60)
    print("💡 You can attach up to 5 files (Max 25MB total)")
    print("💡 Supported: PDF, DOCX, XLSX, images, etc.")
    print("💡 Enter file paths separated by commas")
    print("💡 If file is in same folder as script, just enter filename")
    print("💡 Press Enter to skip attachments\n")
    
    print("Examples:")
    print("  - Single file: resume.pdf")
    print("  - Multiple files: resume.pdf, cover_letter.docx")
    print("  - Full path: C:\\Users\\YourName\\Documents\\resume.pdf")
    print("  - Mixed: resume.pdf, C:\\Documents\\portfolio.pdf\n")
    
    attachment_input = input("Enter attachment file path(s): ").strip()
    
    # If user presses Enter (no input), return empty list
    if not attachment_input:
        print("📧 No attachments - sending text-only email")
        return []
    
    # Split by comma and clean up
    file_paths = [path.strip() for path in attachment_input.split(',')]
    
    # Limit to 5 files
    if len(file_paths) > 5:
        print(f"\n⚠️  Warning: You entered {len(file_paths)} files. Maximum is 5.")
        print("Using first 5 files only.")
        file_paths = file_paths[:5]
    
    return file_paths


def main():
    """Main function to run the email sender"""
    
    # Print welcome banner
    print_banner()
    
    # Create email sender instance
    sender = EmailSender()
    
    # Step 1: Connect to Gmail
    print("\n📝 STEP 1: CONNECT TO GMAIL")
    print("-" * 60)
    email = input("Enter your Gmail address: ").strip()
    print("\n💡 Enter your App Password (16 characters from Google)")
    print("💡 Tip: Your typing will be hidden for security")
    
    # For security, you might want to use getpass, but for simplicity using input
    import getpass
    app_password = getpass.getpass("Enter App Password: ").strip()
    
    # Connect to Gmail
    if not sender.connect_to_gmail(email, app_password):
        print("\n⚠️  Connection failed. Please try again.")
        return
    
    # Step 2: Load email list from CSV
    print("\n📝 STEP 2: LOAD EMAIL LIST")
    print("-" * 60)
    print("💡 Place your CSV file in the same folder as this script")
    print("💡 CSV should have a column named 'email' or 'emails'")
    
    csv_path = input("\nEnter CSV file path (or just filename if in same folder): ").strip()
    
    # Remove quotes if user copied path with quotes
    csv_path = csv_path.strip('"').strip("'")
    
    # Read emails from CSV
    emails = sender.read_emails_from_csv(csv_path)
    
    if not emails or len(emails) == 0:
        print("\n⚠️  No valid emails found. Please check your CSV file.")
        sender.disconnect()
        return
    
    # Show preview of emails
    print("📋 Preview of email list:")
    for i, email in enumerate(emails[:5], 1):
        print(f"   {i}. {email}")
    if len(emails) > 5:
        print(f"   ... and {len(emails) - 5} more")
    
    # Confirm before proceeding
    proceed = input(f"\n✅ Proceed to send emails to {len(emails)} recipients? (yes/no): ").strip().lower()
    if proceed not in ['yes', 'y']:
        print("\n❌ Operation cancelled.")
        sender.disconnect()
        return
    
    # Step 3: Compose email
    print("\n📝 STEP 3: COMPOSE YOUR EMAIL")
    print("-" * 60)
    
    sender_name = input("Enter your name (optional, press Enter to skip): ").strip()
    subject = input("Enter email subject: ").strip()
    
    print()
    body = get_multiline_input("✍️  Enter email body:")
    
    # Step 4: Add attachments
    print("\n📝 STEP 4: ADD ATTACHMENTS (OPTIONAL)")
    print("-" * 60)
    
    attachment_paths = get_attachments()
    
    # Validate attachments if provided
    validated_attachments = None
    if attachment_paths:
        validated_attachments = sender.validate_attachments(attachment_paths)
        if validated_attachments is None:
            print("\n❌ Attachment validation failed. Please check your files.")
            retry = input("Continue without attachments? (yes/no): ").strip().lower()
            if retry not in ['yes', 'y']:
                print("\n❌ Operation cancelled.")
                sender.disconnect()
                return
            validated_attachments = []
    else:
        validated_attachments = []
    
    # Step 5: Send emails
    print("\n📝 STEP 5: SENDING EMAILS")
    print("-" * 60)
    
    # Ask for delay between emails
    print("\n💡 Recommended delay: 2-3 seconds between emails")
    delay_input = input("Enter delay in seconds (press Enter for 2): ").strip()
    delay = int(delay_input) if delay_input.isdigit() else 2
    
    # Final confirmation
    print(f"\n📊 READY TO SEND:")
    print(f"   👤 From: {sender_name or email}")
    print(f"   📧 To: {len(emails)} recipients")
    print(f"   📝 Subject: {subject}")
    if validated_attachments:
        print(f"   📎 Attachments: {len(validated_attachments)} file(s)")
        for att in validated_attachments:
            print(f"      - {os.path.basename(att)}")
    else:
        print(f"   📎 Attachments: None")
    print(f"   ⏱️  Delay: {delay} seconds between emails")
    
    final_confirm = input("\n🚀 Start sending? (yes/no): ").strip().lower()
    if final_confirm not in ['yes', 'y']:
        print("\n❌ Operation cancelled.")
        sender.disconnect()
        return
    
    # Send emails
    sender.send_bulk_emails(emails, subject, body, sender_name, validated_attachments, delay)
    
    # Disconnect
    sender.disconnect()
    
    print("\n🎉 Process completed!")
    print(f"📅 Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n💡 Tip: Check your Gmail 'Sent' folder to verify emails were sent")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Process interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
    finally:
        print("\n👋 Thank you for using Bulk Email Sender!")
        input("\nPress Enter to exit...")