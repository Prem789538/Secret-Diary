# fake_editor
Text editor in python


Usage:-

	run the program, and you can start writing



CaughtMode:-

	when we press \ (backslash) the editor become
	normal and no data is being written to actual
	file
	
	NOTE:- Once entered, you can't get out of caught
		mode, you  have to restart it


Features:-

	* Autosaves when we press enter
	* Backspace is allowed (in real data too)
	* Caught Mode available
	* Fake data is loaded beforehand to improve performance
	* Can add multiple fake files
	* No need to focus on the text area
	* Auto completion at end of line


Errors:-

	* Backspace not working in windows (line 58 keycode(=22 in linux) (=8 in windows))

	* Can only remove last line
	
