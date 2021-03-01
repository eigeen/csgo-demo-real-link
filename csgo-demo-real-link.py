# -*- coding: utf-8 -*-
import re
import os

print("请输入原始文本\n\
例如MatchInfo Download prepared replays/match730_003467352148457554114_0130544451_234.dem.info...\n")
raw = input(">")

kws = re.findall("replays\/match(\d{3})_([\d]*?_[\d]*?)_([\d]{3}).dem", raw)[0]
reallink = "replay{}.valve.net/{}/{}.dem.bz2".format(kws[2], kws[0], kws[1])
print("真实链接为：{}".format(reallink))
os.system("pause")
