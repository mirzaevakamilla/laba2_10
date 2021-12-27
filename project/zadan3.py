# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

def music(composer, **titles):
    print(f"Композитор: {composer}")
    for titles, name in titles.items():
        print(f"{titles}: {name}")


if __name__ == "__main__":
    music(
        "Людвиг ван Бетховен",
        произведение="Турецкий марш",
        произведение_1="Симфония №2",
        произведение_2="Фиделио"
    )
