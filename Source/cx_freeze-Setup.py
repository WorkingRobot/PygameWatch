import cx_Freeze

executables = [cx_Freeze.Executable("Watch.pyw", base = "Win32GUI")]

cx_Freeze.setup(
	name="Watch",
	options={"build_exe": {"packages":["pygame"],
	"include_files":["10.png", "11.png", "12.png", "13.png", "14.png", "15.png", "16.png", "17.png", "18.png", "19.png", "20.png", "21.png", "cursor.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png","alarmSound.mp3","font.TTF","icon.ico"]}},
	executables = executables
	)
