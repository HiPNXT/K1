class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link

def read_video():
	title = input("Enter title: ")
	link = input("Enter url: ")
	video = Video(title, link)
	return video
	
def read_videos():
	videos = []
	total_video = int(input("Enter how many videos: "))
	for i in range(total_video):
		print("Enter video", i+1, ": ")
		videos.append(read_video())
	return videos


def print_video(video):
	print("Video title: ", video.title, end = "")
	print("Video link: ", video.link, end = "")

def print_videos(videos):
	print("---------")
	for i in range(len(videos)):
		print_video(videos[i])

def write_video_text(videos, file):
	file.write(videos.title + "\n")
	file.write(videos.link + "\n")

def write_videos_text(videos):
	with open("a.txt", "w") as f:
		f.write(str(len(videos)) + "\n")
		for i in range(len(videos)):
			write_video_text(videos[i], f)

def read_video_text(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video

def read_videos_text():
	videos = []
	with open("a.txt", "r") as f:
		for i in range(int(f.readline())):
			video = read_video_text(f)
			videos.append(video)
	return videos

def main():
	vid = read_videos()
	write_videos_text(vid)
	vid = read_videos_text()
	print_videos(vid)

main()