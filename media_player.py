class Player:
    def __init__(self, name, video_link, duration):
        self.name = name
        self.video_link = video_link
        self.duration = duration
        self.current_time = 0
        self.quality = "HD"

    def play(self, video_link):
        """
        Відтворює відео за посиланням.
        Повертає True, якщо адреса вірна.
        """
        if video_link == self.video_link:
            print(f"Playing {self.name} - {self.video_link}")
            return True
        else:
            print("Invalid video link. Please check the link.")
            return False

    def pause(self):
        """Ставить на паузу."""
        print("Pausing playback.")

    def save_last_time(self):
        """Зберігає поточний час відтворення."""
        print(f"Saving last time: {self.current_time} seconds.")

    def change_quality(self, new_quality):
        """
        Змінює якість.
        Приймає новий рівень якості та встановлює його.
        """
        self.quality = new_quality
        print(f"Changed quality to {self.quality}.")

if __name__ == "__main__":
    netflix_player = Player(name="Паперовий будинок", video_link="https://www.netflix.com/ua/title/80192098", duration=50)

    netflix_player.play ('https://www.netflix.com/ua/title/80192098')  
    netflix_player.pause() 
    netflix_player.save_last_time()  
    netflix_player.change_quality("4K")  
