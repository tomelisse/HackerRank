def minion_game(string):
    vowels = ('A', 'E', 'I', 'O', 'U')
    # Stuart
    Stuart = 0
    Kevin  = 0
    for i,s in enumerate(string):
        points = len(string)-i
        if s in vowels:
            Kevin  += points
        else:
            Stuart += points
    if Stuart > Kevin:
        print "Stuart",Stuart
    if Kevin > Stuart:
        print "Kevin",Kevin
    if Kevin == Stuart:
        print "Draw"
