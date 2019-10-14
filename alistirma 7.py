Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #alistirma7
>>> 
>>> x=0
>>> for a in range(1,10):
	for b in range(0,10):
		for c in range(0,10):
			if a+b==c:
				x=x+1
				print(int(100*a+10*b+c))

				
101
112
123
134
145
156
167
178
189
202
213
224
235
246
257
268
279
303
314
325
336
347
358
369
404
415
426
437
448
459
505
516
527
538
549
606
617
628
639
707
718
729
808
819
909
>>> x
45
>>> 
