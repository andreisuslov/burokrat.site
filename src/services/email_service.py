"""
Email service using SMTP (self-hosted solution).
Handles sending contact form submissions via email.
"""

import os
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr


class EmailService:
    """Service for sending emails via SMTP."""
    
    def __init__(self):
        """Initialize SMTP client with configuration from environment."""
        self.smtp_host = os.environ.get('SMTP_HOST', 'smtp.gmail.com')
        self.smtp_port = int(os.environ.get('SMTP_PORT', '587'))
        self.smtp_username = os.environ.get('SMTP_USERNAME')
        self.smtp_password = os.environ.get('SMTP_PASSWORD')
        self.from_email = os.environ.get('SMTP_FROM_EMAIL', self.smtp_username)
        self.from_name = os.environ.get('SMTP_FROM_NAME', 'Бюрократ - Форма обратной связи')
        self.to_email = os.environ.get('SMTP_TO_EMAIL')
        self.use_tls = os.environ.get('SMTP_USE_TLS', 'true').lower() == 'true'
        
        if not self.smtp_username:
            logging.warning("⚠️  SMTP_USERNAME not found in environment variables")
        if not self.smtp_password:
            logging.warning("⚠️  SMTP_PASSWORD not found in environment variables")
        if not self.to_email:
            logging.warning("⚠️  SMTP_TO_EMAIL not found in environment variables")
    
    def send_contact_form_email(self, form_data: dict) -> tuple[bool, str]:
        """
        Send contact form submission via email.
        
        Args:
            form_data: Dictionary containing form fields:
                - name: Sender's name
                - email: Sender's email
                - phone: Sender's phone (optional)
                - subject: Email subject
                - message: Email message
                - company: Company name (optional)
        
        Returns:
            Tuple of (success: bool, message: str)
        """
        if not self.smtp_username or not self.smtp_password or not self.to_email:
            error_msg = "Email service not configured. Please set SMTP_USERNAME, SMTP_PASSWORD, and SMTP_TO_EMAIL environment variables."
            logging.error(f"❌ {error_msg}")
            return False, error_msg
        
        try:
            # Extract form data
            name = form_data.get('name', 'Unknown')
            sender_email = form_data.get('email', 'unknown@example.com')
            phone = form_data.get('phone', 'Не указан')
            subject = form_data.get('subject', 'Без темы')
            message_text = form_data.get('message', '')
            company = form_data.get('company', 'Не указана')
            
            # Add [FORM] prefix to subject
            email_subject = f"[FORM] {subject}"
            
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = email_subject
            msg['From'] = formataddr((self.from_name, self.from_email))
            msg['To'] = self.to_email
            msg['Reply-To'] = formataddr((name, sender_email))
            
            # Plain text version
            text_content = f"""
Новое сообщение с формы обратной связи

Имя: {name}
Email: {sender_email}
Телефон: {phone}
Компания: {company}
Тема: {subject}

Сообщение:
{message_text}

---
Это сообщение отправлено с сайта burokrat.site через форму обратной связи.
            """
            
            # HTML version
            html_content = f"""
            <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                    <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
                        <h2 style="color: #4F46E5; border-bottom: 2px solid #4F46E5; padding-bottom: 10px;">
                            Новое сообщение с формы обратной связи
                        </h2>
                        
                        <div style="margin: 20px 0;">
                            <p style="margin: 10px 0;"><strong>Имя:</strong> {name}</p>
                            <p style="margin: 10px 0;"><strong>Email:</strong> <a href="mailto:{sender_email}">{sender_email}</a></p>
                            <p style="margin: 10px 0;"><strong>Телефон:</strong> {phone}</p>
                            <p style="margin: 10px 0;"><strong>Компания:</strong> {company}</p>
                            <p style="margin: 10px 0;"><strong>Тема:</strong> {subject}</p>
                        </div>
                        
                        <div style="margin: 20px 0; padding: 15px; background-color: #f9fafb; border-left: 4px solid #4F46E5; border-radius: 4px;">
                            <h3 style="margin-top: 0; color: #4F46E5;">Сообщение:</h3>
                            <p style="white-space: pre-wrap;">{message_text}</p>
                        </div>
                        
                        <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; font-size: 12px; color: #666;">
                            <p>Это сообщение отправлено с сайта burokrat.site через форму обратной связи.</p>
                        </div>
                    </div>
                </body>
            </html>
            """
            
            # Attach both versions
            part1 = MIMEText(text_content, 'plain', 'utf-8')
            part2 = MIMEText(html_content, 'html', 'utf-8')
            msg.attach(part1)
            msg.attach(part2)
            
            # Connect to SMTP server and send email
            logging.info(f"📧 Connecting to SMTP server {self.smtp_host}:{self.smtp_port}")
            
            if self.use_tls:
                # Use STARTTLS (most common for port 587)
                server = smtplib.SMTP(self.smtp_host, self.smtp_port, timeout=10)
                server.ehlo()
                server.starttls()
                server.ehlo()
            else:
                # Use SSL (for port 465)
                server = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port, timeout=10)
            
            # Login and send
            server.login(self.smtp_username, self.smtp_password)
            server.send_message(msg)
            server.quit()
            
            logging.info(f"✅ Email sent successfully to {self.to_email}")
            return True, "Email sent successfully"
                
        except smtplib.SMTPAuthenticationError as e:
            error_msg = f"SMTP authentication failed. Check your username and password: {str(e)}"
            logging.error(f"❌ {error_msg}")
            return False, error_msg
        except smtplib.SMTPException as e:
            error_msg = f"SMTP error occurred: {str(e)}"
            logging.error(f"❌ {error_msg}")
            return False, error_msg
        except Exception as e:
            error_msg = f"Failed to send email: {str(e)}"
            logging.error(f"❌ {error_msg}")
            return False, error_msg


# Singleton instance
_email_service = None

def get_email_service() -> EmailService:
    """Get or create the email service singleton."""
    global _email_service
    if _email_service is None:
        _email_service = EmailService()
    return _email_service
