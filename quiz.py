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
					'Correct!\n\n%s' % (movie_quote))
				return
			else:
				# print out error message
				wait = 180
				before = time.time()
				tk.messagebox.showinfo('You are wrong!', 
					'Wrong answer: %d second penalty\n\n'
					'Your movie quote is:\n\n%s' % (wait, movie_quote))
				while((time.time() - before) < wait):
					time.sleep(0.5)
	

window = tk.Tk()
window.wm_title('Coding Obstacle Course')
T = tk.Text(window, height=40, width=80)
T.pack()
greeting = 'Welcome to the Dave Clark Memorial Network and Coding Obstacle Course'
T.insert(tk.END, '%s\n\n' % (greeting))
tk.messagebox.showinfo('Welcome', greeting)

ClueQuestion(1,
	'Do you stink?', 'yes', 'The ip command is very helpful',
	'What is your IP address?', '192.168.1.1',
	'Stupid! You\'re so STUPID!', 'UHF')
ClueQuestion(2,
	'What is the answer to life, the universe and everything?', '42',
	'The ip command is very very helpful',
	'What is your MAC address?', 'FF:FF:FF:FF:FF:FF',
	'Hello. My name is Indigo Montoya. You killed my father. Prepare to die.',
	'The Princess Bride')

window.mainloop()
