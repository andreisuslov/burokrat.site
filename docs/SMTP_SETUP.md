# SMTP Email Setup Guide (Self-Hosted Solution)

This guide explains how to configure SMTP for your contact form email functionality using your own email account. No external services required!

## Overview

The contact form sends emails via SMTP with the following features:
- **Subject prefix**: All emails have `[FORM]` prefix in the subject line
- **Professional formatting**: HTML and plain text email templates
- **Reply-to support**: Recipients can reply directly to the form sender
- **Error handling**: Graceful fallback with user-friendly error messages
- **No external dependencies**: Uses Python's built-in `smtplib`
- **Works with any email provider**: Gmail, Outlook, Yahoo, Mail.ru, Yandex, etc.

## Quick Start

### 1. Choose Your Email Provider

The system works with any SMTP-compatible email provider. Here are the most common:

| Provider | SMTP Host | Port | TLS |
|----------|-----------|------|-----|
| **Gmail** | smtp.gmail.com | 587 | Yes |
| **Outlook/Hotmail** | smtp-mail.outlook.com | 587 | Yes |
| **Yahoo** | smtp.mail.yahoo.com | 587 | Yes |
| **Mail.ru** | smtp.mail.ru | 465 | No (SSL) |
| **Yandex** | smtp.yandex.ru | 465 | No (SSL) |

### 2. Get App Password (Important!)

Most email providers require an "App Password" instead of your regular password for security.

#### Gmail (Recommended)
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable **2-Step Verification** (required)
3. Go to **App passwords** (search for it)
4. Select **Mail** and **Other (Custom name)**
5. Name it: `burokrat-site`
6. Copy the 16-character password (no spaces)

#### Outlook/Hotmail
1. Go to [Microsoft Account Security](https://account.microsoft.com/security)
2. Enable **Two-step verification**
3. Go to **App passwords**
4. Create new app password
5. Copy the password

#### Yandex
1. Go to [Yandex Mail Settings](https://mail.yandex.ru/)
2. Click **Security** → **App passwords**
3. Create new password for "Mail client"
4. Copy the password

#### Mail.ru
1. Go to [Mail.ru Settings](https://e.mail.ru/settings/security)
2. Enable **Two-factor authentication**
3. Create app password
4. Copy the password

### 3. Set Environment Variables

#### For Local Development

Create a `.env` file in the project root:

```bash
# Copy from .env.example
cp .env.example .env
```

Edit `.env` with your settings:

```bash
# SMTP Server Settings
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USE_TLS=true

# SMTP Authentication
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-16-char-app-password

# Email Addresses
SMTP_FROM_EMAIL=your-email@gmail.com
SMTP_FROM_NAME=Бюрократ - Форма обратной связи
SMTP_TO_EMAIL=where-to-receive-forms@example.com
```

**Important**: 
- Use the **App Password**, not your regular password
- `SMTP_TO_EMAIL` is where you want to receive form submissions
- `SMTP_FROM_EMAIL` is your email account

#### For Netlify Production

1. Go to your Netlify site dashboard
2. Navigate to **Site settings** → **Environment variables**
3. Add these variables:
   - `SMTP_HOST`: Your SMTP server (e.g., `smtp.gmail.com`)
   - `SMTP_PORT`: Port number (e.g., `587`)
   - `SMTP_USE_TLS`: `true` for port 587, `false` for port 465
   - `SMTP_USERNAME`: Your email address
   - `SMTP_PASSWORD`: Your app password
   - `SMTP_FROM_EMAIL`: Your email address
   - `SMTP_FROM_NAME`: `Бюрократ - Форма обратной связи`
   - `SMTP_TO_EMAIL`: Where to receive submissions

4. Redeploy your site

### 4. Test the Setup

1. Start your development server:
   ```bash
   python app.py
   ```

2. Navigate to `/contact` page
3. Fill out and submit the form
4. Check the console logs for connection status
5. Check your inbox for the email with `[FORM]` prefix

## Email Format

Emails sent from the form will have:

**Subject**: `[FORM] {user's subject}`

**From**: Бюрократ - Форма обратной связи <your-email@gmail.com>

**Reply-To**: {user's email}

**To**: {SMTP_TO_EMAIL}

**Body** includes:
- Name
- Email (clickable)
- Phone
- Company
- Subject
- Message (formatted with proper spacing)

## Provider-Specific Guides

### Gmail Setup (Detailed)

1. **Enable 2-Step Verification**:
   - Go to https://myaccount.google.com/security
   - Click "2-Step Verification" → "Get Started"
   - Follow the setup wizard

2. **Create App Password**:
   - Go to https://myaccount.google.com/apppasswords
   - Select "Mail" and "Other (Custom name)"
   - Name: `burokrat-site`
   - Click "Generate"
   - Copy the 16-character password (format: `xxxx xxxx xxxx xxxx`)

3. **Configure .env**:
   ```bash
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USE_TLS=true
   SMTP_USERNAME=your-email@gmail.com
   SMTP_PASSWORD=abcdabcdabcdabcd  # No spaces
   SMTP_FROM_EMAIL=your-email@gmail.com
   SMTP_TO_EMAIL=your-email@gmail.com
   ```

### Yandex Setup

1. **Enable 2FA**:
   - Go to https://passport.yandex.ru/profile
   - Enable two-factor authentication

2. **Create App Password**:
   - Go to https://mail.yandex.ru/
   - Settings → Security → App passwords
   - Create password for "Mail client"

3. **Configure .env**:
   ```bash
   SMTP_HOST=smtp.yandex.ru
   SMTP_PORT=465
   SMTP_USE_TLS=false  # Yandex uses SSL, not TLS
   SMTP_USERNAME=your-email@yandex.ru
   SMTP_PASSWORD=your-app-password
   SMTP_FROM_EMAIL=your-email@yandex.ru
   SMTP_TO_EMAIL=your-email@yandex.ru
   ```

### Mail.ru Setup

1. **Enable 2FA**:
   - Go to https://e.mail.ru/settings/security
   - Enable two-factor authentication

2. **Create App Password**:
   - In Security settings, find "App passwords"
   - Create new password

3. **Configure .env**:
   ```bash
   SMTP_HOST=smtp.mail.ru
   SMTP_PORT=465
   SMTP_USE_TLS=false  # Mail.ru uses SSL
   SMTP_USERNAME=your-email@mail.ru
   SMTP_PASSWORD=your-app-password
   SMTP_FROM_EMAIL=your-email@mail.ru
   SMTP_TO_EMAIL=your-email@mail.ru
   ```

## Troubleshooting

### "Email service not configured" error
- Check that all required environment variables are set
- Restart your server after adding environment variables
- Verify `.env` file is in the project root

### "SMTP authentication failed" error
- **Use App Password**, not your regular password
- Ensure 2-Step Verification is enabled
- Check username is your full email address
- Remove any spaces from the app password

### "Connection refused" or "Timeout" error
- Check `SMTP_HOST` and `SMTP_PORT` are correct
- Verify firewall isn't blocking outbound SMTP connections
- Try alternative port (587 vs 465)
- Check `SMTP_USE_TLS` setting matches your port

### Emails not being received
- Check spam/junk folder
- Verify `SMTP_TO_EMAIL` is correct
- Check server logs for success message
- Test with the same email for both FROM and TO first

### "SMTPServerDisconnected" error
- Your email provider may be blocking automated emails
- Try using a different email provider
- Check if your account has sending limits

### Gmail "Less secure app access" error
- Gmail no longer supports "less secure apps"
- You **must** use an App Password with 2-Step Verification
- Regular password will not work

## Security Best Practices

1. **Never commit** `.env` file to Git (already in `.gitignore`)
2. **Use App Passwords**, never regular passwords
3. **Rotate passwords** periodically
4. **Limit access** to environment variables
5. **Use separate email** for sending vs receiving if possible
6. **Monitor logs** for suspicious activity

## Rate Limits

Different providers have different sending limits:

- **Gmail**: 500 emails/day (free), 2000/day (Google Workspace)
- **Outlook**: 300 emails/day (free)
- **Yahoo**: 500 emails/day
- **Mail.ru**: ~100 emails/day
- **Yandex**: ~500 emails/day

For high-volume needs, consider:
- Using a dedicated email account
- Implementing rate limiting in your application
- Using a professional email service

## Configuration Files

- **Email service**: `src/services/email_service.py`
- **Contact route**: `src/routes/contact.py`
- **Form messages**: `data/contact.yaml`
- **Environment template**: `.env.example`

## Cost

**FREE!** No external services required. Uses your existing email account.

## Advantages of Self-Hosted SMTP

✅ **No external dependencies** - No third-party services  
✅ **Zero cost** - Uses your existing email  
✅ **Full control** - Complete ownership of email flow  
✅ **Privacy** - No data shared with third parties  
✅ **Simple setup** - Just configure your email credentials  
✅ **Works anywhere** - Any hosting platform with Python  

## Support

For SMTP-specific issues:
- Check your email provider's SMTP documentation
- Verify app password is correctly generated
- Test SMTP credentials with a simple Python script first

For implementation issues:
- Check console logs for detailed error messages
- Verify all environment variables are set correctly
- Test with a simple form submission

## Testing SMTP Connection

You can test your SMTP settings with this simple Python script:

```python
import smtplib
from email.mime.text import MIMEText

# Your settings
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
USERNAME = "your-email@gmail.com"
PASSWORD = "your-app-password"

try:
    server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    server.starttls()
    server.login(USERNAME, PASSWORD)
    
    msg = MIMEText("Test email from burokrat.site")
    msg['Subject'] = "[TEST] SMTP Configuration"
    msg['From'] = USERNAME
    msg['To'] = USERNAME
    
    server.send_message(msg)
    server.quit()
    print("✅ Success! Email sent.")
except Exception as e:
    print(f"❌ Error: {e}")
```

Save as `test_smtp.py` and run: `python test_smtp.py`
