# How to Get Google Drive Video IDs

## Step-by-Step Instructions

1. **Open your Google Drive folder:**
   - Go to: https://drive.google.com/drive/folders/1lcMrrfG2IpClaZ7f3_IJrcou1t0cZ7nM

2. **For each video file:**
   - Right-click on the video file (e.g., "Module1.mov")
   - Click "Get link" or "Share"
   - Make sure it's set to "Anyone with the link can view"
   - Copy the link

3. **Extract the File ID:**
   - The link will look like: `https://drive.google.com/file/d/FILE_ID/view?usp=sharing`
   - Copy the `FILE_ID` (the long string between `/d/` and `/view`)

4. **Update video_config.py:**
   - Open `video_config.py`
   - Replace the empty strings with your file IDs:
     ```python
     VIDEO_IDS = {
         'module1': 'YOUR_MODULE1_FILE_ID',
         'module2': 'YOUR_MODULE2_FILE_ID',
         'module3': 'YOUR_MODULE3_FILE_ID',
         'module4': 'YOUR_MODULE4_FILE_ID',
         'module5': 'YOUR_MODULE5_FILE_ID',
         'module7': 'YOUR_MODULE6_FILE_ID',  # Note: Module6.mov is for Module 7
     }
     ```

## Example

If your Module1.mov link is:
```
https://drive.google.com/file/d/1ABC123xyz456DEF789GHI/view?usp=sharing
```

Then in `video_config.py`, set:
```python
'module1': '1ABC123xyz456DEF789GHI',
```

## Quick Method (Alternative)

You can also:
1. Open each video in Google Drive
2. Look at the URL in your browser
3. The file ID is in the URL: `drive.google.com/file/d/FILE_ID/view`

## After Updating

Once you've updated `video_config.py` with all the file IDs:
1. The videos will automatically appear on each module page
2. No need to restart the server (if using debug mode)
3. If videos don't show, make sure the files are set to "Anyone with the link can view"

