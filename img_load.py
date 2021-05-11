from bing_image_downloader import downloader

downloader.download('apple fruit', limit=3, output_dir='dataset/train')
# downloader.download('fresh guava', limit=350, output_dir='dataset/test')