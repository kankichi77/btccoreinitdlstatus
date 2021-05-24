import os, subprocess, time
os.system("clear")
bc_current = int(subprocess.check_output(["bitcoin-cli", "getblockcount"]).decode("utf-8"))
bc_height = int(subprocess.check_output(["wget", "-O", "-", "https://blockchain.info/q/getblockcount"],stderr=subprocess.DEVNULL).decode("utf-8"))
bc_diff = bc_height - bc_current

print("Current Block Height: %d" % bc_height)
print("Current Block: %d" % bc_current)
print("Diff: %d" % bc_diff)

#time.sleep(1)
#inp = input("in: ")
#print(inp)

