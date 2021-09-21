--[[ Open ]] --

config1_file = io.open("DC-Bot/cogs/etc/config.py", "w")
config2_file = io.open("DC-Bot/API/config.py", "w")

-- [[ Write ]] --

config1_file:write("TOKEN = ''\nPREFIX = ''\nESCAPE = ''")
config2_file:write("URLSCAN_TOKEN = ''\nIQAIR = ''")

-- [[ Close ]] --

config1_file:close()
config2_file:close()
