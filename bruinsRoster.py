# NHL Teams have 23 players. Each Club must have a roster of at least 20 players,
# composed of 18 skaters and two goaltenders.
# Players on Injured Reserve do not count in the 23-man limit.

import random

bruinsCenters = ['      #55 Noel Acciari' , '      #37 Patrice Bergeron' , '      #26 Colby Cave' ,
                 '      #17 Ryan Donato' , '      #23 Jakob Forsbacka Karlsson' , '      #43 Danton Heinen' ,
                 '      #46 David Krejci' , '      #52 Sean Kuraly' , '      #20 Joakim Nordstrom' ]

bruinsRightWing = ['  #14 Chris Wagner', '  #88 David Pastrnak', '  #42 David Backes']

bruinsLeftWing = ['   #63 Brad Marchand', '   #74 Jake DeBrusk']

bruinsDefense = ['     #73 Charlie McAvoy', '     #86 Kevan Miller', '     #27 John Moore',
                 '     #58 Urho Vaakanainen', '     #33 Zdeno Chara', '     #47 Torey Krug',
                 '     #25 Brandon Carlo', '     #44 Steven Kampfer', '     #48 Matt Grzelcyk']

bruinsGoalie = ['      #41 Jaroslav Halak', '      #40 Tuukka Rask']

print("\nStarting Roster For The 2018-2019 Boston Bruins\n")

print('Center' +(random.choice(bruinsCenters)))
print('Right Wing' +(random.choice(bruinsRightWing)))
print('Left Wing' +(random.choice(bruinsLeftWing)))
print('Defense' +(random.choice(bruinsDefense)))
print('Defense' +(random.choice(bruinsDefense)))
print('Goalie' +(random.choice(bruinsGoalie)))
