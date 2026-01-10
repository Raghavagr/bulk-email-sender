"""
Bulk Email Sender - Simple & Secure
Created for: Sending personalized emails to multiple recipients
Author: Your AI Mentor
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
    
    def create_email_message(self, recipient, subject, body, sender_name=None):
        """
        Create email message with proper formatting
        
        Args:
            recipient: Recipient email address
            subject: Email subject
            body: Email body (can include HTML)
            sender_name: Optional sender name
            
        Returns:
            MIMEMultipart message object
        """
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = f"{sender_name} <{self.sender_email}>" if sender_name else self.sender_email
        message["To"] = recipient
        
        # Create both plain text and HTML versions
        text_part = MIMEText(body, "plain")
        html_part = MIMEText(body, "html")
        
        message.attach(text_part)
        message.attach(html_part)
        
        return message
    
    def send_bulk_emails(self, emails, subject, body, sender_name=None, delay=2):
        """
        Send emails to multiple recipients
        
        Args:
            emails: List of recipient email addresses
            subject: Email subject
            body: Email body
            sender_name: Optional sender name
            delay: Delay between emails (seconds) to avoid spam detection
        """
        if not self.server:
            print("❌ Not connected to server. Please connect first.")
            return
        
        total_emails = len(emails)
        sent_count = 0
        failed_count = 0
        failed_emails = []
        
        print(f"📨 Starting to send {total_emails} emails...\n")
        print("=" * 60)
        
        for index, recipient in enumerate(emails, 1):
            try:
                # Create message
                message = self.create_email_message(recipient, subject, body, sender_name)
                
                # Send email
                self.server.send_message(message)
                sent_count += 1
                
                print(f"✅ [{index}/{total_emails}] Sent to: {recipient}")
                
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
    ║               Your Personal Email Automation Tool         ║
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
    
    # Step 4: Send emails
    print("\n📝 STEP 4: SENDING EMAILS")
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
    print(f"   ⏱️  Delay: {delay} seconds between emails")
    
    final_confirm = input("\n🚀 Start sending? (yes/no): ").strip().lower()
    if final_confirm not in ['yes', 'y']:
        print("\n❌ Operation cancelled.")
        sender.disconnect()
        return
    
    # Send emails
    sender.send_bulk_emails(emails, subject, body, sender_name, delay)
    
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