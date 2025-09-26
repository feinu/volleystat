#!/usr/bin/env python
import sys


def parse_match(teamlist, match):
    stats = {
        p[0]: {"name": p[2:], **{k: [0, 0, 0] for k in "abdrsv"}}
        for p in teamlist.split("\n")
        if p and not p.startswith("#")
    }
    global_stats = {
        "oe": 0,
        "ok": 0,
        "tp": 0,
    }
    for point in match.split("\n"):
        if point.startswith("#"):
            continue
        global_stats["tp"] += 1
        for action in point.split(" "):
            if not action:
                continue
            if len(action) == 2:
                global_stats[action] += 1
            elif len(action) == 3:
                stats[action[0]][action[1]][int(action[2])] += 1
            else:
                raise ValueError(f"Invalid action in '{point}'")
    return stats, global_stats


actions = {
        "a": {"name": "Attacks", "args": ("Errors", "Kills", True)},
        "d": {"name": "Digs", "args": ("Errors", "Great")},
        "r": {"name": "Receives", "args": ("Errors", "Great")},
        "v": {"name": "Serves", "args": ("Errors", "Aces", True)},
        "s": {"name": "Sets", "args": ("Errors", "Great")},
        "b": {"name": "Blocks", "args": ("Errors", "Kills")},
}


def statline(line, labeltotal, label0, label2, efficiency=False):
    stat_line = (
        f"{labeltotal: <9}{sum(line): <4}"
        f"{label2: <6}{line[2]: <4}"
        f"{label0: <7}{line[0]: <4}"
    )

    if efficiency:
        percentage = round((line[2] - line[0]) / sum(line) * 100)
        stat_line += f"Efficiency {percentage: >3}%"

    return stat_line


def playerprint(stats):
    for abbrev, p in stats.items():
        print(p["name"])
        for abbrev, action in actions.items():
            print(statline(p[abbrev], action["name"], *action["args"]))
        print()


def actionprint(stats):
    for act, action in actions.items():
        print(f"**{action['name']}**")
        for abbrev, p in stats.items():
            print(statline(p[act], p["name"], *action["args"]))
        print()


def totalprint(stats, global_stats):
    aces = sum(p["v"][2] for p in stats.values())
    kills = sum(p["a"][2] for p in stats.values())
    won = sum((aces, kills, global_stats["oe"]))
    ace_perc = round(aces / won * 100)
    kill_perc = round(kills / won * 100)
    oe_perc = round(global_stats["oe"] / won * 100)
    print("**Summary**")
    print(f"Points won: {won}")
    print(f"  Aces: {ace_perc}%")
    print(f"  Kills: {kill_perc}%")
    print(f"  Opponent Errors: {oe_perc}%")


with open(sys.argv[1], "r") as f:
    text = f.read()

teamlist, match = text.split("\n\n")

stats, global_stats = parse_match(teamlist, match)

playerprint(stats)
print("\n")
actionprint(stats)
totalprint(stats, global_stats)
