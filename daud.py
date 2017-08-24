import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = "/")

@bot.event
async def on_ready():
   print("bot logged on: " + bot.user.name + "//" + bot.user.id)

@bot.command()
async def h():
   await bot.say('With "/d ?" or "/d "[question]?"" I answer to yes/no/maybe or other simple questions. For some *Extra* lines just type in "/d".')

@bot.command()

async def d(arg="whatever"):
   talkdict = {0: "GGGGGGGGGGG GG GGG G",
               1: "Are all artists narcissists?",
               2: "Wakey wakey eggs and bakey",
               3: "I have... one more surprise for you. [Pulls down pants]",
               4: "Let's see if the Outsider will save your life or mine.",
               5: "You want the D(aud)?",
               6: "Now this is a story all about how my life got flipped-turned upside down/And I'd like to take a minute to sit right there/I'll tell you how I became the knife of a town called… Dunwall. Shit, that doesn’t rhyme.",
               7: "Hi my name is Daud and I have a receding hairline (that has nothing to do with my name) and grey eyes like Dunwall clouds and a lot of people tell me I look like Corvo Attano (if u don’t know who he is get da hell out of here!). I’m not related to the Outsider but I wish I was because he’s a major fucking hottie. I’m Marked but the Overseers haven't gotten me yet. I have tanned brown skin. I’m also an assassin, and I live in a shithole called the Flooded District in Dunwall. I’m the boss (in case you couldn’t tell) and I wear mostly red. I love Drapers Ward and I steal all my clothes from there. For example today I was wearing a red coat with matching leather around it and a black pants, 2 belts and black combat boots. I was traversing the city rooftops. I was on a mission so I had money, which I was very happy about. Jessamine Kaldwin stared at me. I put my sword through her.",
               8: "[growls]",
               9: "Who told you I cried myself to sleep last night when the Outsider didn't show up at the shrine?? WAS IT CORVO? I BET IT WAS CORVO.",
               10: "I came out to attack and I am honestly having such a good time right now.",
               11: "I came out to have a good time and I am honestly feeling so attacked right now.",
               12: "Am I responsible for the consequences of my own actions? ....No. It's the black-eyed bastard who is wrong.",
               13: "Hold on- Thomas, turn off the damn tango music! Just because I'm Serkonan doesn't mean I'm going to dance for you.",
               14: "Next time Billie asks what the sultana-eyed asshole smells like, I'm telling her he smells like shit. That's all that comes out of his mouth, anyway.",
               15: "I can monologue better than the black-eyed bastard can.",
               16: "Huh. This cigar tastes like regret.",
               17: "If I had a coin for every person I've kill- wait.",
               18: "Dammit, Jim, I'm an assassin, not an answering machine.",
               19: "Whale god, my ass. God of being a little bitch, that's more like it.",
               20: "[scribbling in diary] What... must I do... to get... Corvo's luscious locks...",
               21: "Corvo and I have so much in common! Do you think he likes me?",
               22: "I'd rather be in the peaceful Serkonan countryside. Anyone who thinks my time is better spent, I don't know, killing a metaphorical whale? Can go screw themselves.",
               23: "My mother warned me never to make an enemy of a witch.",
               24: "The first rule of the Whalers is: you do not talk about the Whalers.",
               25: "gusy my dicl fell out of my slacl into glames lo",
               26: "My dicl fell out of my slacl",
               27: "Me? Responsible for my own actions? I don't know what you're talking about...",
               28: "So what I killed the Empress? It was still the Outsider's fault.",
               29: "Oh so now *I'm* the one to blame? Right...",
               30: "[grunts]",
               31: "The Abbey never changes.",
               32: "Tell it to the Empress.",
               33: "No one should have to kill an Empress. But the Outsider on the other hand...",
               34: "Maybe you should do something more useful than standing by this window, pissing your pants about Corvo.",
               35: "I've had enough [*cough*] killing",
               36: "I'm not impressed.",
               37: "Corvo! Spread the word. Please do.",
               38: "It's a metaphor, see: You put the killing thing right through the Empress's heart, but you don't give it the power to do its - wait, this metaphor isn't working.",
               39: "[grunts] Leave me alone.",
               40: "Error 404 self-pitying monologue not found",
               41: "The world is not kind to Empires, the black-eyed bastard says. Well who is responsible for all the chaos, HMMM?",
               42: "For Void's sake, Billie, can't you see I'm in the middle of a six-month sulk?",
               43: "My favorite musical? It's A Little Knife Music, of course.",
               44: "Now on the sidewalk/Lies a body just oozin' life/And someone's sneakin' 'round the corner/Could that someone be Daud the Knife?",
               45: "I never asked for this.",
               46: "She stood there laughing/I felt the knife in my hand and she laughed no more/My, my, my, Delilah/Why, why, why, Delilah",
               47: "They call me the Knife of Dunwall. Why not the Sword of Dunwall? Does this look like a little knife to you???",
               48: "The name is Dunwall. Knife of.",
               50: "That's not a knife. THIS is a knife.",
               51: "It is I, the Kitchen Knife of Dunwall.",
               52: "The Outsider made me do it!",
               53: "We make our choices, and take what comes. And sooner or later, in ways we can't always fathom, the consequences come back to us.",
               54: "¥oung Money Ca$h Money",
               55: ":knife:",
               56: "You guys are such bastards it's like listening to 2.5 Outsiders",
               57: "Don't ever talk to me or my microwaved sun tea ever again.",
               58: "I'm not that miserable.",
               59: "Do you think if I inscribe a rune and leave it for the Outsider, he'd like me again?",
               60: "I'm writing a new monologue. Do you know any insults that rhyme with 'the Outsider'?",
               61: "Hear that? That's the sound of the Outsider being up to no good.",
               62: "Billie called me 'dad' yesterday.",
               63: "[air horn noise]",
               64: "[the Outsider voice] Fa*S*Ci**N**a**T**InG",
               65: "Nice try. But inside my mind is the last place you want to be.",
               66: "Why am I going to kill the Outsider, you ask? Well... let me tell you.. uh...",
               67: "The Outsider has called me a boring bitch for the last time.",
               68: "Don't kill me! I have children!",
               69: "Wake Me Up Inside (Can't Wake Up)",
               70: "How is Delilah back? I shanked her plant ass, Corvo, I SHANKED HER I TELL YOU",
               71: "Don't talk to me or my 100 adopted children ever again.",
               72: "tfw all of dunwall hates u, but u kno u saved emily kaldwin’s life",
               73: "Any time you think I'm a little soft, you're welcome to come by my office. Bring a blade.",
               74: "I'm so tired.",
               75: "I don't know if you deserve me.",
               76: "Dump your ass directly into the fucking Void...",
               77: "OUTSIDER YOU CAN RUN BUT YOU CAN'T HIDE",
               78: "I could use a laugh.",
               79: "[cronch]",
               80: "Can it wait for a bit? I'm in the middle of some assassinations.",
               81: "DAMN good sun tea.",
               82: "[takes a bite of rotten tyvian pear] What? And Corvo eating rat skewers isn't disgusting?",
               83: "Wait a minute, I need to finish this tin of jellied eels.",
               84: ":dad2:",
               85: ":dad:"
               
               }
   answerdict = {0: "Never Daud it.",
                 1: "Ask the black-eyed bastard.",
                 2: "No.",
                 3: "Honestly?",
                 4: "I never asked for this.",
                 5: "[growls]",
                 6: "I came out to have a good time and I am honestly feeling so attacked right now.",
                 7: "I came out to attack and I am honestly having such a good time right now.",
                 8: "Blame the black-eyed bastard responsible for all this chaos.",
                 9: "You talkin' to me?",
                 10: "Here's another nice mess you've gotten me into!",
                 11: "[grunts]",
                 12: "Go ask someone else.",
                 13: "Yes.",
                 14: "That's enough.",
                 15: "I Daud it.",
                 16: "yeah, rip",
                 17: "That's what I thought.",
                 18: "Ugh this better be worth it...",
                 19: "I don't give a shit.",
                 20: "Ask me again when I've finished my six-month sulk.",
                 21: ":knife:",
                 22: "I'm busy right now- I'm writing a new self-pitying speech.",
                 23: "I honestly have no clue.",
                 24: "Damn kids, get off my Flooded District.",
                 25: "Does the Outsider shit in the Void?",
                 26: "Daud yeah",
                 27: "Daud no",
                 28: "[licks finger, touches the air] Hmm... no.",
                 29: "[licks finger, touches the air] Hmm... yes.",
                 30: "Certainly.",
                 31: "How about no",
                 32: "We'll settle this Serkonan style. [death drops]",
                 33: ":dad2:"
                 }
   randomtalk = random.randrange(0, len(talkdict))
   randomanswer = random.randrange(0, len(answerdict))
   if arg and arg[-1] == "?":
       await bot.say(answerdict[randomanswer])
   else:
       await bot.say(talkdict[randomtalk])

bot.run("MzQ4ODMyMDkyNTI1OTUzMDI2.DHsqyg.saLO9MzoddBvV-6uquBO1lBFJkQ")

