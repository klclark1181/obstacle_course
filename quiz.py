import tkinter as tk
from tkinter import simpledialog
import threading
import time


def ClueQuestion(num, cluequestion, clueanswer, clue, quizquestion, quizanswer,
	movie_quote, movie):
	clued = False
	while True:
		if clued:
			answer = simpledialog.askstring('Question %d' % (num),
				'Advancement Question: %s' % (quizquestion), parent=window)
		else:
			answer = simpledialog.askstring('Question %d' % (num),
				'Clue Question: %s\n\nAdvancement Question: %s' %
				(cluequestion, quizquestion),
				parent=window)
		if answer != None:
			if answer.casefold() == clueanswer.casefold() or \
					answer.casefold() == movie.casefold():
				if clued != True:
					T.insert(tk.END, 'Clue #%d: %s\n' %(num, clue))
					clued = True
			elif answer.casefold() == quizanswer.casefold():
				if clued != True:
					T.insert(tk.END, 'Clue #%d: %s\n' %(num, clue))
				T.insert(tk.END, '%s: %s\n' %(quizquestion, answer))
				tk.messagebox.showinfo('You move on',
					'Correct!\n\n\"%s\"\n - %s' % (movie_quote, movie))
				return
			else:
				# print out error message
				wait = 120
				before = time.time()
				tk.messagebox.showinfo('You are wrong!', 
					'Wrong answer: %d second penalty\n\n'
					'Your movie quote is:\n\n\"%s\"' % (wait, movie_quote))
				while((time.time() - before) < wait):
					time.sleep(0.5)
	

window = tk.Tk()
window.wm_title('Coding Obstacle Course')
T = tk.Text(window, height=40, width=80)
T.pack()
greeting = 'Welcome to the Clark Network and Coding Obstacle Course'
T.insert(tk.END, '%s\n\n' % (greeting))
tk.messagebox.showinfo('Welcome', greeting)

number = 1;
ClueQuestion(
    num = number,
	cluequestion = 'Who is the best stooge (This is somewhat subjective)?', 
    clueanswer = 'Curly',
	clue = 'The ip command is very helpful',
	quizquestion = 'What is the IPv4 address for your public interface?', 
    quizanswer = '',
	movie_quote = 'Hello. My name is Indigo Montoya. You killed my father. Prepare to die.',
	movie = 'The Princess Bride'
)

#number += 1;
#ClueQuestion(
#    num = number,
#	cluequestion = '', 
#    clueanswer = '',
#	clue = 'The ip command is very very helpful',
#	quizquestion = 'What is the MAC or Hardware address of your Network Interface card?', 
#   quizanswer = '',
#	movie_quote = '',
# 	movie = ''
#)

number += 1;
ClueQuestion(
    num = number,
	cluequestion = 'Who is the worst stooge (This is totally scientific)?', 
    clueanswer = 'Shemp',
	clue = 'The route command will be helpful here',
	quizquestion = 'What is the IPv4 address of your router or gateway?', 
    quizanswer = '192.168.1.1',
	movie_quote = 'I\'ve got a big head and little arms. I\'m just not sure how well this plan was thought through.',
	movie = 'Meet the Robinsons'
)

number += 1;
ClueQuestion(
    num = number,
	cluequestion = 'What word in the English language has two synonyms, that are antonyms to each other?', 
    clueanswer = 'cleave',
	clue = 'The ip command is very, very, very helpful',
	quizquestion = 'How many subnet bits are there for your local subnet?', 
    quizanswer = '24',
	movie_quote = 'How about, science slumber parties?',
	movie = 'A Goofy Movie'
)

number += 1;
ClueQuestion(
    num = number,
	cluequestion = 'What country has the most islands in the world?', 
    clueanswer = 'Sweden',
	clue = 'The numbers in an IPv4 address are noted W.X.Y.Z, In a subnet with 24 subnet bits, W, X and Y are always the same. Z changes and can be any number but 0 that can be represented with 8 bits because there are 32 bits in and IPv4 address, but 24 are fixed subnet bits. 0 is not used for the last 8 bits',
	quizquestion = 'What is the lowest IPv4 address in your subnet?', 
    quizanswer = '192.168.1.1',
	movie_quote = 'I already know an awful lot of people and until one of them dies I couldn\'t possibly meet anyone else.',
	movie = 'Charade'
)

number += 1;
ClueQuestion(
    num = number,
	cluequestion = 'What English word uses all 5 vowels plus y in alphabetical order?', 
    clueanswer = 'facetiously',
	clue = 'That was a really hard clue question to get the clue: DITTO!',
	quizquestion = 'What is the highest IPv4 address in your subnet?', 
    quizanswer = '192.168.1.255',
	movie_quote = 'Blythe\'s not blind when he\'s with me, and he\'s going with me.',
	movie = 'The Great Escape'
)

number += 1;
ClueQuestion(
    num = number,
	cluequestion = 'What is the answer to the ultimate question of life, the universe and everything?', 
    clueanswer = '42',
	clue = 'In /home/pi/ping_scan, there is a python file that will almost allow you to scan your subnet for addresses. Modify it using the information you have gathered to find your answer!',
	quizquestion = 'What is your opponent\'s IPv4 address?', 
    quizanswer = '',
	movie_quote = 'A jester unemployed is nobody\'s fool!',
	movie = 'The Court Jester'
)

#number += 1;
#ClueQuestion(
#    num = number,
#	cluequestion = '', 
#    clueanswer = '',
#	clue = 'The ARP Protocol is used to resolve an IP address to a MAC address. The ARP command will show you the ARP table of your box.',
#	quizquestion = 'What is your opponent\'s MAC or Hardware address?', 
#    quizanswer = '',
#	movie_quote = '',
#	movie = ''
#)

number += 1;
ClueQuestion(
    num = number,
	cluequestion = 'What does IANA stand for?', 
    clueanswer = 'Internet Assigned Numbers Authority',
	clue = 'Google it!',
	quizquestion = 'What is the IANA assigned TCP port number for ssh?', 
    quizanswer = '22',
	movie_quote = 'What do you want us to die of... old age?',
	movie = 'Secondhand Lions'
)

number += 1;
ClueQuestion(
    num = number,
	cluequestion = 'Do you really need a clue?', 
    clueanswer = 'no',
	clue = 'Google it!',
	quizquestion = 'What is the IANA assigned TCP port number for http?', 
    quizanswer = '80',
	movie_quote = 'I\'ve been savin\' this money for a divorce, if ever I got a husband.',
	movie = 'It\'s a Wonderful Life'
)

number += 1;
ClueQuestion(
    num = number,
	cluequestion = 'Who was the 16th U.S. President?', 
    clueanswer = 'Abraham Lincoln',
	clue = 'In /home/pi/port_scan/ there is a python script that will almost allow you to port scan your opponent. The TCP port you are looking for is between the ports for ssh and http. Modify it using what you know to find the opponent\'s open TCP ports. ',
	quizquestion = 'What TCP port is listening on your opponent\'s box that you should connect to in order to send a message?', 
    quizanswer = '77',
	movie_quote = 'Mayor Ollie Perkins: I guess you know what you\'re doing, Sheriff.\n Jason McCullough: I don\'t know what I could have said to give you that idea, Mayor.',
	movie = 'Support Your Local Sheriff'
)

number += 1;
ClueQuestion(
    num = number,
	cluequestion = 'What is the most famous tennis tournament in England?', 
    clueanswer = 'Wimbledon',
	clue = 'In /home/pi/message_client, modify the message_client.py file to send a message of your choice to your opponent using the information you have accumulated. Then run the program to win.',
	quizquestion = 'What does the message in the box say when you win?', 
    quizanswer = 'Good game.',
	movie_quote = 'Let me try. I\'m a genius',
	movie = 'Strange Brew'
)
window.mainloop()
