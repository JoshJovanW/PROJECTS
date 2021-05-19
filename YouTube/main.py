from user import User
from videos import Video
from channel import Channel

def main():
    channel = Channel()

    print("welcome to youtube.")

    app = "open"

    while app == "open":
        identity = input("\nlogin as user or creator?\n").lower()

        if identity == "user":
            username = input("What is your name? ")
            username = User(username)
            print("\nwelcome " + username.name + "\n")
            print(username.user_menu())

            while identity == "user":
                action = input("what do you want to do? (view/logout/exit)\n").lower()
                print("\n")

                if action == "view":   
                    if len(channel.videos) != 0:
                        print("\nVideos available:\n")
                        for vid in channel.videos:
                            print(f"- {vid.name} \n")
                        choice = input("What do you want to watch? (video name)\n")
                        print("\n")
                        print(channel.view_video(choice, username))
                    
                    else:
                        print("We're sorry there are no videos at the moment. \n")

                elif action == "logout":
                    identity = "undefined"
                    break

                elif action == "exit":
                    print("Thank you for using Youtube")
                    app = "close"
                    break
                    
    
        if identity == "creator":
            if channel.name == "":
                channel_name = input("What do you want to name your channel?\n")
                channel.name_channel(channel_name)

            print("welcome , " + channel.name +"\n")

            print(channel.owner_menu())

            while identity == "creator":
                action = input("What do you want to do? (add, views, list, logout, exit) \n")
                print("\n")

                if action == "add":
                    vidname = input("What is the name of the video? \n")
                    print(channel.make_video(vidname))
                    print("\n")

                elif action == "views":
                    channel.see_viewers()

                elif action == "list":
                    if len(channel.videos) != 0:
                        print("\nVideos:\n")
                        for vid in channel.videos:
                            print(f"- {vid.name} \n")
                    else:
                        print("No videos found. \n")

                elif action == "logout":
                    identity = "undefined"
                    continue

                elif action == "exit":
                    print("Thank you for using Youtube")
                    app = "close"
                    break
main()
