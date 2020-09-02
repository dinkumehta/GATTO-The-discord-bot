import os
from datetime import datetime 
import pytz 
import time

UTC = pytz.utc from discord.ext import commands

client = commands.Bot(command_prefix=".")
TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    print("Logged in as {}({})".format(client.user.name, client.user.id))

@client.command()
async def puspus(ctx):
	timeZ_Kl = pytz.timezone('Asia/Kolkata') 
	dt_Kl = datetime.now(timeZ_Kl) 
	# finding the time aoocind to 24 hrs clock........
	local= dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z').split()[1]
	time1=""
	for i in local:
		if(i==':'):
			break
		time1+=i 
	time1=int(time1)
	#finding the day hdsiojd 
	day=time.ctime().split()[0]
	await ctx.send(f"{time1} , {day}")
	if(day=='Mon'):
		if(time1==1+12):
			await ctx.send("AP by varun")			
			await ctx.send("https://meet.google.com/lookup/frazjfw4w6?authuser=1&hs=179")			
		elif(time1==2+12):
			await ctx.send("COA")			
			await ctx.send("https://meet.google.com/lookup/f5kcqcas3e")
		elif(time1==3+12):
			await ctx.send("IDBMS")
			await ctx.send("https://meet.google.com/lookup/evx4lzq2xa?authuser=1&hs=179")
		elif(time1==4+12):		
			await ctx.send("DCS")
			await ctx.send("https://meet.google.com/lookup/gcfpz2o5ch?authuser=1&hs=179")
		elif(time1==5+12):		
			await ctx.send("M3")
			await ctx.send("https://meet.google.com/lookup/eqdw27ysw5?authuser=1&hs=179")
		else:
			await ctx.send("Rn koyi class koni hjdhfjahsdfjkg")
	elif(day=='Tue'):
		if(time1==9):
			await ctx.send("IDBMS's lab")			
			await ctx.send("teacher tatti h kuch nhi krvayeag so u can sleep")			
			await ctx.send("https://meet.google.com/lookup/g232xe3juu?authuser=1&hs=179")					
		elif(time1==1+12):
			await ctx.send("doubt class h and ik u haven't seen the video so chill kr")
		else:
			await ctx.send("mje kr be !!!!!!!!!!!!!!!!")		
	elif(day=='Wed'):
		if(time1==5+12):
			await ctx.send("AP by varun")			
			await ctx.send("https://meet.google.com/lookup/frazjfw4w6?authuser=1&hs=179")			
		elif(time1==1+12):
			await ctx.send("COA")			
			await ctx.send("https://meet.google.com/lookup/f5kcqcas3e")
		elif(time1==2+12):
			await ctx.send("IDBMS")
			await ctx.send("https://meet.google.com/lookup/evx4lzq2xa?authuser=1&hs=179")
		elif(time1==3+12):		
			await ctx.send("DCS")
			await ctx.send("https://meet.google.com/lookup/gcfpz2o5ch?authuser=1&hs=179")
		elif(time1==4+12):		
			await ctx.send("M3")
			await ctx.send("https://meet.google.com/lookup/eqdw27ysw5?authuser=1&hs=179")
		else:
			await ctx.send("NO calss hsadfjhsdgah")
	elif(day=='Thu'):
		if(time1==10):
			await ctx.send("AP's lab")			
			# await ctx.send("teacher tatti h kuch nhi krvayeag so u can sleep")			
			await ctx.send("https://meet.google.com/lookup/htvdf4mslf?authuser=1&hs=179")					
		elif(time1==1+12):
			await ctx.send("doubt class h and ik u haven't seen the video so chill kr")
		else:
			await ctx.send("mje kr be !!!!!!!!!!!!!!!!")		
	elif(day=="Fri"):
		if(time1==4+12):
			await ctx.send("AP by varun")			
			await ctx.send("https://meet.google.com/lookup/frazjfw4w6?authuser=1&hs=179")			
		elif(time1==5+12):
			await ctx.send("COA")			
			await ctx.send("https://meet.google.com/lookup/f5kcqcas3e")
		elif(time1==1+12):
			await ctx.send("IDBMS")
			await ctx.send("https://meet.google.com/lookup/evx4lzq2xa?authuser=1&hs=179")
		elif(time1==2+12):		
			await ctx.send("DCS")
			await ctx.send("https://meet.google.com/lookup/gcfpz2o5ch?authuser=1&hs=179")
		elif(time1==3+12):		
			await ctx.send("M3")
			await ctx.send("https://meet.google.com/lookup/eqdw27ysw5?authuser=1&hs=179")
		else:
			await ctx.send("NO calss hsadfjhsdgah")
	else:
		await ctx.send("i duuno jk no class today sjkhsgd")

if __name__ == "__main__":
    client.run(TOKEN)
