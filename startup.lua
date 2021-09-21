path1 = "DC-Bot/cogs/etc/config.py"
path2 = "DC-Bot/API/config.py"

if not os.isfile(path1) then

    config1_file = io.open(path1, "w")
    config1_file:write("TOKEN = ''\nPREFIX = ''\nESCAPE = ''")
    config1_file:close()

else

    print("File ", path1, " already exists")

end

if not os.isfile(path2) then

    config2_file = io.open(path2, "w")
    config2_file:write("URLSCAN_TOKEN = ''\nIQAIR = ''")
    config2_file:close()

else

    print("File ", path2, " already exists")

end

