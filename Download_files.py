from urllib import request


book_url = 'https://www.e-reading.club/download.php?book=20412.fb2'

def download_book(fb2_url):
    response = request.urlopen(fb2_url)
    fb2 = response.read()
    fb2_str = str(fb2)
    lines = fb2_url.split("\\n")
    dest_url = r'book.fb2'
    file = open(dest_url, 'w')
    for line in lines:
        file.write(line + "\n")
    file.close()

download_book(book_url)



