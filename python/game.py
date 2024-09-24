class Game:
    def __init__(self):
        self.rooms = {
            "entrance": {
                "description": "You are at the entrance of a dark and eerie castle.",
                "links": ["hallway"]
            },
            "hallway": {
                "description": "A long corridor. There's a door to the north and south.",
                "links": ["entrance", "dungeon", "library"]
            },
            "dungeon": {
                "description": "You stand in a damp dungeon. A treasure glitters in the corner.",
                "links": ["hallway"]
            },
            "library": {
                "description": "Bookshelves tower around you, filled with dust-covered tomes.",
                "links": ["hallway"]
            }
        }
        self.current_room = "entrance"

    def start(self):
        print("Welcome to the Adventure Game!")
        while True:
            print(f"\n{self.rooms[self.current_room]['description']}")
            print(f"You can go: {', '.join(self.rooms[self.current_room]['links'])}")
            input_direction = input("Which direction do you want to go? (or type 'exit' to quit): ").lower()

            if input_direction == "exit":
                print("Thanks for playing!")
                break
            if input_direction in self.rooms[self.current_room]["links"]:
                self.current_room = input_direction
            else:
                print("You can't go that way!")

if __name__ == "__main__":
    game = Game()
    game.start()
