class Youtube:
    _instance = None  # Singleton instance
    #videos = []  # List to store uploaded videos

    def __init__(self):
        self.subscribers = []  # List of subscribers
        self.channel_name = "Twitter"  # Channel name
        self.videos = []  # List to store uploaded videos
        #Youtube._instance = self

    @staticmethod
    def get_instance():
        """Return the single instance of the Youtube class."""
        if Youtube._instance is None:
            Youtube._instance = Youtube()  # Create instance if not already created
        return Youtube._instance

    def subscribe(self, subscriber):
        """Add a subscriber to the channel."""
        self.subscribers.append(subscriber)

    def upload_video(self, video_title):
        """Upload a new video and notify subscribers."""
        self.videos.append(video_title)  # Add video to the videos list
        self.notify_subscribers(video_title)

    def notify_subscribers(self, video_title):
        """Notify all subscribers about the new video."""
        for subscriber in self.subscribers:
            print(f"Hey {subscriber.username}, {self.channel_name} uploaded a new video: {video_title}")
            



class Subscriber:
    def __init__(self, username):
        self.username = username

    def subscribe_to_channel(self):
        """Subscribe to the Singleton Youtube channel."""
        youtube = Youtube.get_instance()
        youtube.subscribe(self)


# Driver Code
if __name__ == "__main__":
    # Step 1: Create subscribers and subscribe to the channel
    subscriber1 = Subscriber("Alice")
    subscriber2 = Subscriber("Bob")

    subscriber1.subscribe_to_channel()
    subscriber2.subscribe_to_channel()

    # Step 2: Access the Youtube instance and upload videos
    youtube_channel = Youtube.get_instance()
    youtube_channel.upload_video("Introduction to Python")
    youtube_channel.upload_video("Advanced Python Tips")
