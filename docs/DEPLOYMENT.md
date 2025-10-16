# Deployment Guide for Burokrat.site

This document provides comprehensive deployment instructions for the Burokrat.site FastHTML application.

## 🌐 Deployment Platform

The application is deployed on **Netlify** as a static site.

- **Production URL**: https://burokrat.netlify.app
- **Admin Dashboard**: https://app.netlify.com/projects/burokrat
- **Project ID**: 5456debb-89ef-42e2-a5eb-22a8c3523f76

## 📋 Prerequisites

Before deploying, ensure you have:

1. **Netlify CLI** installed:
   ```bash
   npm install -g netlify-cli
   ```

2. **Netlify account** linked:
   ```bash
   netlify login
   ```

3. **Python 3.11+** installed with all dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Quick Deployment

### Option 1: Using the Deployment Script (Recommended)

```bash
./deploy.sh
```

This script will:
1. ✅ Check if Netlify CLI is installed
2. 🏗️ Build the static site using `build_static.py`
3. 📊 Display current Netlify status
4. 🚀 Deploy to production (after confirmation)

### Option 2: Manual Deployment

```bash
# 1. Build the static site
python3 build_static.py

# 2. Deploy to Netlify
netlify deploy --prod
```

## 🏗️ Build Process

The static site generation process (`build_static.py`):

1. **Cleans** the `dist/` directory
2. **Copies** all assets from `assets/` to `dist/assets/`
3. **Generates** static HTML files for all routes:
   - `/` → `index.html`
   - `/seals-and-stamps` → `seals-and-stamps.html`
   - `/self-inking-stamps` → `self-inking-stamps.html`
   - `/engraving` → `engraving.html`
   - `/stationery` → `stationery.html`
   - `/about` → `about.html`
   - `/contact` → `contact.html`

### Testing the Build Locally

```bash
python3 build_static.py
```

Expected output:
```
✅ Copied assets to dist/assets
🏗️  Generating static pages...
✅ Generated index.html
✅ Generated seals-and-stamps.html
✅ Generated self-inking-stamps.html
✅ Generated engraving.html
✅ Generated stationery.html
✅ Generated about.html
✅ Generated contact.html

🎉 Static site generated successfully in dist/
📁 Total files: 33
```

## ⚙️ Netlify Configuration

All deployment settings are defined in `netlify.toml`:

### Build Settings
- **Build command**: `python3 build_static.py`
- **Publish directory**: `dist`
- **Python version**: 3.11

### URL Redirects
Clean URLs are configured for all pages (e.g., `/about` → `/about.html`)

### Security Headers
- `X-Frame-Options: DENY`
- `X-XSS-Protection: 1; mode=block`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`

### Cache Control
- **Static assets** (`/assets/*`): 1 year cache
- **HTML files** (`/*.html`): No cache, must revalidate

## 🔍 Checking Deployment Status

```bash
netlify status
```

This shows:
- Current Netlify user
- Project information
- Admin and project URLs

## 📝 Deployment Checklist

Before deploying to production:

- [ ] Test the application locally (`python3 app.py`)
- [ ] Build the static site (`python3 build_static.py`)
- [ ] Verify all pages are generated in `dist/`
- [ ] Check that assets are copied correctly
- [ ] Review any code changes
- [ ] Update version/changelog if applicable
- [ ] Run the deployment script or manual deploy
- [ ] Verify the live site after deployment

## 🐛 Troubleshooting

### Build Fails

**Issue**: `build_static.py` fails to generate pages

**Solutions**:
1. Check Python version: `python3 --version` (should be 3.11+)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Check for syntax errors in route files
4. Verify YAML data files are valid

### Netlify CLI Not Found

**Issue**: `netlify: command not found`

**Solution**:
```bash
npm install -g netlify-cli
```

### Authentication Issues

**Issue**: Not logged into Netlify

**Solution**:
```bash
netlify login
```

### Site Not Linked

**Issue**: Project not linked to Netlify site

**Solution**:
```bash
netlify link
```

## 🔄 Continuous Deployment

For automatic deployments on git push:

1. Connect your GitHub repository to Netlify
2. Configure build settings in Netlify dashboard
3. Push to main branch to trigger automatic deployment

## 📊 Monitoring

After deployment, monitor:

- **Build logs**: Check for any warnings or errors
- **Function logs**: Monitor serverless function performance
- **Analytics**: Track site traffic and performance
- **Error tracking**: Set up error monitoring if needed

## 🌍 Custom Domain

To use a custom domain (e.g., burokrat.site):

1. Go to Netlify dashboard → Domain settings
2. Add custom domain
3. Configure DNS records as instructed
4. Enable HTTPS (automatic with Let's Encrypt)

## 📚 Additional Resources

- [Netlify Documentation](https://docs.netlify.com/)
- [FastHTML Documentation](https://github.com/AnswerDotAI/fasthtml)
- [Project README](README_EN.md)

---

**Last Updated**: October 13, 2025  
**Maintained by**: Andrei Suslov (truvord@gmail.com)
