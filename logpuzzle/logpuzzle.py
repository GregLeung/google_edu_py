
import os
import re
import sys
import urllib
import urlparse

def sort_by_picture_name(url):
  match = re.search(r'puzzle/(.*)', url)
  return match.group()

def sort_by_picture_name_place(url):
  match = re.search(r'puzzle/.*-.*-(.*).jpg', url)
  return match.group(1)

def read_urls(filename):
  f = open(filename)
  urls = re.findall(r'GET\s(.*puzzle/.*.jpg)', f.read())
  urls = list(dict.fromkeys(urls))
  urls = sorted(urls, key=sort_by_picture_name_place)
  filename = filename.split('_')
  result = []
  for url in urls:
    result.append('http://' + filename[1] + url)
  return result
  

def download_images(img_urls, dest_dir):
  f = open('index.html', 'w')
  f.write('<html>')
  f.write('<body>')
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
  count = 0
  files = ''
  for url in img_urls:
    print('Retrieving from: ' + url + '...')
    fileUrl = './imgs/img' + str(count)
    urllib.urlretrieve(url, fileUrl)
    count += 1
    files += '<img src="' + fileUrl + '">'
  f.write(files)
  f.write('</body>')
  f.write('</html>')
  f.close()

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
