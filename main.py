import requests
from bs4 import BeautifulSoup

archive_url = "Website Link"

def get_video_links(url):
    scrap = requests.get(url)
    soup = BeautifulSoup(scrap.content, 'html5lib')
    links = soup.findAll('a')
    videoLinks = [url + link['href'] for link in links if link['href'].endswith('mp4')]

    return videoLinks


def download_video_series(videoLinks):
    for link in videoLinks:
        file_name = link.split('/')[-1]

        print("Downloading file:%s" % file_name)

        r = requests.get(link, stream=True)

        # download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        print("%s downloaded!\n" % file_name)

    print("All videos downloaded!")
    return


if __name__ == "__main__":
    download_video_series(get_video_links(archive_url))
