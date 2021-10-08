import time

animation = [
"[        ]",
"[=       ]",
"[===     ]",
"[====    ]",
"[=====   ]",
"[======  ]",
"[======= ]",
"[========]",
"[ =======]",
"[  ======]",
"[   =====]",
"[    ====]",
"[     ===]",
"[      ==]",
"[       =]",
"[        ]",
"[        ]"
]

notcomplete = True

i = 0
while notcomplete:
  try:
    while notcomplete:
        print(animation[i % len(animation)], end='\r')
        time.sleep(.1)
        i += 1
  except KeyboardInterrupt:
    print('you cant stop me')