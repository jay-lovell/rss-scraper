import feedparser
import csv

url = "https://feeds.acast.com/public/shows/blindboy"
feed = feedparser.parse(url)

# Print all entries to the console
# print(feed.entries)

# Print first entry to console
# print(feed.entries[0])

# Loop entries and print certain attributes
# for entry in feed.entries:
#     print("Title: ", entry.title)
#     print("Published: ", entry.published)
#     print("Summary: ", entry.link)

# Output CSV file with selected attributes
# Prepare the CSV file
with open('rss_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['title', 'link', 'published', 'summary', 'duration']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    # Iterate through entries and write to the CSV file
    for entry in feed.entries:
        writer.writerow({'title': entry.title, 'link': entry.link,
                         'published': entry.published, 'summary': entry.summary, 'duration': entry.itunes_duration})


