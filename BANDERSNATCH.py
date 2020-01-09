from datetime import datetime
import math

# def getTime():
# 	(dt, micro) = datetime.utcnow().strftime('%Y%m%d%H%M%S.%f').split('.')
# 	dt = "%s%03d" % (dt, int(micro) / 1000)
# 	return dt
#
# def timeElapsed(start):
# 	end = getTime()
# 	minutes = math.floor((int(end) - int(start)) / 1000 / 60)
# 	seconds = math.floor((int(end) - int(start)) / 1000 % 60)
# 	return str(minutes) + " Minutes " + str(seconds) + " Seconds"

done = False
inventory = []
suspects = []
checkpoints = []
# start_time = 0

#intro & instructions
print("")
print("")
print("RIPPER MURDER MYSTERY")
print("---------------------------------------------------------------------------------------------")
print("")
print("")
print("INTRODUCTION")
print("")
print("")
print("It is November 9, 1888 in London.")
print("You are on your way home when you see that it is surrounded by policemen.")
print("They tell you what happened. Your best friend and roommate, Mary, has been killed in the apartment you both share. ")
print("Not just killed -- mutilated viciously. Toes severed, internal organs placed beneath her head and on her bedside table. ")
print("At first, you refuse to believe it. But then, all the evidence lines up: She is the fifth victim of Jack the Ripper. ")
print("")
print("")
print("---------------------------------------------------------------------------------------------")
print("INSTRUCTIONS")
print("")
print("You are tasked with trying to find who Jack the Ripper is and avenging Mary. ")
print("")
print("Open Mary's contact book to find new suspects")
print("When a new suspect is added, you can choose to investigate them")
print("During the investigation, you will occasionally be asked to (c) continue or (o) view options")
print("Choose to continue if you want to continue with your storyline.")
print("Choose to view options if you think you know who did it or if you want to investigate a new suspect.")
print("If you continue an investigation when you think the suspect is innocent, you risk 1) getting a bad ending or 2) running out of time")
print("There are more bad endings than good ones.")
print("")
print("YOU HAVE 15 MINUTES TO FIND THE RIPPER.")
print("HAVE FUN, AND GOOD LUCK. \nTIP: TRY NOT TO DIE.")
print("")
start_time = getTime()
hm = input("Would you like to start? (y or n)")
if hm == "y":
	print("")
else:
	print("Goodbye!")
	done = True



#code thingz
# Set Starting Time
# start_time = getTime()
# print(timeElapsed(start_time))
while not done:
	#time

	print("---------------------------------------------------------------------------------------------")
	print("\n \nOPTIONS")
	print("")
	print("TYPE “M” IF YOU WANT TO SEE HOW MANY MINUTES HAVE ELAPSED")
	print("")
	print("TYPE “V” IF YOU WANT TO VIEW ALL YOUR SUSPECTS. ")
	print("")
	print("TYPE “S” IF YOU WANT TO INVESTIGATE A SUSPECT. ")
	print("")
	print("TYPE “I” IF YOU WANT TO VIEW YOUR INVENTORY AND SEE ALL THE CLUES YOU HAVE GATHERED. ")
	print("")
	print("TYPE “A” IF YOU THINK YOU KNOW WHO THE KILLER IS AND WANT TO ALERT THE AUTHORITIES. ")
	print("")
	print("TYPE “C” IF YOU WANT TO ACCESS MARY'S CONTACTS BOOK.")
	print("")
	cosa = input("What do you want to do? ")
	#see minutes
	if cosa == "m":
		print("---------------------------------------------------------------------------------------------")
		print("")

		print("You have been playing for.")
		# print(timeElapsed(start_time))
		continue
	#investigate suspects
	elif cosa == "s":
		print("---------------------------------------------------------------------------------------------")
		print("")
		if suspects == []:
			print("You have no suspects to investigate yet!")
			continue
		else:
			print("Who would you like to investigate? \n", suspects)
			seuss = input("")
			if seuss == "aaron kosminsksi":
				thing = -3
			elif seuss == "thomas neill cream":
				thing = 3
			elif seuss == "joseph barnett":
				thing = 1
			elif seuss == "carmen dilaurentis":
				thing = 4
			elif seuss == "officer murrey":
				thing = -4
			else:
				print("Not a choice!")
				continue
	#view suspects
	elif cosa == "v":
		print("---------------------------------------------------------------------------------------------")
		print("")
		if suspects == []:
			print("You have no suspects yet!")
			continue
		else:
			print("")
			print("Your suspects are: ",suspects)
			continue
	#view inventory
	elif cosa == "i":
		print("---------------------------------------------------------------------------------------------")
		print("")
		if inventory == []:
			print("")
			print("There is nothing in your inventory!")
		else:
			print("")
			print("In your inventory, you have: ",inventory)
		continue
	#alert authorities
	elif cosa == "a":
		print("---------------------------------------------------------------------------------------------")
		print("")
		if suspects == []:
			print("You have no suspects to alert the authorities of!")
			continue
		else:
			print("You have chosen to alert the authorities.")
			print("Who would you like to accuse of being Jack the Ripper?")
			print("Your suspects are: ", suspects)
			flower = input("")
			if "letter" in inventory:
				print("")
				print("The police came and saw that you had a letter in the Ripper's handwriting. Because you didn't tell them about it, they think it is yours. They arrest you")
				print("GAME OVER")
				done = True
			else:
				if flower == "thomas neill cream":
					print("")
					print("You are wrong!")
					done = True
				elif flower == "aaron kosminski":
					print("")
					print("You are wrong!")
					done = True
				elif flower == "joseph barnett":
					print("")
					print("You are wrong!")
					done = True
				elif flower == "carmen dilaurentis":
					print("")
					print("You are wrong!")
					done = True
				elif flower == "officer murrey":
					print("")
					print("You are wrong!")
					done = True
				elif flower == "chet kipparjer":
					print("")
					print("You caught Jack the Ripper! How did you do it? The authorities track down Chet and he confesses to all the murders.")
					print("GAME OVER")
					done = True
				else:
					print("")
					print("Not a choice!")
					continue
	#see contact book
	elif cosa == "c":
		print("---------------------------------------------------------------------------------------------")
		print("")
		print("You look through Mary’s contact book to find suspects.")
		print("")
		print("You know three things to look for in suspects:")
		print("")
		print("a) Medical skills")
		print("")
		print("b) Occupation as a barber")
		print("")
		print("c) Motivation for killing Mary")
		print("")
		choice = input("What would you like to look for?")
		if choice == "a":
			print("")
			if "Thomas Neill Cream" in suspects:
				print("THOMAS NEILL CREAM IS ALREADY IN YOUR LIST OF SUSPECTS.")
			else:
				print("You find one possible suspect: THOMAS NEILL CREAM. \nHe is listed in Mary's contact book as a doctor. He lives around the Whitechapel area.")
				print("\n \nTHOMAS NEILL CREAM HAS BEEN ADDED TO YOUR LIST OF SUSPECTS.")
				suspects.append("Thomas Neill Cream")
				golly = input("Would you like to a) start your investigation on Thomas or b) view options?")
				if golly == "a":
					thing = 3
				elif golly == "b":
					continue
				else:
					print("Not an option!")
					continue
		elif choice == "b":
			print("")
			if "Aaron Kosminski" in suspects:
				print("AARON KOSMINSKI IS ALREADY IN YOUR LIST OF SUSPECTS.")
			else:
				print("You find one possible suspect: AARON KOSMINSKI. \nHe is listed in Mary's contact book as a barber. He lives around the Whitechapel area.")
				print("\n \nAARON KOSMINSKI HAS BEEN ADDED TO YOUR LIST OF SUSPECTS.")
				suspects.append("Aaron Kosminski")
				golly = input("Would you like to a) start your investigation on Aaron or b) view options?")
				if golly == "a":
					thing = -3
				elif golly == "b":
					continue
				else:
					print("Not an option!")
					continue
		elif choice == "c":
			print("")
			if "Joseph Barnett" in suspects:
				print("JOSEPH BARNETT IS ALREADY IN YOUR LIST OF SUSPECTS.")
			else:
				print("You find one possible suspect: JOSEPH BARNETT. \nHe is Mary's ex husband. The two did not get along, and he left their divorce on unfriendly terms. ")
				print("\n \nJOSEPH BARNETT HAS BEEN ADDED TO YOUR LIST OF SUSPECTS. ")
				suspects.append("Joseph Barnett")
				golly = input("Would you like to a) start your investigation on Joseph or b) view options?")
				if golly == "a":
					thing = 1
				elif golly == "b":
					continue
				else:
					print("Not an option!")
					continue
		else:
			print("")
			print("Not a choice!")
			continue
	else:
		print("Not a choice!")
		continue
	#thomas
	if thing == 3:
		print("---------------------------------------------------------------------------------------------")
		print("YOU HAVE STARTED YOUR INVESTIGATION ON THOMAS NEILL CREAM")
		print("")
		choice = input("Would you like to a) call Thomas or b) view options?")
		if choice == "a":
			print("")
			print("You call Thomas. He picks up pretty fast.")
			print("“Hello?” he says. He sounds wary, surprised.")
			print("“Good evening,” you say.")
			print("“Oh, yes, uh, what can I help you with?” he asks.")
			print("")
			print("WHAT WOULD YOU LIKE TO REPLY WITH?")
			print("")
			print("a) I was wondering if you knew anything about the Whitechapel Murders.")
			call = input("b) What services do you provide?")
			if call == "a":
				print("")
				print("“No, I uh, I don't. It’s devastating, what’s happening. If you don’t mind me asking, what's your name? So that if I find anything...” he trails off.")
				print("You tell him your name. \n“If you find any extra information,” you say, “please call me back and tell me!”")
				print("He agrees, sounding a bit too amicable, and hangs up hurriedly.")
				print("")
				notcreative = input("Press (c) to continue , press (o) to view options")
				if notcreative == "o":
					continue
				if notcreative == "c":
					print("")
					print("A few days later, you get a call. It is from Thomas. \nWhen you pick up, his voice is hushed. As if he is about to tell you a secret. \n“Hello?” you say. “Did you fin-”\n“Listen,” he says. His voice is intense. “You want information?”\n“Yes,” you say. \n“Aaron Kosminski,” he whispers. His voice is unrecognizable. And then he hangs up the phone.")
					print("")
					print("DO YOU WANT TO")
					print("")
					print("a) trust Thomas and investigate Aaron instead")
					ack = input("b) don't trust Thomas and continue your investigation? \n")
					if ack == "a":
						print("\n \nAARON KOSMINSKI HAS BEEN ADDED TO YOUR LIST OF SUSPECTS")
						if "Aaron Kosminski" in suspects:
							thing = -3
							continue
						else:
							suspects.append("Aaron Kosminski")
							thing = -3
						continue
					elif ack == "b":
						print("")
						print("You decide that Thomas is not to be trusted. \nThere is a letter in the mail, and it is addressed to you. Whoever wrote it spelt your name wrong.")
						print("")
						print("The letter says this: \n I hear you’re trying to find me. When I heard that I almost died laughing. The police can’t catch me, and.. you’re different? \n    You should’ve just told me you wanted to meet me! \n    Who said you had to come to me?\n   I'm an awful polite man-- I’ll come to you. \n  Signed,\n   Mr. Jack")
						print("")
						print("The letter is in the same handwriting as the Dear Boss letter the Ripper had sent to the police a few months ago. \nWhoever sent you this letter, it wasn't a fake. This was actually Jack. \nHow does he know your name? And how did he find where you live? He must've known you lived with Mary.")
						print("")
						boom = input("DO YOU WANT TO \n \na) contact the authorities \nb) keep the letter to yourself")
						if boom == "a":
							print("")
							print("You contact the authorities and they ask you why you are in possession of such a letter. You tell them you do not know. They take the letter. The authorities are now on the lookout, watching you. \nDon’t do anything suspicious, you tell yourself. \nBut you aren’t sure if it’s as easy as it sounds.")
							print("")
							chicka = input("Press (a) to continue, press (o) to view options")
							if chicka == "o":
								continue
							elif chicka == "a":
								print("")
								print("News of the letter has spread.\nPeople believe that you turned your own letter in, to throw suspicion off yourself. \nSuddenly the fact that you lived with and had access to the apartment of the girl who’s been murdered is much more blatant.\nYou are uneasy about the fact that Jack the Ripper knows where you live and what your name is.")
								boomboom = input("\n \nDO YOU WANT TO MOVE SOMEPLACE ELSE? (y or n)")
								if boomboom == "y":
									print("\n \nYou move to a small house away from everything.")
									print("\n \nYou decide to investigate someone new.")
									continue
								elif boomboom == "n":
									print("")
									print("You stay in your apartment.")
									lmao = input("\n \nDO YOU WANT TO BUY WEAPONS IN CASE THE RIPPER COMES? (y or n)")
									if lmao == "y":
										print("\n \nYou buy weapons and leave them hidden around the house. If the Ripper comes, you will not be unprepared. \nThe problem is that the Ripper wasn’t after you. \nYour neighbor is killed, in the patented Jack the Ripper style. \nAnd the weapons that you bought? One of them was the murder weapon. \nThe evidence is overwhelming. \nJack the Ripper has successfully framed you.")
										print("GAME OVER")
										done = True
									elif lmao == "n":
										print("")
										print("You are anxious in your room. You’ve locked the doors. The windows. The everything. \nIt doesn’t seem like it is enough. \n \nThere is somebody at the door. \nThere is somebody at the door. \nTHERE IS SOMEBODY AT THE DOOR.")
										oop = input("HELP")
										if oop == "ok":
											print("\n \nThere is nothing you can do to help yourself")
											print("The door is broken down. \nWhile you are bleeding out, you are cursing yourself because you finally know who Jack the Ripper is when there is nobody to tell.")
											HAHA = input("Do you want to know who it is? (y or n)")
											if HAHA == "y":
												print("\n \nYou die before you can utter another word.")
												print("GAME OVER")
												done = True
											elif HAHA == "n":
												print("\n \nYou die before you can utter another word.")
												print("GAME OVER")
												done = True
										else:
											print("\n \nThere is nothing you can do to help yourself")
											print("The door is broken down. \nWhile you are bleeding out, you are cursing yourself because you finally know who Jack the Ripper is when there is nobody to tell.")
											HAHA = input("\n \nDo you want to know who it is? (y or n)")
											if HAHA == "y":
												print("You die before you can utter another word.")
												print("GAME OVER")
												done = True
											if HAHA == "n":
												print("You die before you can utter another word.")
												print("GAME OVER")
												done = True
						elif boom == "b":
							print(" \nYou do not contact the authorities and keep the letter to yourself.")
							print("\n \n LETTER HAS BEEN ADDED TO YOUR INVENTORY")
							print("")
							print("Since the Ripper knows where you live, you decide to move to a more secluded neighborhood.")
							inventory.append("letter")
							print("\n \nWOULD YOU LIKE TO")
							print("a) Inspect the letter for clues")
							fbi = input("b) Inspect Mary's crime scene")
							if fbi == "a":
								print("")
								print("You look at the letter closely, trying to find hidden clues. \nYou take out Mary’s contact book and compare handwriting. \nThe handwriting that it belongs to? \nNone other than Thomas Niell Cream.")
								print("")
								print("Your letter and whoever wrote Thomas' name in Mary's contact book is the same. ")
								print("It is clear that Thomas is hiding something. \nYou decide to find his office and pay him a little visit.")
								pedo = input("\n \nWOULD YOU LIKE TO TAKE A KNIFE WITH YOU? (y or n) ")
								if pedo == "y":
									inventory.append("knife")
									print("A KNIFE HAS BEEN ADDED TO YOUR INVENTORY.")
									print("")
									print("You find Thomas in his office. You hope that he doesn’t recognize you as the person who called him on the phone.")
									print("He is a regular looking man with a beard and brown hair.")
									print("“Hello,” you say. “I’m terribly ill, and this was the closest doctor’s office to my work. Could you write a sick note for me?”")
									print("Thomas looks you up and down. His eyes are cunning, manipulative.")
									print("“What are you sick with?” he asks, bored.")
									print("“Polio?”")
									print("He gives you a look, but writes it down anyways.")
									print("“And what’s your name?”")
									print("You lie.")
									print("“Thank you,” you say, when he gives you the note.")
									inventory.append("doctor's note")
									print("\n \nDOCTORS NOTE HAS BEEN ADDED TO YOUR INVENTORY. \n \nWhen you get home to look at it, you are disappointed to find that the handwriting is vastly different from that of the letter's.")
									hm = input("\n \nWOULD YOU LIKE TO CONTINUE THE INVESTIGATION? (y or n) ")
									if hm == "n":
										continue
									if hm == "y":
										adam = input("\n \nWOULD YOU LIKE TO \na) discard the letter \nb) keep the letter")
										if adam == "a":
											inventory.remove("letter")
											print("")
											print("A few days later, another Ripper letter is sent out. Left on the doorstep of the police’s station. It's a different handwriting than the other Ripper letters: it doesn't match the dear Boss letter, or your letter. \nIt reads:\n  Dear mr. Satan,	\n  I am  having so fun! My toes tingle down everytime I do I job, but the best part boss is, the idiots playing hide n seek with me! \n    They think they are on something but I dont think they will ever win this game. \n    Its their fault, they shouldntve gave me so much time to hide!\n    Sincerely\n Ripper, Jack\n \nThe letter came in a box with severed toes painted bright red. You don’t want to think about whether those toes were Mary’s.\nNo, instead, you think about how the handwriting in the dear mr. Satan letter matches perfectly with your doctor’s note. ")
											checkpoints.append("checkpoint 1")
											ronan = input("\n \nWOULD YOU LIKE TO \na) alert authorities \nb) stay solo")
											if ronan == "a":
												print("")
												print("The authorities tell you that Thomas is supposed to be in prison.")
												print("Thomas is a murderer himself. He’s incarcerated for poisoning people through the pills he prescribes them.")
												doki = input("Press (c) to continue, (o) to view options.")
												if doki == "o":
													continue
												elif doki == "c":
													print("You and the authorities pay Thomas a visit together.")
													print("The security guards at Thomas’s prison are told to check his cell.")
													print("When you arrive at Thomas’s office, you find that the man with the beard is there.")
													print("“Did you get polio again?” he asks drily.")
													print("His face stops looking so bored when the police burst into his office.")
													print("")
													print("In the end, the security guards report that Thomas was indeed in his cell. It’s just that the guy with the beard was not Thomas.")
													print("Thomas and Jack the Ripper had been covering for each other, both playing doubles so that one could stay in prison while the other could escape and kill to their hearts’ content in the real world, with an alibi secured.")
													print("The authorities thank you for helping them catch the Ripper.")
													print("GAME OVER.")
													done = True
											if ronan == "b":
												print("You are going to walk, but you realize the weather is too cold. You have no mode of transportation. You decide to wait until tomorrow.")
												q = input("Press (a) to continue, press (o) to view options")
												if q == "o":
													continue
												if q == "a":
													print("You go to visit Thomas alone.\nWhen you arrive at Thomas’s office, you find that the man with the beard is there. Except this time, he has a mustache instead. \n")
													if "knife" in inventory:
														print("You pull out the knife that you bought earlier.")
														print("“I used to be a surgeon,” you tell him. “I know my way around internal organs too, Jack.”")
														print("Thomas freezes. \nYou wave the knife closer. You caught him unaware, he has no way to defend himself except for his bare hands. \nHe says carefully, cautiously: “I’m not Jack the Ripper. But I know who he is.”")
														carpal = input("Do you believe him? (y or n) ")
														if carpal == "y":
															print("“Take me to him,” you say. \nThomas explains the situation on the way: \nThomas was supposed to be in prison. \n“For what?” you ask.\nHe was a serial killer. His method of choice: poisoning people’s pills as a doctor. \nThomas and Jack the Ripper had been covering for each other, both playing doubles so that one could stay in prison while the other could escape and kill to their hearts’ content in the real world, with an alibi secured.\n“I’m covering for you, right now,” Thomas says. “Let me go. I’ll change my identity. Get a haircut. Convince them the man in the cell is the Ripper and me. Let me go free.”")
															tunnel = input("Do you want to let him go free? (y or n) ")
															if tunnel == "y":
																print("You nod. Fair’s fair. \nWhen you arrive at the cell, you see a man who looks eerily similar to Thomas. Except where Thomas had a mustache, the man had a beard. \nIt suddenly made sense why the voices in the two phone calls had sounded so different. \nYou keep your word and tell the authorities that you have found Jack the Ripper. \nThomas goes free. \nThe authorities thank you greatly. \nYou should feel happy, but it doesn’t feel like you just imprisoned a murderer for good. \nIt feels like you just set another murderer free. \nGAME OVER")
																done = True
															if tunnel == "n":
																print("You nod, a bluff. It’s only fair to turn in Thomas as well. \nWhen you arrive at the cell, you see a man who looks eerily similar to Thomas. Except where Thomas had a mustache, the man had a beard. \nIt suddenly made sense why the voices in the two phone calls had sounded so different. \nYou go to alert the authorities when Thomas isn’t looking, whisper that you have two murderers with you.\nWhen the authorities come, Thomas realizes what you have done. \nHe lunges at you, pins your hands against the wall, hurriedly reaches for the knife and makes one clean stab into your heart. \n \nYou’ve caught the murderers, but you died in the process. \n \n\nGAME OVER")
																done = True
														if carpal == "n":
															print("You pin the knife against his neck. Like hell you would believe him. \nHe struggles as you contact the authorities.\nWhen they come, they arrest him. He is sentenced to death and hanged for his crimes. \nA month later, you receive another letter, with the same handwriting as the doctor’s note, as the last letter. \nThere’s blood stains on it. \nAll it says is this:\nYou killed the wrong man\n-Saucy Jack \nGAME OVER")
										if adam == "b":
											print("A few days later, another Ripper letter is sent out. Left on the doorstep of the police’s station. It's a different handwriting than the other Ripper letters: it doesn't match the dear Boss letter, or your letter. \nIt reads:\n  Dear mr. Satan,	\n  I am  having so fun! My toes tingle down everytime I do I job, but the best part boss is, the idiots playing hide n seek with me! \n    They think they are on something but I dont think they will ever win this game. \n    Its their fault, they shouldntve gave me so much time to hide!\n    Sincerely\n Ripper, Jack\n \nThe letter came in a box with severed toes painted bright red. You don’t want to think about whether those toes were Mary’s.\nNo, instead, you think about how the handwriting in the dear mr. Satan matches perfectly with your doctor’s note. ")
											checkpoints.append("checkpoint 1")
											ronan = input("\n \nWOULD YOU LIKE TO \na) alert authorities \nb) stay solo")
											if ronan == "a":
												print("")
												print("The police came and saw that you had a letter in the Ripper's handwriting. Because you didn't tell them about it, they think it is yours. They arrest you")
												print("GAME OVER")
												done = True
											if ronan == "b":
												print("")
												print("You are going to walk, but you realize the weather is too cold. You have no mode of transportation. You decide to wait until tomorrow.")
												q = input("\n \nPress (a) to continue, press (o) to view options")
												if q == "o":
													continue
												if q == "a":
													print("")
													print("You go to visit Thomas alone.\nWhen you arrive at Thomas’s office, you find that the man with the beard is there. Except this time, he has a mustache instead. In fact, when you look closer... this man is a different man than the Thomas who wrote you your doctor's note. \n“How can I help you?” he asks. \nThis Thomas doesn't recognnize you.")
													if "knife" in inventory:
														print("")
														print("You pull out the knife that you bought earlier.")
														print("“I used to be a surgeon,” you tell him. “I know my way around internal organs too, Jack.”")
														print("Thomas freezes. \nYou wave the knife closer. You caught him unaware, he has no way to defend himself except for his bare hands. \nHe says carefully, cautiously: “I’m not Jack the Ripper. But I know who he is.”")
														carpal = input("\n \nDo you believe him? (y or n) ")
														if carpal == "y":
															print("")
															print("“Take me to him,” you say. \nThomas explains the situation on the way: \nThomas was supposed to be in prison. \n“For what?” you ask.\nHe was a serial killer. His method of choice: poisoning people’s pills as a doctor. \nThomas and Jack the Ripper had been covering for each other, both playing doubles so that one could stay in prison while the other could escape and kill to their hearts’ content in the real world, with an alibi secured.\n“I’m helping you, right now,” Thomas says. “Let me go. I’ll change my identity. Get a haircut. Convince them the man in the cell is the Ripper and the evil murderer doctor. Let me go free.”")
															tunnel = input("\n \nDo you want to let him go free? (y or n) ")
															if tunnel == "y":
																print("")
																print("You nod. Fair’s fair. \nWhen you arrive at the cell, you see a man who looks eerily similar to Thomas. Except where Thomas had a mustache, the man had a beard. \nIt suddenly made sense why the voices in the two phone calls had sounded so different. \nYou keep your word and tell the authorities that  you have found Jack the Ripper, and that he and the doctor murderer are the same person. \nThomas goes free. \nThe authorities thank you greatly. \nYou should feel happy, but it doesn’t feel like you just imprisoned a murderer for good. \nIt feels like you just set another murderer free. \nGAME OVER")
																done = True
															if tunnel == "n":
																print("")
																print("You nod, a bluff. It’s only fair to turn in Thomas as well. \nWhen you arrive at the cell, you see a man who looks eerily similar to Thomas. Except where Thomas had a musatche, the man had a beard. \nIt suddenly made sense why the voices in the two phone calls had sounded so different. \nYou go to alert the authorities when Thomas isn’t looking, whisper that you have two murderers with you.\nWhen the authorities come, Thomas realizes what you have done. \nHe lunges at you, pins your hands against the wall, hurriedly reaches for the knife and makes one clean stab into your heart. \n \nYou’ve caught the murderers, but you died in the process. \n \n\nGAME OVER")
																done = True
														if carpal == "n":
															print("")
															print("You pin the knife against his neck. Like hell you would believe him. \nHe struggles as you contact the authorities.\nWhen they come, they arrest him. He is sentenced to death and hanged for his crimes. \n \nA month later, you receive another letter, with the same handwriting as the doctor’s note, as the dear mr. Satan letter. \nThere’s blood stains on it. \nAll it says is this:\nYou killed the wrong man\n-Saucy Jack \nGAME OVER")
															done = True

								if pedo == "n":
									print("")
									print("You find Thomas in his office. You hope that he doesn’t recognize you as the person who called him on the phone.")
									print("He is a regular looking man with a beard and brown hair.")
									print("“Hello,” you say. “I’m terribly ill, and this was the closest doctor’s office to my work. Could you very quickly write a sick note for me? I feel horrendous.”")
									print("Thomas looks at you up and down. His eyes are cunning, manipulative.")
									print("“What are you sick with?” he asks, bored.")
									print("“Polio?”")
									print("He gives you a look, but writes it down anyways.")
									print("“And what’s your name?”")
									print("You lie.")
									print("“Thank you,” you say, when he gives you the note.")
									inventory.append("doctor's note")
									print("\n \nDOCTORS NOTE HAS BEEN ADDED TO YOUR INVENTORY. \n \nWhen you get back to look at it, you are disappointed to find that the handwriting is vastly different from that of the letter's.")
									hm = input("\n \nWOULD YOU LIKE TO CONTINUE THE INVESTIGATION? (y or n) ")
									if hm == "n":
										continue
									elif hm == "y":
										lel = input("\n \nWOULD YOU LIKE TO a) discard the letter \nb) keep the letter?")
										if lel == "a":
											inventory.remove("letter")
											print("")
											print("A few days later, another Ripper letter is sent out. Left on the doorstep of the police’s station. It's a different handwriting than the other Ripper letters: it doesn't match the dear Boss letter, or your letter. \nIt reads:\n  Dear mr. Satan,	\n  I am  having so fun! My toes tingle down everytime I do I job, but the best part boss is, the idiots playing hide n seek with me! \n    They think they are on something but I dont think they will ever win this game. \n  Its their fault, they shouldntve gave me so much time to hide!\n    Sincerely\n Ripper, Jack\n \nThe letter came in a box with severed toes painted bright red. You don’t want to think about whether those toes were Mary’s.\nNo, instead, you think about how the handwriting in the dear mr. Satan letter matches perfectly with your doctor’s note. ")
											checkpoints.append("checkpoint 1")
											ronan = input("\n \nWOULD YOU LIKE TO \na) alert authorities \nb) stay solo")
											if ronan == "a":
												print("")
												print("The authorities tell you that Thomas is supposed to be in prison.")
												print("Thomas is a murderer himself. He’s incarcerated for poisoning people through the pills he prescribes them.")
												doki = input("Press (c) to continue, (o) to view options")
												if doki == "o":
													continue
												elif doki == "c":
													print("You and the authorities pay Thomas a visit together.")
													print("The security guards at Thomas’s prison are told to check his cell.")
													print("When you arrive at Thomas’s office, you find that the man with the beard is there.")
													print("“Did you get polio again?” he asks drily.")
													print("His face stops looking so bored when the police burst into his office.")
													print("")
													print("In the end, the security guards report that Thomas was indeed in his cell. It’s just that the guy with the mustache was not Thomas.")
													print("Thomas and Jack the Ripper had been covering for each other, both playing doubles so that one could stay in prison while the other could escape and kill to their hearts’ content in the real world, with an alibi secured.")
													print("The authorities thank you for helping them catch the Ripper.")
													print("GAME OVER.")
													done = True
											if ronan == "b":
												pass #this storyline will be the same as... (staying solo w/o knife to interrogate thomas w)
										if lel == "b":
											print("")
											print("A few days later, another Ripper letter is sent out. Left on the doorstep of the police’s station. It's a different handwriting than the other Ripper letters: it doesn't match the dear Boss letter, or your letter. \nIt reads:\n  Dear mr. Satan,	\n  I am  having so fun! My toes tingle down everytime I do I job, but the best part boss is, the idiots playing hide n seek with me! \n    They think they are on something but I dont think they will ever win this game. \n    Its their fault, they shouldntve gave me so much time to hide!\n  Sincerely\n Ripper, Jack\n \nThe letter came in a box with severed toes painted bright red. You don’t want to think about whether those toes were Mary’s.\nNo, instead, you think about how the handwriting in the dear mr. Satan letter matches perfectly with your doctor’s note. ")
											checkpoints.append("checkpoint 1")
											ronan = input("\n \nWOULD YOU LIKE TO \na) alert authorities \nb) stay solo")
											if ronan == "a":
												print("The police came and saw that you had a letter in the Ripper's handwriting. Because you didn't tell them about it, they think it is yours. They arrest you.")
												print("GAME OVER")
												done = True
											if ronan == "b":
												pass #...this one (staying solo w/o knife to interrogate thomas w)
							elif fbi == "b":
								print("\n \nSince the police have wrapped up, you look closer at you and Mary’s shared apartment. \nYou look closely at Mary’s desk-- there is a wedding ring. But you know what Mary’s wedding ring looks like, and that is not it. \nNo, it’s Mary’s ex husband’s wedding ring. \nJoseph Barnett. \nAnd since Joseph had long ago moved out of the apartment, there would have been no reason for him to be back… ")
								print("\n \nA WEDDING RING HAS NOW BEEN ADDED TO YOUR INVENTORY")
								inventory.append("wedding ring")
								print("")
								print("So far, everything you've learned about Thomas seems like a dead end. ")
								print("You decide to stop investigating Thomas and start investigating Joseph instead. ")
								print(" \n \nJOSEPH BARNETT HAS BEEN ADDED TO YOUR LIST OF SUSPECTS")
								god = input("Would you like to (s) start your investigation of Joseph or (o) view options?")
								if god == "o":
									continue
								elif god == "s":
									if "Joseph Barnett" in suspects:
										thing = 1
									else:
										suspects.append("Joseph Barnett")
										thing = 1
			elif call == "b":
				print("")
				print("“Do you have epilepsy?,” he asks. “I have medicines that are able to combat that tremendously.” \nYou want to investigate more, even if you don’t have epilepsy. \n“Sure,” you say.\n“Great! Meet me tomorrow at noon then, at my office on Dorset Street?”\nIf this guy only hands out medicine, surely he can’t be so dangerous, can he?\n“Yeah, ok,” you agree. \nTomorrow at noon, then.")
				hm = input("\n \nWOULD YOU LIKE TO CONTINUE THE INVESTIGATION? (y or n) ")
				if hm == "n":
					continue
				if hm == "y":
					print("")
					print("The next day, you walk into his office at noon.\nHe is a regular looking man with a mustache and brown hair. \nHe already has pills waiting for you. \n“All you need to do is sign,” Thomas says. \nYou sign, and carefully inspect the room. Nothing suspicious. Nothing unusual. \nYou look up after signing. Thomas has pushed the pills to you. \n“Take one now,” he is saying.")
					hmm = input("\n \nDO YOU TAKE THE PILLS? (y or n) ")
					if hmm == "y":
						print("You take the pills. Only too late you realize that they are laced with poison. \nThomas was not Jack the Ripper, but he was a serial killer in his own right. ")
						print("GAME OVER")
						done = True
					if hmm == "n":
						print("")
						print("“No, thank you.”\n“Take one now,” he insists, harder. ")
						hmmm = input("\n \nDO YOU TAKE THE PILLS? (y or n) ")
						if hmmm == "y":
							print("\n \nYou take the pills. Only too late you realize that they are laced with poison. \nThomas was not Jack the Ripper, but he was a serial killer in his own right. ")
							print("GAME OVER")
							done = True
						if hmmm == "n":
							print("\n \n“No, really, I’m good-” \n“Take. One. Now.” He is looking at you menacingly, like if you don’t take the pills, he will force you to. \nYou take the pills.\nThey are laced with poison. \nThomas was not Jack the Ripper, but he was a serial killer in his own right. \nGAME OVER. ")
							done = True
		if choice == "b":
			continue
	#joseph
	if thing == 1 and "wedding ring" in inventory:
		print("---------------------------------------------------------------------------------------------")
		print("YOU HAVE STARTED YOUR INVESTIGATION ON JOSEPH BARNETT")
		print("")
		print("You remember the days when Mary still lived with Joseph. \nScreaming, fighting. \nTheir biggest problem was with Mary’s occupation. \nMary had an…. unconventional job. She was an escort, to put it politely. \nJoseph hated it-- hated the business, hated the people. But after Joseph lost his job, she resorted back to her job for the money. \nIt all ended in Joseph bitterly packing up his things and leaving. ")
		hm = input(" \n \nPress (c) to continue, (o) to view options ")
		if hm == "o":
			continue
		if hm == "c":
			elsa = input("WOULD YOU LIKE TO ALERT THE AUTHORITIES ABOUT THE WEDDING RING? (y or n)")
			if elsa == "y":
				print("The police came and saw that you had a letter in the Ripper's handwriting. Because you didn't tell them about it, they think it is yours. They arrest you")
				print("GAME OVER")
				done = True
			if elsa == "n":
				print("\n \nYou stay solo and decide to visit Joseph’s current girlfriend, Carmen. \nHe moved on fast after Mary. \n“He’s trying to spite me,” Mary would complain to you. “It’s all because he lost his job, that absolute bag of di-”")
				print("You hurry to Carmen’s flat. The two have only  been dating for a month, so she lives alone. \nWhen you knock at the door, you see Carmen for the first time. \nShe’s a beautiful Romani woman; cherry lips, cartoon eyes. \n“Can I come in?”")
				hm = input(" \n \nPress (c) to continue, (o) to view options ")
				if hm == "o":
					continue
				elif hm == "c":
					print("\n \n“I’m sorry for your loss,” Carmen says, handing you tea.")
					print("“Thank you,” you say. The tea is lukewarm. You drink it anyways, trying to be polite.")
					j = input("\n \nPress (c) to continue, (o) to view options.")
					if j == "o":
						continue
					elif j == "c":
						print("\n \n“Right,” she says. “What are you here for?” \n“I was actually here to talk about Joseph.” \nCarmen sits down, gives a grimace. “Ugh, Joseph. We’re currently in a fight. He can really be the worst sometimes, don’t you think?”")
						print("“Mary would say that too,” you say. “What do you know about his relationship with Mary?” \nCarmen shrugs, looks down at her tea. “Nothing you probably don’t already know.” \n“They divorced because of Mary’s job. That’s what I know.” \n“Really?” Carmen asks. “Do you know about the--” She stops. Takes a sip of her awful lukewarm tea.")
						o = input("\n \nPress (c) to continue, (o) to view options.")
						if o == "o":
							continue
						elif o == "c":
							print("\n \n“What?” you press. \n“Joseph… well… Mary’s prostitution wasn’t the only reason they didn’t work out.” \nThis is new information to you. You are a bit hurt- why did Mary not tell you this?")
							print("“What was the other reason?” \n“Joseph didn’t want children,” Carmen says. “Hated them, hated the idea of having them. God, he’d rather die.” \n“And?” \nCarmen looks surprised you don’t know. \n“And Mary wanted them. She didn’t tell you?” \n“No,” you say. ")
							hm = input(" \n \nPress (c) to continue, (o) to view options ")
							if hm == "o":
								continue
							elif hm == "c":
								print("\n \n“Where is the bathroom?” you ask. \n“Down the hallway, third door to the left.” \n“Thank you.” ")
								gasp = input("\n \nWOULD YOU LIKE TO a) GO TO THE BATHROOM or b) LOOK IN CARMEN'S ROOM?")
								if gasp == "a":
									print("You find the bathroom easily. You wash your hands at the sink, but your eyes catch on something silver. \nA wedding ring, at the edge of the counter. \nNot Joseph’s-- Mary’s. \nWhy does Carmen have Mary’s wedding ring in her bathroom?")
									print("\n \nMARY’S WEDDING RING HAS BEEN ADDED TO YOUR INVENTORY")
									inventory.append("mary's wedding ring")
									print("\n \nCARMEN DILAURENTIS HAS BEEN ADDED TO YOUR LIST OF SUSPECTS")
									suspects.append("Carmen DiLaurentis")
									print("You start to investigate Carmen.")
									thing = 4
								elif gasp == "b":
									print("\n \nYou don’t actually go to the bathroom. You take the opportunity to look around the flat. \nYou go into Carmen’s room. \nIt’s nice. Simple, decorated nicely.")
									print("Your eyes catch on a familiar looking book on Carmen’s desk. \nYou go to pick it up. Open the pages. \nIt’s Mary’s diary. \nWhy does Carmen have Mary’s diary in her bedroom?")
									print("\n \nMARY’S DIARY HAS BEEN ADDED TO YOUR INVENTORY")
									inventory.append("mary's diary")
									print("\n \nCARMEN DILAURENTIS HAS BEEN ADDED TO YOUR LIST OF SUSPECTS")
									suspects.append("Carmen DiLaurentis")
									anna = input("\n \nWOULD YOU LIKE TO (A) INVESTIGATE CARMEN OR (B) CONTINUE INVESTIGATING JOSEPH?")
									if anna == "a":
										print("You start to investigate Carmen.")
										thing = 4
									if anna == "b":
										print("\n \nYou hide the diary in your bag. Carmen gives you some more tea before you leave: “For times when the grief becomes too hard,” she says. \nOkay, Carmen. ")
										kristoff = input("\n \nPress (c) to continue, (o) to view options.")
										if kristoff == "o":
											continue
										elif kristoff == "c":
											print("\n \nWhen you get home, you read the diary’s contents. \n \nSeptember 14, 1888 \nThings have been rocky between Joseph and I. \nI’ll be honest - \nI’m scared. I think that he’s capable of doing… things…")
											olaf = input("\n \nPress (c) to continue, (o) to view options.")
											if olaf == "o":
												continue
											elif olaf == "c":
												print("\n \nOctober 1, 1888 \nI’m pregnant. \nIt’s Joseph’s. \nHe wasn’t happy when I told him. ")
												onepercent = input("\n \nPress (c) to continue, (o) to view options.")
												if onepercent == "o":
													continue
												elif onepercent == "c":
													print("\n \nOctober 20, 1888 \nJoseph has lost his job. I don’t know what to do. \nI want to go back. We need the money. \nI need the money. This baby…")
													car = input("\n \nPress (c) to continue, (o) to view options.")
													if car == "o":
														continue
													elif car == "c":
														print("\n \nOctober 21, 1888\nHe says that he hates people like me. Women like me. \nHe says that if he could, he would kill all of us and then some. \nMaybe he was bluffing, to scare me off. \nMaybe --\nHe’s here, I have to go, I have t\n \nThe last entry is left off in a smear. \nThe evidence is enough to be incriminating. ")
														pal = input("\n \nPress (c) to continue, (o) to view options.")
														if pal == "o":
															continue
														elif pal == "c":
															print("\n \nCould Joseph have killed those prostitutes to scare Mary off the streets? ")
															d = input("\n \nPress (c) to continue, (o) to view options.")
															if d == "o":
																continue
															elif d == "c":
																print("\n \nYou decide to visit Mary’s flat/your old apartment. \nIt looks the same. When you walk in, you greet George, your old neighbor. \n“You have an admirer,” he says, laughing. \n“What?” you say. \n“Check your doorstep.”\nYou go up to the second floor. You see a pile of letters before your door. ")
																kill = input("\n \nPress (c) to continue, (o) to view options.")
																if kill == "o":
																	continue
																elif kill == "c":
																	print("\n \nSEVERAL LETTERS HAVE NOW BEEN ADDED TO YOUR INVENTORY")
																	inventory.append("several letters")
																	purple = input("\n \nWOULD YOU LIKE TO ALERT THE AUTHORITIES? (y or n)")
																	if purple == "y":
																		print("")
																		print("The police came and saw that you had a letter in the Ripper's handwriting. Because you didn't tell them about it, they think it is yours. They arrest you")
																		print("GAME OVER")
																		done = True
																	elif purple == "n":
																		print("")
																		print("When you go home to read them, you realize who they are from. They are in the same pen as the dear mr. Satan letter, but different than your letter.")
																		a = input("\n \nPress (c) to continue, (o) to view options.")
																		if a == "o":
																			continue
																		elif a == "c":
																			print("")
																			print("	1- \n	Seeker - \n	I am still hiding. Whered you go?")
																			b = input("\n \nPress (c) to continue, (o) to view options.")
																			if b == "o":
																				continue
																			elif b == "c":
																				print("")
																				print("	2 - \n	Hello seeker!\n	I miss you, dont tell me i scared you off!!! ")
																				c = input("\n \nPress (c) to continue, (o) to view options.")
																				if c == "o":
																					continue
																				elif c == "c":
																					print("")
																					print("	3 - \n	Seeker,\n	I hear youve moved. \n	Fine,\n	If you dont want to find me,\n	Ill find u. ")
																					d = input("\n \nPress (c) to continue, (o) to view options.")
																					if d == "o":
																						continue
																					elif d == "c":
																						print("")
																						print("	4 - \n	Please move back in. I miss you.")
																						e = input("\n \nPress (c) to continue, (o) to view options.")
																						if e == "o":
																							continue
																						elif e == "c":
																							print("")
																							print("	5 - \n	George is awful nice, isnt he?")
																							f = input("\n \nPress (c) to continue, (o) to view options.")
																							if f == "o":
																								continue
																							elif f == "c":
																								print("\n \nYou are worried that the Ripper will kill George if you don’t do something. \nClearly, he is entertained by you. He wants you to be the cat, and he wants to be the mouse. ")
																								g = input("\n \nDO YOU WANT TO \na) HIDE OUT NEAR YOUR APARTMENT IN CASE HE COMES BACK TO PUT ANOTHER LETTER \nb)STICK NEAR GEORGE IN CASE HE ATTACKS GEORGE")
																								if g == "a":
																									print("\n \nYou hide for a couple of days in a neighbor’s room. \nFinally, you see someone come to place another letter. \nIt’s a man, a doctor.")
																									h = input("\n \nPress (c) to continue, (o) to view options")
																									if h == "o":
																										continue
																									elif h == "c":
																										print("\n \nYou inch closer to the peephole, try to make out what his nametag says:\nTHOMAS NIELL CREAM. \nYou gasp, audibly. \nThomas turns around instantly. \nHe comes to the door, puts his face right up to the peephole. ")
																										i = input("\n \nDO YOU ALERT THE AUTHORITIES THAT YOU THINK THOMAS IS THE RIPPER? (y or n)")
																										if i == "y":
																											print("")
																											print("The police came and saw that you had a letter in the Ripper's handwriting. Because you didn't tell them about it, they think it is yours. They arrest you.")
																											print("GAME OVER")
																										elif i == "n":
																											print("")
																											print("You waited too long. He forcibly knocks on the door. \n“Hello? Who’s there? Let me in!”\nYou don’t budge. You try to look around the apartment, but there is no escape.")
																											print("“Hello?! I’ll break this door down!” he says. \nYou panic. He will kill you if you let him in. You are a witness. \n“Whoever’s on the other side of that door, let me in, or I swear, I’ll--”\nHe breaks in.")
																											print("You were killed by Thomas!\nGAME OVER. ")
																											done = True
																								if g == "b":
																									print("\n \nYou buy a knife. You stick near George. You are his protector. \n“If something happens,” you tell him, “I’ll be there. I’m a surgeon too. I know how cut if I need to.” \nHe seems grateful. ")
																									george = input("\n \nPress (c) to continue, (o) to view options.")
																									if george == "o":
																										continue
																									elif george == "c":
																										print("\n \nYou are in George’s flat when there is a knock on the door. \n“Hello?” a man says. “Can I come in?”\nGeorge glances at you. You hold up the knife, and nod.")
																										print("George opens the door. There is a man with a beard. \nHe is holding a knife. \n“Stay silent,” he says, and closes the door. You hide behind furniture, trying to sneak up on him. If you do not hurry, then George… well…")
																										print("You tell yourself not to think about it. \nYou get the courage to lunge up at the man and stab him in the back. \nHe freezes. Before he collapses, he pulls George to him and stabs George in the heart. ")
																										gah = input("\n \nDO YOU WANT TO (a) ALERT THE AUTHORITIES OR (b) RUN?")
																										if gah == "a":
																											print("\n \nThe authorities come. No matter what you say, they will not believe you. They see that you have a letter in the Ripper’s handwriting that you didn’t tell them about. Since the letter not addressed to you, they believe that you were the Ripper and had written another letter to give to the police. \nIt looks like you killed 2 men. \nYou are arrested. \nThe Ripper has successfully framed you. \nGAME OVER. ")
																											done = True
																										elif gah == "b":
																											print("\n \nYou run. You’ve successfully killed the Ripper, but you have no clue who he is. \nGAME OVER")
																											done = True
	else:
		print("---------------------------------------------------------------------------------------------")
		print("YOU HAVE STARTED YOUR INVESTIGATION ON JOSEPH BARNETT")
		print("")
		print("You decide to inspect Mary’s room/the crime scene. \nSince the police have wrapped up, you look closer at you and Mary’s shared apartment. \nYou look closely at Mary’s desk-- there is a wedding ring. But you know what Mary’s wedding ring looks like, and that is not it. \nNo, it’s Mary’s ex husband’s wedding ring. \nJoseph Barnett.\nAnd since Joseph had long ago moved out of the apartment, there would have been no reason for him to be back…")
		print("\n \nA WEDDING RING HAS BEEN ADDED TO YOUR INVENTORY")
		inventory.append("wedding ring")
		gary = input("\n \nWOULD YOU LIKE TO ALERT THE AUTHORITIES? (y or n)")
		if gary == "n":
			print("\n \nYou stay solo and decide to visit Joseph’s current girlfriend, Carmen. \nHe moved on fast after Mary. \n“He’s trying to spite me,” Mary would complain to you. “It’s all because he lost his job, that absolute bag of di-” \nYou hurry to Carmen’s flat. The two have only  been dating for a month, so she lives alone. \nWhen you knock at the door, you see Carmen for the first time. \nShe’s a beautiful Romani woman; cherry lips, cartoon eyes. \n“Can I come in?”")
			jesus = input("\n \nPress (c) to continue, (o) to view options.")
			if jesus == "o":
				continue
			elif jesus == "c":
				print("\n \n“I’m sorry for your loss,” Carmen says, handing you tea.")
				print("“Thank you,” you say. The tea is lukewarm. You drink it anyways, trying to be polite.")
				j = input("\n \nPress (c) to continue, (o) to view options.")
				if j == "o":
					continue
				elif j == "c":
					print("\n \n“Right,” she says. “What are you here for?” \n“I was actually here to talk about Joseph.” \nCarmen sits down, gives a grimace. “Ugh, Joseph. We’re currently in a fight. He can really be the worst sometimes, don’t you think?”")
					print("“Mary would say that too,” you say. “What do you know about his relationship with Mary?” \nCarmen shrugs, looks down at her tea. “Nothing you probably don’t already know.” \n“They divorced because of Mary’s job. That’s what I know.” \n“Really?” Carmen asks. “Do you know about the--” She stops. Takes a sip of her awful lukewarm tea.")
					u = input("\n \nPress (c) to continue, (o) to view options.")
					if u == "o":
						continue
					elif u == "c":
						print("\n \n“What?” you press. \n“Joseph… well… Mary’s prostitution wasn’t the only reason they didn’t work out.” \nThis is new information to you. You are a bit hurt- why did Mary not tell you this?")
						print("“What was the other reason?” \n“Joseph didn’t want children,” Carmen says. “Hated them, hated the idea of having them. God, he’d rather die.” \n“And?” \nCarmen looks surprised you don’t know. \n“And Mary wanted them. She didn’t tell you?” \n“No,” you say. ")
						christ = input("\n \nPress (c) to continue, (o) to view options.")
						if christ == "o":
							continue
						elif christ == "c":
							print("\n \n“Where is the bathroom?” you ask. \n“Down the hallway, third door to the left.” \n“Thank you.” ")
							gasp = input("\n \nWOULD YOU LIKE TO a) GO TO THE BATHROOM or b) LOOK IN CARMEN'S ROOM?")
							if gasp == "a":
								print("\n \nYou find the bathroom easily. You wash your hands at the sink, but your eyes catch on something silver. \nA wedding ring, at the edge of the counter. \nNot Joseph’s-- Mary’s. \nWhy does Carmen have Mary’s wedding ring in her bathroom?")
								print("\n \nMARY’S WEDDING RING HAS BEEN ADDED TO YOUR INVENTORY")
								inventory.append("mary's wedding ring")
								print("\n \nCARMEN DILAURENTIS HAS BEEN ADDED TO YOUR LIST OF SUSPECTS")
								suspects.append("Carmen DiLaurentis")
								print("You start to investigate Carmen.")
								thing = 4
							elif gasp == "b":
								print("\n \nYou don’t actually go to the bathroom. You take the opportunity to look around the flat. \nYou go into Carmen’s room. \nIt’s nice. Simple, decorated nicely.")
								print("Your eyes catch on a familiar looking book on Carmen’s desk. \nYou go to pick it up. Open the pages. \nIt’s Mary’s diary. \nWhy does Carmen have Mary’s diary in her bedroom?")
								print("\n \nMARY’S DIARY HAS BEEN ADDED TO YOUR INVENTORY")
								inventory.append("mary's diary")
								print("\n \nCARMEN DILAURENTIS HAS BEEN ADDED TO YOUR LIST OF SUSPECTS")
								suspects.append("Carmen DiLaurentis")
								anna = input("WOULD YOU LIKE TO (A) INVESTIGATE CARMEN OR (B) CONTINUE INVESTIGATING JOSEPH?")
								if anna == "a":
									print("\n \nYou start to investigate Carmen.")
									thing = 4
								if anna == "b":
									print("\n \nYou hide the diary in your bag. Carmen gives you some more tea before you leave: “For times when the grief becomes too hard,” she says. \nOkay, Carmen. ")
									kristoff = input("\n \nPress (c) to continue, (o) to view options.")
									if kristoff == "o":
										continue
									elif kristoff == "c":
										print("\n \nWhen you get home, you read the diary’s contents. \n \nSeptember 14, 1888 \nThings have been rocky between Joseph and I. \nI’ll be honest - \nI’m scared. I think that he’s capable of doing… things…")
										olaf = input("\n \nPress (c) to continue, (o) to view options.")
										if olaf == "o":
											continue
										elif olaf == "c":
											print("\n \nOctober 1, 1888 \nI’m pregnant. \nIt’s Joseph’s. \nHe wasn’t happy when I told him. ")
											onepercent = input("\n \nPress (c) to continue, (o) to view options.")
											if onepercent == "o":
												continue
											elif onepercent == "c":
												print("\n \nOctober 20, 1888 \nJoseph has lost his job. I don’t know what to do. \nI want to go back to work. We need the money. \nI need the money. This baby…")
												car = input("\n \nPress (c) to continue, (o) to view options.")
												if car == "o":
													continue
												elif car == "c":
													print("\n \nOctober 21, 1888\nHe says that he hates people like me. Women like me. \nHe says that if he could, he would kill all of us and then some. \nMaybe he was bluffing, to scare me off. \nMaybe --\nHe’s here, I have to go, I have t\n \nThe last entry is left off in a smear. \nThe evidence is enough to be incriminating. ")
													pal = input("\n \nPress (c) to continue, (o) to view options.")
													if pal == "o":
														continue
													elif pal == "c":
														print("\n \nA few days later, another Ripper letter is sent out. Left on the doorstep of the police’s station.\nIt reads:\n	Dear mr. Satan,\n	I am  having so fun! My toes tingle down everytime I do I job, but the best part boss is, the idiots playing hide n seek with me! \n    They think they are on something but I dont think they will ever win this game.\n	Its their fault, they shouldntve gave me so much time to hide!\n	Sincerely\n	Ripper, Jack\n \nThe letter came in a box with severed toes painted bright red. You don’t want to think about whether those toes were Mary’s.")
														print("")
														ok = input("\n \nPress (c) to continue, (o) to view options.")
														if ok == "o":
															continue
														elif ok == "c":
															print("\n \nYou are perplexed. None of the canonical Ripper letters match up. \nThe dear mr. Satan letter has to be Jack, since it came with the toes, but it doesn’t match the handwriting of your letter or of the dear boss letter. \nAs if two or more people were Jack the Ripper. \nAs if it were a group effort. ")
															d = input("\n \nPress (c) to continue, (o) to view options.")
															if d == "o":
																continue
															elif d == "c":
																print("\n \n	You decide to visit Mary’s flat/your old apartment. \nIt looks the same. When you walk in, you greet George, your old neighbor. \n“You have an admirer,” he says, laughing. \n“What?” you say. \n“Check your doorstep.”\nYou go up to the second floor. You see a pile of letters before your door. ")
																kill = input("\n \nPress (c) to continue, (o) to view options.")
																if kill == "o":
																	continue
																elif kill == "c":
																	print("\n \nSEVERAL LETTERS HAVE NOW BEEN ADDED TO YOUR INVENTORY")
																	inventory.append("several letters")
																	purple = input("\n \nWOULD YOU LIKE TO ALERT THE AUTHORITIES? (y or n)")
																	if purple == "y":
																		print("")
																		print("The police came and saw that you had a letter in the Ripper's handwriting. Because you didn't tell them about it, they think it is yours. They arrest you")
																		print("GAME OVER")
																		done = True
																	elif purple == "n":
																		print("")
																		print("When you go home to read them, you realize who they are from. They are in the same pen as the dear mr. Satan letter, but different than your letter.")
																		a = input("\n \nPress (c) to continue, (o) to view options.")
																		if a == "o":
																			continue
																		elif a == "c":
																			print("")
																			print("	1- \n	Seeker - \n	I am still hiding. Whered you go?")
																			b = input("\n \nPress (c) to continue, (o) to view options.")
																			if b == "o":
																				continue
																			elif b == "c":
																				print("")
																				print("	2 - \n	Hello seeker!\n	I miss you, dont tell me i scared you off!!! ")
																				c = input("\n \nPress (c) to continue, (o) to view options.")
																				if c == "o":
																					continue
																				elif c == "c":
																					print("")
																					print("	3 - \n	Seeker,\n	I hear youve moved. \n	Fine,\n	If you dont want to find me,\n	Ill find u. ")
																					d = input("\n \nPress (c) to continue, (o) to view options.")
																					if d == "o":
																						continue
																					elif d == "c":
																						print("")
																						print("	4 - \n	Please move back in. I miss you.")
																						e = input("\n \nPress (c) to continue, (o) to view options.")
																						if e == "o":
																							continue
																						elif e == "c":
																							print("")
																							print("	5 - \n	George is awful nice, isnt he?")
																							f = input("\n \nPress (c) to continue, (o) to view options.")
																							if f == "o":
																								continue
																							elif f == "c":
																								print("You are worried that the Ripper will kill George if you don’t do something. \nClearly, he is entertained by you. He wants you to be the cat, and he wants to be the mouse. ")
																								g = input("DO YOU WANT TO \na) HIDE OUT NEAR YOUR APARTMENT IN CASE HE COMES BACK TO PUT ANOTHER LETTER \nb)STICK NEAR GEORGE IN CASE HE ATTACKS GEORGE")
																								if g == "a":
																									print("\n \nYou hide for a couple of days in a neighbor’s room. \nFinally, you see someone come to place another letter. \nIt’s a man, a doctor.")
																									h = input("\n \nPress (c) to continue, (o) to view options")
																									if h == "o":
																										continue
																									elif h == "c":
																										print("\n \nYou inch closer to the peephole, try to make out what his nametag says:\nTHOMAS NIELL CREAM. \nYou gasp, audibly. \nThomas turns around instantly. \nHe comes to the door, puts his face right up to the peephole. ")
																										i = input("DO YOU ALERT THE AUTHORITIES THAT YOU THINK THOMAS IS THE RIPPER? (y or n)")
																										if i == "y":
																											print("")
																											print("The police came and saw that you had a letter in the Ripper's handwriting. Because you didn't tell them about it, they think it is yours. They arrest you")
																											print("GAME OVER")
																										elif i == "n":
																											print("")
																											print("You waited too long. He forcibly knocks on the door. \n“Hello? Who’s there? Let me in!”\nYou don’t budge. You try to look around the apartment, but there is no escape.")
																											print("“Hello?! I’ll break this door down!” he says. \nYou panic. He will kill you if you let him in. You are a witness. \n“Whoever’s on the other side of that door, let me in, or I swear, I’ll--”\nHe breaks in.")
																											print("You were killed by Thomas!\nGAME OVER. ")
																											done = True
																								if g == "b":
																									print("\n \nYou buy a knife. You stick near George. You are his protector. \n“If something happens,” you tell him, “I’ll be there. I’m a surgeon too. I know how cut if I need to.” \nHe seems grateful. ")
																									george = input("\n \nPress (c) to continue, (o) to view options.")
																									if george == "o":
																										continue
																									elif george == "c":
																										print("\n \nYou are in George’s flat when there is a knock on the door. \n“Hello?” a man says. “Can I come in?”\nGeorge glances at you. You hold up the knife, and nod.")
																										print("George opens the door. There is a man with a beard. \nHe is holding a knife. \n“Stay silent,” he says, and closes the door. You hide behind furniture, trying to sneak up on him. If you do not hurry, then George… well…")
																										print("You tell yourself not to think about it. \nYou get the courage to lunge up at the man and stab him in the back. \nHe freezes. Before he collapses, he pulls George to him and stabs George in the heart. ")
																										gah = input("\n \nDO YOU WANT TO (a) ALERT THE AUTHORITIES OR (b) RUN?")
																										if gah == "a":
																											print("\n \nThe authorities come. No matter what you say, they will not believe you. They see that you have a letter in the Ripper’s handwriting that you didn’t tell them about. Since the letter not addressed to you, they believe that you were the Ripper and had written another letter to give to the police. \nIt looks like you killed 2 men. \nYou are arrested. \nThe Ripper has successfully framed you. \nGAME OVER. ")
																											done = True
																										elif gah == "b":
																											print("\n \nYou run. You’ve successfully killed the Ripper, but you have no clue who he is. \nGAME OVER")
																											done = True

		if gary == "y":
			print("\n \nThe authorities already have Joseph as a suspect, but now with the wedding ring, they are keeping a closer look on him. \nThey note your personal connection to Joseph and your affinity for investigating, and ask you if you would like to try to get closer to Joseph and maybe get him to admit something. ")
			print("\n \nThe authorities take the wedding ring.")
			print("\n \nWEDDING RING HAS BEEN REMOVED FROM YOUR INVENTORY")
			inventory.remove("wedding ring")
			brett = input("\n \nWOULD YOU LIKE TO BE A SPY FOR THE AUTHORITIES? (y or n) ")
			if brett == "y":
				print("\n \nYou are now a spy for the authorities, tasked with getting information out of Joseph. \nA police officer named Murrey is watching this operation. You are to give him weekly updates on what you find.")
				pedophile = input("\n \nPress (c) to continue, (o) to view options.")
				if pedophile == "o":
					continue
				elif pedophile == "c":
					print("\n \nYou give Joseph a call. \n“Hello?”\n“Hi, Joseph!” you say, trying to sound friendly. \n“Oh, hello,” he says. “I heard about what happened to Mary. It’s devastating.” \nYou note that he doesn’t sound all too remorseful, like he’s feigning sincerity.")
					christmas = input("\n \nPress (c) to continue, (o) to view options.")
					if christmas == "o":
						continue
					elif christmas == "c":
						print("\n \n“Yes, yes,” you say, “it’s been very hard. Listen, I thought that maybe we should meet up. We were closest to Mary, after all.” \nHe is silent for a few seconds. \nThen, finally: “Sure. I happen to be in town anyway.”\nYou find that interesting. He happens to be in town around the time that Mary is killed. ")
						easter = input("\n \nPress (c) to continue, (o) to view options.")
						if easter == "o":
							continue
						elif easter == "c":
							print("\n \n“Tomorrow, at noon?” you suggest. “At the bar on Dorset?”\n“Sounds good.” \nHe hangs up. \nTomorrow, at noon, then. ")
							bleacher = input("\n \nPress (c) to continue, (o) to view options.")
							if bleacher == "o":
								continue
							elif bleacher == "c":
								print("\n \nJoseph arrives at the bar and the two of you are talking, solemn about Mary’s death. \n“Do you miss her?” you ask Joseph. \n“Of course I do, why wouldn’t I?” he says. “I loved her.”\nYou find that hard to believe. \n“If you loved her, why’d you leave her?” you ask. \nJoseph scoffs. “It wasn’t a choice. I couldn’t… I couldn’t be with her if she was going to…”\nYou don’t need him to finish the sentence. ")
								you = input("\n \nPress (c) to continue, (o) to view options.")
								if you == "o":
									continue
								elif you == "c":
									print("\n \nJoseph is getting ready to leave when a girl walks in. She’s pretty. Brunette, blue eyes. Wearing a bright blue scarf. She smiles at Joseph, and Joseph gives her a nod. \n“You two know each other?” you ask.")
									print("Joseph startles. He forgot you were there.\n“Uh… yeah,” he says,  “she’s nobody.” ")
									antonoff = input("\n \nDO YOU a) TRAIL JOSEPH WHEN HE LEAVES OR b) TALK TO THE GIRL?")
									if antonoff == "a":
										print("\n \n“Thanks for meeting me here,” you say. “It was nice seeing you.”\n“Sure thing,” Joseph responds, as he walks away. You wait a couple of minutes before tailing him.")
										celeste = input("\n \nPress (c) to continue, (o) to view options.")
										if celeste == "o":
											continue
										elif celeste == "c":
											print("\n \nYou follow him and see the brunette girl catching up to him, talking to him. \nHe leads the girl into an alley, you hurry to catch up. \n“You can’t talk to me, it makes me look suspicious,” you hear Joseph saying. \nSuspicious? ")
											celeste = input("\n \nPress (c) to continue, (o) to view options.")
											if celeste == "o":
												continue
											elif celeste == "c":
												print("\n \n“Joe,” brunette says, “please, I haven’t seen you in--”\nJoseph pushes the girl against the wall, pins a hand against her neck. \nYou are surprised at how violent he is. \n“Leave me alone,” Joseph snarls. Lets her go, and walks away. ")
												celeste = input("\n \nPress (c) to continue, (o) to view options.")
												if celeste == "o":
													continue
												elif celeste == "c":
													print("\n \nYou go back to the bar, the day after.\n“Hello,” you say to the bartender. “Does a brunette usually come in here?” \nThe bartender snorts. “You’ll need to be more specific than that.”")
													celeste = input("\n \nPress (c) to continue, (o) to view options.")
													if celeste == "o":
														continue
													elif celeste == "c":
														print("\n \n“Blue eyes? Wears a bright blue scarf? About,” you demonstrate with your hand, “yeigh tall?” \n“Hm,” the bartender says, “you’re talking about Lolly.”")
														celeste = input("\n \nPress (c) to continue, (o) to view options.")
														if celeste == "o":
															continue
														elif celeste == "c":
															print("\n \n“Lolly?”\n“Dolores, goes by Lolly.”\n“Is she a regular?” you ask. \nThe bartender shrugs. “Sometimes she comes in on Thursdays.”\nThursdays, you remind yourself. ")
															celeste = input("\n \nPress (c) to continue, (o) to view options.")
															if celeste == "o":
																continue
															elif celeste == "c":
																print("\n \nNext Thursday, you’re waiting. Like clockwork, Lolly comes in at the same time you saw her last. \nShe sits down at the bar, makes an order. ")
																celeste = input("\n \nPress (c) to continue, (o) to view options.")
																if celeste == "o":
																	continue
																elif celeste == "c":
																	print("\n \n“Hey,” you say, sliding down in the chair next to her. \nShe looks over. “Hey,” she says, “I recognize you. You were with Joe the other day, weren’t you?” \n“Um, Joseph, yeah.”\n“Joseph.” She rolls her eyes. “What do you want to know?”")
																	celeste = input("\n \nPress (c) to continue, (o) to view options.")
																	if celeste == "o":
																		continue
																	elif celeste == "c":
																		print("\n \n“That transparent, huh?” you say. \n“You’re not the only one who’s asking around,” she says. “People think he’s the one who did it.”\n“Do you?” you ask.\n“Do I what?”\n“Do you think he did it?”")
																		celeste = input("\n \nPress (c) to continue, (o) to view options.")
																		if celeste == "o":
																			continue
																		elif celeste == "c":
																			print("\n \nShe looks you over. “Why should I tell you?”\nYou wonder why she is so secretive. ")
																			print("\n \nLOLLY HAS BEEN ADDED TO YOUR LIST OF SUSPECTS.")
																			suspects.append("lolly")
																			celeste = input("\n \nPress (c) to continue, (o) to view options.")
																			if celeste == "o":
																				continue
																			elif celeste == "c":
																				print("\n \n“I saw you,” you tell her. “In the alley. When he pinned you against the wall.”\nShe shrugs in indifference, but you see her eyes widen slightly. \n“What?” you press. “Is that typical?”\nLolly lets out a small laugh. “For Joe, it is.”")
																				celeste = input("\n \nPress (c) to continue, (o) to view options.")
																				if celeste == "o":
																					continue
																				elif celeste == "c":
																					print("\n \n“Joseph is… typically violent with you?”\n“Isn’t he with everyone?” Lolly asks. “I’m surprised Mary didn’t tell you.” \nYou’re surprised Mary didn’t tell you, too. ")
																					celeste = input("\n \nPress (c) to continue, (o) to view options.")
																					if celeste == "o":
																						continue
																					elif celeste == "c":
																						print("\n \n“Joseph’s  violent,” you tell Murrey, a few days later. \nMurrey is eating a donut. \n“Find more information about Joseph,” he says mid-donut bite. “Why would he kill Mary, and those other four prostitutes?”\n“Maybe he wanted to scare Mary off the streets by killing the other girls?”  you suggest.\nOfficer Murrey takes another bite of his donut.")
																						celeste = input("\n \nPress (c) to continue, (o) to view options.")
																						if celeste == "o":
																							continue
																						elif celeste == "c":
																							print("\n \n“Who do you think did it, Officer Murrey?” you ask. \nHe doesn’t answer. He is still chewing a mouthful of donut.\nYou examine his desk, and are startled to see some papers. ")
																							celeste = input("\n \nPress (c) to continue, (o) to view options.")
																							if celeste == "o":
																								continue
																							elif celeste == "c":
																								print("\n \nNot that the papers are startling -- it’s what they contain.\nWhoever wrote the papers wrote it in a blood red pen, a loose pen, a pen that looks very similar to the Jack the Ripper letters. \nYou would know that pen anywhere.\nSo why… why does Officer Murrey have a pen eerily similar to the Ripper’s pen?")
																								print("\n \nOFFICER MURREY HAS BEEN ADDED TO YOUR LIST OF SUSPECTS")
																								mad = input("\n \nWOULD YOU LIKE TO (a) INVESTIGATE OFFICER MURREY OR (b) CONTINUE WITH JOSEPH?")
																								if mad == "a":
																									print("\n \nYou start to investigate Officer Murrey.")
																									thing = -4
																								elif mad == "b":
																									print("\n \nYou think that it’s time to ask Joseph some questions again. \nThis time, you’re meeting him at the hotel he’s staying at. ")
																									bon = input("\n \nPress (c) to continue, (o) to view options.")
																									if bon == "o":
																										continue
																									elif bon == "c":
																										print("\n \n“What else do you want to know?” Joseph asks, lazily lounging on his bed. You sit uncomfortably next to him. \n“How was… how was your relationship with Mary?”\nThat earns a sharp look from Joseph. “What do you mean?”")
																										bon = input("\n \nPress (c) to continue, (o) to view options.")
																										if bon == "o":
																											continue
																										elif bon == "c":
																											print("\n \n“I didn’t mean to offend, or anything, I just meant -- was it healthy? Did you two fight often, before the…”\nJoseph finishes your sentence for you. “Before I lost my job and she wanted to go back to being a whore?” \n“Well,” you say, “that’s one way to put it.”\nJoseph scoffs. “No. We were in love.” \n“That’s what you said last time,” you point out. \n“And?” Joseph is getting irritated. “Doesn’t make it less true.” ")
																											bon = input("\n \nPress (c) to continue, (o) to view options.")
																											if bon == "o":
																												continue
																											elif bon == "c":
																												print("\n \nYou are starting to get angry. \nYou remember that this isn’t just some mystery game, this is about the murder of your friend, your best friend.\n“Oh please,” you say, “you didn’t love her.”\nJoseph’s eyes widen-- he’s shocked that you’d say that. ")
																												bon = input("\n \nPress (c) to continue, (o) to view options.")
																												if bon == "o":
																													continue
																												elif bon == "c":
																													print("\n \n“I loved her,” Joseph insists. \n“Oh yeah?” you ask. “Did you love her when you were having an affair? Did you love her when you abused her?”\nJoseph’s eyes narrowed, becoming sharp things. He’s getting up from the bed, coming closer to you. ")
																													bon = input("\n \nPress (c) to continue, (o) to view options.")
																													if bon == "o":
																														continue
																													elif bon == "c":
																														print("\n \n“How do you-- why do you,” he stumbles, “why do you think that?”\n“I saw you with Lolly,” you tell him. “I saw you. In the alleyway. I saw it all.” \nHe looks concerned, like you’ve found out his biggest secret. ")
																														bon = input("\n \nPress (c) to continue, (o) to view options.")
																														if bon == "o":
																															continue
																														elif bon == "c":
																															print("\n \nHe inches closer to you. \n“Did you do it?” you whisper. \nHe doesn’t answer. \nYou’re backed up against the wall. ")
																															bon = input("\n \nPress (c) to continue, (o) to view options.")
																															if bon == "o":
																																continue
																															elif bon == "c":
																																if "knife" not in inventory:
																																	print("\n \n“Tell me you won’t tell them about what you saw,” Joseph says, in a low voice. \n“Why would I do that?” \nHe pins you with a wrist, holds you hostage against the wall. \n“Don’t tell them,” he says, but his voice is shaking, and you don’t think he knows that his grip is getting stronger, that it’s getting hard to breathe. \n“Please, don’t tell them,” he pleads,  “they already think it’s me, I have a life--”\nIt’s getting harder to breath. He’s not noticing. He’s rambling, desperate--\nYou manage one last choked out “help” before you die. ")
																																	print("GAME OVER.")
																																	done = True
																																elif "knife" in inventory:
																																	print("\n \n“Tell me you won’t tell them about what you saw,” Joseph says, in a low voice. \n“Why would I do that?” \nHe pins you with a wrist, holds you hostage against the wall. \n“Don’t tell them,” he says, but his voice is shaking, and you don’t think he knows that his grip is getting stronger, that it’s getting hard to breathe. ")
																																	print("You take out your knife and stab him once in the neck. ")
																																	print("His grip loosens, he falls. ")
																																	print("The police come. You are let go-- it was self defense. ")
																																	print("You wonder to yourself -- did I finally kill the Ripper?")
																																	print("Did I?")
																																	print("GAME OVER.")
																																	done = True
									if antonoff == "b":
										print("\n \nAfter Joseph leaves, you hurry to talk to the girl. \n“Hello,” you say. “You know Joseph, right?”\nThe brunette seems annoyed-- she was probably going to try to catch up with Joseph before you interrupted. ")
										me = input("\n \n Press (c) to continue, (o) to view options.")
										if me == "o":
											continue
										elif me == "c":
											print("\n \n“Yeah,” she says, sitting down. You take a seat across from her. \n“How do you know him?” you ask her. \nShe takes a sip of her drink. “We had a thing.”\nThat’s curious. After Joseph left Mary, he moved on pretty quick with a new girl named Carmen. \nThis brunette was not Carmen. ")
											fork = input("\n \nPress (c) to continue, (o) to view options.")
											if fork == "o":
												continue
											elif fork == "c":
												print("“When?” you ask. You try not to sound too nosy. \nThe brunette doesn’t mind. “If I remember correctly… around mid-October? Maybe late September?”\nYou are shocked. Joseph was still with Mary at the time.\nHad he been… having an affair? ]n“I loved her,” Joseph had said about Mary. You find that really hard to believe, now. ")
												outlet = input("\n \nPress (c) to continue, (o) to view options.")
												if outlet == "o":
													continue
												elif outlet == "c":
													print("\n \nYou have a lot to tell Officer Murrey when he calls you in later that week. \n“He was having an affair,” you tell him. “With this brunette.”")
													print("Murrey takes a bite of his donut. “Makes him more suspicious,” he says, mouth full. \n“Yeah,” you say. \nYou are about to say something else when something catches your eye-- blood red ink, just like the Ripper’s notes.")
													print("It’s on the papers, in Murrey’s handwriting, on Murrey’s desk, and no… it couldn’t be a coincidence, could it?\nWhy does Murrey have the Ripper’s pen?")
													print("\n \nMURREY HAS BEEN ADDED TO YOUR LIST OF SUSPECTS")
													suspects.append("Officer Murrey")
													mary = input("\n \nWOULD YOU LIKE TO a) INVESTIGATE MURREY INSTEAD OR b) CONTINUE INVESTIGATING JOSEPH?")
													if mary == "a":
														print("\n \nYou start to investigate Murrey.")
														thing = -4
													elif mary == "b":
														print("You search for evidence that Joseph and Mary’s marriage was a case of domestic abuse. \nWhen searching through Mary’s mail, you find a postcard. \nIt’s in Mary’s handwriting, and it’s addressed to Carmen DiLaurentis. \n \nPOSTCARD HAS NOW BEEN ADDED TO YOUR INVENTORY")
														inventory.append("postcard")
														kevin = input("\n \n Press (c) to continue, (o) to view options.")
														if kevin == "o":
															continue
														elif kevin == "c":
															print("\n \nCarmen is Joseph’s current girlfriend. It’s weird that Mary and her were talking. \nThe postcard says this:")
															print("")
															print("	Carmen, \n	Please come\n	I know it’s dangerous but\n	I can’t do this without you")
															print("")
															print("It was written a few days before Mary’s death. ")
															print("\n \nCARMEN HAS BEEN ADDED TO YOUR LIST OF SUSPECTS")
															suspects.append("Carmen DiLaurentis")
															print("")
															eff = input("DO YOU WANT TO a) INVESTIGATE CARMEN OR b) CONTINUE INVESTIGATING JOSEPH?")
															if eff == "a":
																thing = 4
																print("\n \nYou start to investigate Carmen. ")
															elif eff == "b":
																print("")
																print("You feel like something is wrong.\nYou wanted to investigate Carmen… why did you choose no?\nIt’s as if… \nIt’s as if somebody is controlling you. ")
																weird = input("\n \nPress (c) to continue, (o) to view options.")
																if weird == "o":
																	continue
																elif weird == "c":
																	print("")
																	print("That’s weird. Everything just-- stopped… for a second, before it continued….\n“Who’s there?” you ask. “Why won’t you let me be?”")
																	toby = input("\n \nPress (c) to continue, (o) to view options.")
																	if toby == "o":
																		continue
																	elif toby == "c":
																		print("\n \nTHERE! It happened again!! What’s going on?")
																		burnham = input("\n \nPress (c) to continue, (o) to view options.")
																		if burnham == "o":
																			continue
																		elif burnham == "c":
																			print("\n \nYou run back to Officer Murrey’s office. \n“What?” he says. “You think you’re… being controlled?”\nYou nod, yes, yes you do. \n“That’s ridiculous! Why would someone control you?”\n“I don’t know!” you yell. “For entertainment?”\nOfficer Murrey is looking at you like you are crazy. \nBut you’re not. \nYOU’RE NOT. \nRight?")
																			bo = input("\n \nPress (c) to continue, (o) to view options.")
																			if bo == "o":
																				continue
																			elif bo == "c":
																				print("\n \nThere! It happened again!\nWHO ARE YOU? WHY ARE YOU DOING THIS TO ME?\n“Okay, let’s pick this apart, logically,” Officer Murrey says, trying to calm you down. “If this was all being done for entertainment, wouldn’t this be more… entertaining?”")
																				taylor = input("\n \nPress (c) to continue, (o) to view options.")
																				if taylor == "o":
																					continue
																				elif taylor == "c":
																					print("\n \n“What?”\n“I’m just saying…” Officer Murrey says, “this is awful boring. You’re just in a room talking to a police officer. Wouldn’t whoever controlling you want this to be more exciting?”")
																					swift = input("\n \nDO YOU WANT IT TO BE MORE EXCITING? \na) YES \nb) F*** YES!")
																					if swift == "a":
																						print("You take the coffee on Officer Murrey’s desk and spill it on him. \nThe two of you start to fight. ")
																						tswift = input("\n \nPress (c) to continue, (o) to view options.")
																						if tswift == "o":
																							continue
																						elif tswift == "c":
																							print("\n \nPOW")
																							print("POW")
																							swizzle = input("\n \nPress (c) to continue, (o) to view options.")
																							if swizzle == "o":
																								continue
																							elif swizzle == "c":
																								print("\n \nBOOM")
																								print("POW")
																								haylorsux = input("\n \nPress (c) to continue, (o) to view options.")
																								if haylorsux == "o":
																									continue
																								elif haylorsux == "c":
																									print("\n \nOW")
																									kaylor = input("\n \nPress (c) to continue, (o) to view options.")
																									print("\n \nYou win and Officer Murrey dies. \nBut then…\nthen the police find you. ")
																									print("GAME OVER")
																									done = True
			if brett == "n":
				print("\n \nYou stay solo and decide to visit Joseph’s current girlfriend, Carmen. \nHe moved on fast after Mary. \n“He’s trying to spite me,” Mary would complain to you. “It’s all because he lost his job, that absolute bag of di-” \nYou hurry to Carmen’s flat. The two have only  been dating for a month, so she lives alone. \nWhen you knock at the door, you see Carmen for the first time. \nShe’s a beautiful Romani woman; cherry lips, cartoon eyes. \n“Can I come in?”")
				jesus = input("\n \nPress (c) to continue, (o) to view options.")
				if jesus == "o":
					continue
				elif jesus == "c":
					print("\n \n“I’m sorry for your loss,” Carmen says, handing you tea.")
					print("“Thank you,” you say. The tea is lukewarm. You drink it anyways, trying to be polite.")
					j = input("\n \nPress (c) to continue, (o) to view options.")
					if j == "o":
						continue
					elif j == "c":
						print("\n \n“Right,” she says. “What are you here for?” \n“I was actually here to talk about Joseph.” \nCarmen sits down, gives a grimace. “Ugh, Joseph. We’re currently in a fight. He can really be the worst sometimes, don’t you think?”")
						print("“Mary would say that too,” you say. “What do you know about his relationship with Mary?” \nCarmen shrugs, looks down at her tea. “Nothing you probably don’t already know.” \n“They divorced because of Mary’s job. That’s what I know.” \n“Really?” Carmen asks. “Do you know about the--” She stops. Takes a sip of her awful lukewarm tea.")
						u = input("\n \nPress (c) to continue, (o) to view options.")
						if u == "o":
							continue
						elif u == "c":
							print("\n \n“What?” you press. \n“Joseph… well… Mary’s prostitution wasn’t the only reason they didn’t work out.” \nThis is new information to you. You are a bit hurt- why did Mary not tell you this?")
							print("“What was the other reason?” \n“Joseph didn’t want children,” Carmen says. “Hated them, hated the idea of having them. God, he’d rather die.” \n“And?” \nCarmen looks surprised you don’t know. \n“And Mary wanted them. She didn’t tell you?” \n“No,” you say. ")
							christ = input("\n \nPress (c) to continue, (o) to view options.")
							if christ == "o":
								continue
							elif christ == "c":
								print("\n \n“Where is the bathroom?” you ask. \n“Down the hallway, third door to the left.” \n“Thank you.” ")
								gasp = input("\n \nWOULD YOU LIKE TO a) GO TO THE BATHROOM or b) LOOK IN CARMEN'S ROOM?")
								if gasp == "a":
									print("\n \nYou find the bathroom easily. You wash your hands at the sink, but your eyes catch on something silver. \nA wedding ring, at the edge of the counter. \nNot Joseph’s-- Mary’s. \nWhy does Carmen have Mary’s wedding ring in her bathroom?")
									print("\n \nMARY’S WEDDING RING HAS BEEN ADDED TO YOUR INVENTORY")
									inventory.append("mary's wedding ring")
									print("\n \nCARMEN DILAURENTIS HAS BEEN ADDED TO YOUR LIST OF SUSPECTS")
									suspects.append("Carmen DiLaurentis")
									print("You start to investigate Carmen.")
									thing = 4
								elif gasp == "b":
									print("\n \nYou don’t actually go to the bathroom. You take the opportunity to look around the flat. \nYou go into Carmen’s room. \nIt’s nice. Simple, decorated nicely.")
									print("Your eyes catch on a familiar looking book on Carmen’s desk. \nYou go to pick it up. Open the pages. \nIt’s Mary’s diary. \nWhy does Carmen have Mary’s diary in her bedroom?")
									print("\n \nMARY’S DIARY HAS BEEN ADDED TO YOUR INVENTORY")
									inventory.append("mary's diary")
									print("\n \nCARMEN DILAURENTIS HAS BEEN ADDED TO YOUR LIST OF SUSPECTS")
									suspects.append("Carmen DiLaurentis")
									anna = input("WOULD YOU LIKE TO (A) INVESTIGATE CARMEN OR (B) CONTINUE INVESTIGATING JOSEPH?")
									if anna == "a":
										print("\n \nYou start to investigate Carmen.")
										thing = 4
									if anna == "b":
										print("\n \nYou hide the diary in your bag. Carmen gives you some more tea before you leave: “For times when the grief becomes too hard,” she says. \nOkay, Carmen. ")
										kristoff = input("\n \nPress (c) to continue, (o) to view options.")
										if kristoff == "o":
											continue
										elif kristoff == "c":
											print("\n \nWhen you get home, you read the diary’s contents. \n \nSeptember 14, 1888 \nThings have been rocky between Joseph and I. \nI’ll be honest - \nI’m scared. I think that he’s capable of doing… things…")
											olaf = input("\n \nPress (c) to continue, (o) to view options.")
											if olaf == "o":
												continue
											elif olaf == "c":
												print("\n \nOctober 1, 1888 \nI’m pregnant. \nIt’s Joseph’s. \nHe wasn’t happy when I told him. ")
												onepercent = input("\n \nPress (c) to continue, (o) to view options.")
												if onepercent == "o":
													continue
												elif onepercent == "c":
													print("\n \nOctober 20, 1888 \nJoseph has lost his job. I don’t know what to do. \nI want to go back to work. We need the money. \nI need the money. This baby…")
													car = input("\n \nPress (c) to continue, (o) to view options.")
													if car == "o":
														continue
													elif car == "c":
														print("\n \nOctober 21, 1888\nHe says that he hates people like me. Women like me. \nHe says that if he could, he would kill all of us and then some. \nMaybe he was bluffing, to scare me off. \nMaybe --\nHe’s here, I have to go, I have t\n \nThe last entry is left off in a smear. \nThe evidence is enough to be incriminating. ")
														pal = input("\n \nPress (c) to continue, (o) to view options.")
														if pal == "o":
															continue
														elif pal == "c":
															print("\n \nA few days later, another Ripper letter is sent out. Left on the doorstep of the police’s station.\nIt reads:\n	Dear mr. Satan,\n	I am  having so fun! My toes tingle down everytime I do I job, but the best part boss is, the idiots playing hide n seek with me! \n    They think they are on something but I dont think they will ever win this game.\n	Its their fault, they shouldntve gave me so much time to hide!\n	Sincerely\n	Ripper, Jack\n \nThe letter came in a box with severed toes painted bright red. You don’t want to think about whether those toes were Mary’s.")
															ok = input("\n \nPress (c) to continue, (o) to view options.")
															if ok == "o":
																continue
															elif ok == "c":
																print("\n \nYou are thinking about Mary’s diary. \nAll the evidence leads up to Joseph. \nYou think that maybe all the other Ripper victims-- all the prostitutes-- could’ve been killed by Joseph to scare Mary off the streets. ")
																bf = input("\n \nPress (c) to continue, (o) to view options.")
																if bf == "o":
																	continue
																elif bf == "c":
																	print("\n \nYou decide that you need more evidence before accusing Joseph. You need to be certain. \nYou ask the police for more details about Mary’s murder, details about how she was murdered, about the physical state she was in. \nThey tell you that her fingernails and toes were painted a bright red. ")
																	gf = input("\n \nDO YOU WANT TO LOOK AT THE a) CAFE NEAR MARY'S DEATH OR b) DOCTOR'S OFFICE NEARBY? ")
																	if gf == "a":
																		print("You find a bit of a red fingernail after an hour of looking around the cafe. \nIt is the same shade as Mary’s. \nYou hurriedly take a picture of Joseph out, and ask the cafe owner if he’d seen him the day of Mary’s murder. \nThe cafe owner says yes. ")
																		print("\n \nRED FINGERNAIL HAS BEEN ADDED TO YOUR INVENTORY")
																		inventory.append("red fingernail")
																		neck = input("\n \nWOULD YOU LIKE TO ALERT THE AUTHORITIES? (y or n) ")
																		if neck == "n":
																			print("\n \nThis is the programmer speaking: I am exhausted. There are a million different storylines. I really, really do not want to write another one. Please pick again. ")
																			head = input("\n \nWOULD YOU LIKE TO ALERT THE AUTHORITIES? (y or y or y) ")
																			if head == "y":
																				print("\n \nThere is enough evidence-- the wedding band, the fingernail, the diary. \nThey arrest Joseph. He is sentenced to death and hanged for his crimes. \nA month later, you receive another letter, with the same handwriting as the as the dear mr. Satan letter. \nThere’s blood stains on it. \nAll it says is this:\n	You killed the wrong man\n	-Saucy Jack")
																				print("GAME OVER")
																				done = True
																			else:
																				print("\n \nYOU SUCK. GAME OVER")
																				done = True
																		elif neck == "y":
																			print("\n \nThere is enough evidence-- the wedding band, the fingernail, the diary. \nThey arrest Joseph. He is sentenced to death and hanged for his crimes. \nA month later, you receive another letter, with the same handwriting as the as the dear mr. Satan letter. \nThere’s blood stains on it. \nAll it says is this:\n	You killed the wrong man\n	-Saucy Jack")
																			print("GAME OVER")
																			done = True
																	elif gf == "b":
																		print("\n \nYou enter the doctor’s office. The room is empty. \nYou start to investigate the room for any clues. After a while, you find a chipped bit of a red fingernail. \nIt is the same shade as Mary’s. \nYou are ecstatic, but then the door opens. ")
																		shoulder = input("\n \nPress (c) to continue, (o) to view options.")
																		if shoulder == "o":
																			continue
																		elif shoulder == "c":
																			print("\n \nA man with a beard walks in. \n“Oh, sorry, are you a doctor?” you say.\n“Yes,” the man says warily. “Why are you here?”\n“I’m investigating the death of Mary Jane Kelly. I found this red fingernail that matches hers here,” you tell him.")
																			print("You pull out a picture of Joseph. “Did you happen to see this man come in the day of the murder?”\nThe man closes the door behind him.\n“No,” he says.\n“Oh, well, thank you anyways, I apprecia--”")
																			print("The man pins you against the wall before you can say anything else.\nHe takes out a knife.\nYou have been killed by Jack the Ripper!")
																			print("GAME OVER")
																			done = True