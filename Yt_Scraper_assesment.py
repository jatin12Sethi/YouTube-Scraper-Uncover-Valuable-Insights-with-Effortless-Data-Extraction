

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd

# CHROME DRIVER
from selenium import webdriver
Channel_name=input("ENTER THE YOUTUBE CHANNEL NAME :")
# Set the path to ChromeDriver executable
# chrome_driver_path = r'//PATH of YOUR CHROME DRIVER'
# chrome_driver_path = r'C:\Users\user\Desktop\Chromedrivert\Chromedriver'
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)


def scrape_ytchannel(url):
    driver.get(url)
    handle = driver.find_element(By.XPATH, '//yt-formatted-string[@id="channel-handle"]').text
    subscriber_count = driver.find_element(By.XPATH, '//yt-formatted-string[@id="subscriber-count"]').text

    # SCRIPTINO TO SCROLL PAGE UNTIL IT ENDS
    WAIT_IN_SECONDS = 5
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        # Scroll to the bottom of page
        driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
        # Wait for new videos to show up
        time.sleep(WAIT_IN_SECONDS)

        # Calculate new document height and compare it with last height
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    thumbnails = driver.find_elements(By.XPATH, '//a[@id="thumbnail"]/yt-image/img')
    views = driver.find_elements(By.XPATH, '//div[@id="metadata-line"]/span[1]')
    titles = driver.find_elements(By.ID, "video-title")
    links = driver.find_elements(By.ID, "video-title-link")

    videos = []
    for title, view, thumb, link in zip(titles, views, thumbnails, links):
        video_dict = {
            'title': title.text,
            'views': view.text,
            'thumbnail': thumb.get_attribute('src'),
            'link': link.get_attribute('href')
        }
        videos.append(video_dict)
    result = [videos, handle, subscriber_count]

    return result


# url_conf = "https://www.youtube.com/@confindustria/videos"
# # print(scrape_ytchannel(url_conf))
result = scrape_ytchannel("https://www.youtube.com/@" + Channel_name + "/videos")

# Extract the videos, handle, and subscriber count from the result
videos, handle, subscriber_count = result

# Write the video data to a CSV file
filename = 'video_data.csv'
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['YouTube Channel','Title', 'Views', 'Thumbnail', 'Link'])
    for video in videos:
        writer.writerow([Channel_name,video['title'], video['views'], video['thumbnail'], video['link']])

# Append the handle and subscriber count to the CSV file
with open(filename, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Handle', 'Subscriber Count'])
    writer.writerow([handle, subscriber_count])

print('Data stored in', filename)




#extracting the Description AND PUBLISHED DATE

# In[185]:


import csv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Enter your API key here
API_KEY = 'AIzaSyBHN6BvZhF1btAWdoQw7pk9gcQNaG4CEH0'

def perform_operation_on_link(link):
    videos = []
    link = link.split("v=")[1]
    if "&" in link:
        link = link.split("&")[0]

    # Create a YouTube API client
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    try:
        video_response = youtube.videos().list(
            part='snippet,statistics',
            id=link
        ).execute()

        # Extract the video details from the API response
        video_item = video_response['items'][0]
#         video_title = video_item['snippet']['title']
        
#         # Check if the 'likeCount' field is present in the statistics section
#         if 'likeCount' in video_item['statistics']:
#             video_likes = video_item['statistics']['likeCount']
#         else:
#             video_likes = 'N/A'  # Assign a default value or handle it accordingly
        
        video_published = video_item['snippet']['publishedAt']
        video_description = video_item['snippet']['description']

        # Append the video details to the videos list
        videos.append([video_published, video_description])

    except HttpError as error:
        print(f'An error occurred for video ID {link}:', error)

    return videos
filename = 'video_data.csv'
links = []
with open(filename, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    link_index = header.index('Link')  # Find the index of the 'Link' column
    for row in reader:
        if len(row) > link_index:
            link = row[link_index]
            links.append(link)

# Pass each link to the function for performing the operation
all_videos = []
for link in links:
    videos = perform_operation_on_link(link)
    all_videos.extend(videos)

print('Processing the Results!')
# Save the video details in a CSV file
output_filename = 'videos.csv'
with open(output_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Published', 'Description'])
    writer.writerows(all_videos)



video_data = pd.read_csv('video_data.csv')
videos = pd.read_csv('videos.csv')

# Reset the index of the video_data dataframe
video_data.reset_index(drop=True, inplace=True)

# Concatenate the dataframes horizontally, aligning them based on column names
concatenated_data = pd.concat([video_data, videos], axis=1)

# Write the concatenated data to a new CSV file
concatenated_data.to_csv('concatenated_videos.csv', index=False)


print('Results saved in concatenated_videos.csv')
