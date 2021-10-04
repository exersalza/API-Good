path1 = "DC-Bot/cogs/etc/config.py"
path2 = "DC-Bot/API/config.py"
path3 = "DC-Bot/cogs/etc/.env"


local option = io.read()

if option == 'standart' then
  print(option)
  config1_file = io.open(path1, "w")
  config1_file:write("TOKEN = ''\nPREFIX = ''\nESCAPE = ''")
  config1_file:close()

  config2_file = io.open(path2, "w")
  config2_file:write("URLSCAN_TOKEN = ''\nIQAIR = ''")
  config2_file:close()

elseif option == 'repl' then
  config1_file = io.open(path1, "w")
  config1_file:write("import os\n\ndef token_grep(value):\n  return os.getenv(value)\n\nTOKEN = token_grep('TOKEN')\nPREFIX = ''\nESCAPE = ''\n")
  config1_file:close()

  config2_file = io.open(path2, "w")
  config2_file:write("URLSCAN_TOKEN = ''\nIQAIR = ''")
  config2_file:close()

  config3_file = io.open(path3, "w")
  config3_file:write("TOKEN=''")
  config3_file:close()
end



--[[ config2_file = io.open(path2, "w")
config2_file:write("URLSCAN_TOKEN = ''\nIQAIR = ''")
config2_file:close() ]]

