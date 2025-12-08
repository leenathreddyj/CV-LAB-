# Google Drive Video Embedding Setup

## How to Embed Google Drive Videos

1. **Upload your video to Google Drive**
   - Upload your demonstration video to Google Drive
   - Make sure the video is set to "Anyone with the link can view"

2. **Get the Video ID**
   - Open the video in Google Drive
   - Click "Share" → "Get link"
   - Copy the link (format: `https://drive.google.com/file/d/FILE_ID/view`)
   - Extract the `FILE_ID` from the URL

3. **Update the Module Pages**
   - Open the module HTML file (e.g., `templates/module1.html`)
   - Find the iframe with id `module1Video` (or `module2Video`, etc.)
   - Replace the empty `src=""` with: `https://drive.google.com/file/d/YOUR_FILE_ID/preview`

## Example

If your Google Drive link is:
```
https://drive.google.com/file/d/1ABC123xyz456DEF789/view
```

Then your embed URL should be:
```
https://drive.google.com/file/d/1ABC123xyz456DEF789/preview
```

## Module Video IDs

Update these in each module file:

- **Module 1** (`templates/module1.html`): `id="module1Video"`
- **Module 2** (`templates/module2.html`): `id="module2Video"`
- **Module 3** (`templates/module3.html`): `id="module3Video"`
- **Module 4** (`templates/module4.html`): `id="module4Video"`
- **Module 5** (`templates/module5.html`): `id="module5Video"`
- **Module 7** (`templates/module7.html`): `id="module7Video"`

## Quick Setup Script

You can also update all videos at once by searching for:
```html
id="moduleXVideo"
```

And replacing the `src=""` attribute with your Google Drive preview URL.

