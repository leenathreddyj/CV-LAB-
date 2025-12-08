"""
Google Drive Video Configuration
Author: Venkata Saileenath Reddy

To get the video file IDs:
1. Open your Google Drive folder: https://drive.google.com/drive/folders/1lcMrrfG2IpClaZ7f3_IJrcou1t0cZ7nM
2. Right-click on each video file → "Get link" → "Copy link"
3. Extract the FILE_ID from the URL (between /d/ and /view)
4. Update the VIDEO_IDS dictionary below with your file IDs

Example:
If the link is: https://drive.google.com/file/d/1ABC123xyz456DEF789/view
Then FILE_ID is: 1ABC123xyz456DEF789
"""

VIDEO_IDS = {
    'module1': '1mh25km2tEaOOjaJgBo9HzjVVKCcJ5o0V',  # Module1.mov
    'module2': '1KmqBymEALua-6F3MavL9jEBuZMDHeBZ9',  # Module2.mov
    'module3': '12WXQXhMdixtEkSsd8JApSw8kuKnyQ9fd',  # Module3.mov
    'module4': '1M0BMf3BbGQOwm5FThveieATHBZSrEplm',  # Module4.mov
    'module5': '177AIYosL-a1bsXV8lj-ieB4_COCnMpcV',  # Module5.mov
    'module7': '1FvtttkdUjp1GCw27hFLr0gjr627xzqI_',  # Module6.mov (for Module 7)
}

def get_video_url(module_name):
    """Get Google Drive embed URL for a module"""
    file_id = VIDEO_IDS.get(module_name, '')
    if file_id:
        return f"https://drive.google.com/file/d/{file_id}/preview"
    return ""

