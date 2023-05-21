## YouTube-Scraper-Uncover-Valuable-Insights-with-Effortless-Data-Extraction

This YouTube Scraper is a powerful tool designed to extract comprehensive data from YouTube channels and individual videos. By combining the capabilities of Selenium and the YouTube API, this scraper enables you to scrape all the data from YouTube channels and dive deep into the details of each video.
![youtube-data-scraping](https://github.com/jatin12Sethi/YouTube-Scraper-Uncover-Valuable-Insights-with-Effortless-Data-Extraction/assets/98033741/6b3a6ade-a09c-47bb-9221-b3b5c7df912a)


## Features

- Channel Data Extraction: Extract detailed information about YouTube channels, including channel name, description, subscriber count, video count, and upload dates.
- Video Data Extraction: Scrape data from individual YouTube videos, such as video title, description, duration, view counts, likes, dislikes, comments, and more.
- Selenium Integration: Utilize Selenium to scrape the channel video links, overcoming limitations caused by ad blocking and other obstacles.
- YouTube API Integration: Augment the Selenium scraping with the YouTube API to fetch detailed information for each video, ensuring accuracy and efficiency.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using the following command:
```
pip install -r requirements.txt
```
3. Set up your YouTube API credentials by following the instructions provided by the YouTube API documentation.

## Usage

1. Open the `config.py` file and enter your YouTube API credentials.
2. Customize the scraping parameters in the `scraper.py` file according to your requirements, such as the YouTube channel URLs and the data fields you want to scrape.
3. Run the `scraper.py` script using the command:
```
python yt_scrapeer_assesment.py
```
4. The script will start scraping the channel data and video information using Selenium and the YouTube API. The scraped data will be saved to a CSV file for further analysis.

## Screenshots

![download](https://github.com/jatin12Sethi/YouTube-Scraper-Uncover-Valuable-Insights-with-Effortless-Data-Extraction/assets/98033741/4f7d8143-8671-4da1-82b7-5591616ae4b4)

![download](https://github.com/jatin12Sethi/YouTube-Scraper-Uncover-Valuable-Insights-with-Effortless-Data-Extraction/assets/98033741/3904e252-dfc2-44d0-89db-a354f0956ead)

![download](https://github.com/jatin12Sethi/YouTube-Scraper-Uncover-Valuable-Insights-with-Effortless-Data-Extraction/assets/98033741/b0b78d6e-cc3b-4ae9-b977-a36453454f07)

## Contributing

Contributions to this project are welcome! If you have any ideas for improvements, new features, or bug fixes, please submit a pull request. Make sure to follow the contribution guidelines provided in the repository.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this code for your own purposes.

## Acknowledgements

- [Selenium](https://www.selenium.dev/)
- [YouTube Data API](https://developers.google.com/youtube/v3)

Please note that scraping data from YouTube should comply with YouTube's terms of service and API usage policies. Use this tool responsibly and respect YouTube's guidelines.
