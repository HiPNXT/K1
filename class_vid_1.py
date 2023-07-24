class Video:
	def __init__(self,title,link):
		self.title = title
		self.link = link

def read_video():
	title = input("Enter your title: ")
	link = input("Enter your link: ")
	print("\n")
	return Video(title,link)

def read_videos():
	total_vid = int(input("Enter how many video: "))
	videos = []
	for i in range(total_vid):
		print("Video ", i+1)
		videos.append(read_video())
	return videos

def print_video(video):
	print("Your video is:",video.title, end = "")
	print("Your link is:",video.link, end = "")
	print("\n")

def print_videos(videos):
	print("------------")
	for i in range(len(videos)):
		print("Video number", i+1)
		print_video(videos[i])

def write_video_text(videos, file):
	file.write(videos.title + "\n")
	file.write(videos.link + "\n")

def write_videos_text(videos):
	with open("a.txt", "w") as f:
		f.write(str(len(videos)) + "\n")
		for i in range(len(videos)):
			write_video_text(videos[i],f)

def read_video_text(file):
	title = file.readline()
	link = file.readline()
	return Video(title, link)

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