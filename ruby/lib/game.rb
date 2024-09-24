class Game
  def initialize
    @rooms = {
      "entrance" => {
        description: "You are at the entrance of a dark and eerie castle.",
        links: ["hallway"]
      },
      "hallway" => {
        description: "A long corridor. There's a door to the north and south.",
        links: ["entrance", "dungeon", "library"]
      },
      "dungeon" => {
        description: "You stand in a damp dungeon. A treasure glitters in the corner.",
        links: ["hallway"]
      },
      "library" => {
        description: "Bookshelves tower around you, filled with dust-covered tomes.",
        links: ["hallway"]
      }
    }
    @current_room = "entrance"
  end

  def start
    puts "Welcome to the Adventure Game!"
    while true
      puts "\n#{@rooms[@current_room][:description]}"
      puts "You can go: #{@rooms[@current_room][:links].join(', ')}"
      print "Which direction do you want to go? (or type 'exit' to quit): "
      input = gets.chomp.downcase

      break if input == 'exit'
      if @rooms[@current_room][:links].include?(input)
        @current_room = input
      else
        puts "You can't go that way!"
      end
    end
    puts "Thanks for playing!"
  end
end
