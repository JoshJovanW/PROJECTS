from videos import Video

class Channel:
    def __init__(self):
        self.videos = []
        self.name = "j"

    def make_video(self, vidname):
        vidname = Video(vidname)
        self.videos.append(vidname)
        return f"you have made the video {vidname.name}"

    def see_viewers(self):   
        if len(self.videos) != 0:
            print("\nVideos:\n")
            for vid in self.videos:
                print(f"- {vid.name} - {vid.views} views\n")
        else:
            print("No videos found. \n")

    def view_video(self, name, username):
        video_names = []
        for video in self.videos:
            video_names.append(video.name)
    
        if name in video_names:
            for videos in self.videos:
                if videos.name == name:
                    if username.name in videos.users:
                        return ("You have watched this video before.\n")

                    else:
                        videos.views += 1
                        videos.users.append(username.name)
                        return ("You have watched video " + name +"\n")
                    


    def owner_menu(self):
        return(" - add videos \n - see number of views \n - see list of videos \n - exit \n")

    def name_channel(self, name):
        self.name = name
