def solution(players, callings):
    answer = 0
    play = dict()
    for i, p in enumerate(players):
        play[p] = i
    for c in callings:
        pr, po = play[c] - 1, play[c]
        play[players[pr]] = po
        play[players[po]] = pr
        players[pr], players[po] = players[po], players[pr]
    return players