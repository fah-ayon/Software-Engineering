class Facebook:
    def create_friends_group(self):
        print("Welcome to the group")

    def use_news_feed(self):
        print("Scroll through news feed")


class Messenger:
    def send_message(self):
        print("Let's Message each other")


class Twitch:
    def streaming_video(self):
        print("Videos from twitch")


class WeChat:
    _instance = None

    def __init__(self):
        if WeChat._instance is not None:
            raise Exception("This is a singleton class. Use get_instance() method.")
        self.facebook = Facebook()
        self.twitch = Twitch()
        self.messenger = Messenger()

    @staticmethod
    def get_instance():
        if WeChat._instance is None:
            WeChat._instance = WeChat()
        return WeChat._instance

    def send_message(self):
        print("WeChat has its own message to send")
        self.messenger.send_message()

    def use_news_feed(self):
        print("Let's use the News Feed")
        self.facebook.use_news_feed()

    def streaming_video(self):
        print("Let's stream videos")
        self.twitch.streaming_video()

    def create_friends_group(self):
        print("Let's create friends group")
        self.facebook.create_friends_group()


# Driver Code
if __name__ == "__main__":
    we_chat = WeChat.get_instance()
    we_chat.streaming_video()

    we_chat2 = WeChat.get_instance()
    we_chat.send_message()
    we_chat2.use_news_feed()

    print(we_chat)
    print(we_chat2)
