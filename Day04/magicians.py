# 4.1 Traversel list
# 4.2 Watch the errors
magicians = ['alice', 'david', 'carolina']
# Indent two spaces or four spaces doesn't matter
for magician in magicians:
  print(magician)
  print(magician.title() + ", that was a great trick!")
  print("I can't wait to see you your next track, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")