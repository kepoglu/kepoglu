Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #alistirma8
>>> x=0
>>> cift=[0,2,4,6,8]
>>> for a in range(1,10):
	for b in range(0,10):
		for c in cift:
			if a==b or a==c or b==c:
				x=x+1

				
>>> x
122
>>> 
