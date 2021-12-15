"""
tudo possivel graças
https://github.com/mouuff/mtranslate

MIT License
Copyright (c) 2016 Arnaud Aliès
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import io
from mtranslate import translate

l1=io.open('legenda_ingles.srt','r',encoding='utf-8')
l3=io.open('legenda_traduzida.srt','w',encoding='utf-8')
#traduz do google
cont=0
while 1:
	line=l1.readline()
	if(len(line)==1):
		l3.write(line)
		line=l1.readline()
		l3.write(line)
		line=l1.readline()
	if not line:
		l3.write(translate(line,'pt','en'))
		break
	l3.write(translate(line,'pt','en'))
	l3.write('\n')
l1.close()
l3.close()


#corrige erro google translate

l1=io.open('legenda_traduzida.srt','r',encoding='utf-8')
l2=io.open('legenda_traduzida.srt','r',encoding='utf-8')
l3=io.open('legenda_final.srt','w',encoding='utf-8')


prox=l2.read(1)
anterior='c'

atual=l1.read(1)
while(atual!=""):
	prox=l2.read(1)
	if(atual=='-' and prox=='>'):
		l3.write('-')
	if(atual!='\n'):	
		if(prox!=""):
			if((ord(prox)<58) and (ord(prox)>47)):
				if(anterior==':' and atual==' '):
					atual=l1.read(1)
					prox=l2.read(1)
					l3.write(atual)
					atual=l1.read(1)
					prox=l2.read(1)
			if((ord(prox)<58) and (ord(prox)>47) and (ord(anterior)<58) and (ord(anterior)>47) and (atual==' ' or atual=='.')):
				l3.write(',')
				atual=l1.read(1)
				prox=l2.read(1)

			if(anterior=='/' and prox=='i'):
					atual=l1.read(1)
					prox=l2.read(1)
					
	anterior=atual;
	l3.write(atual)
	#print(atual)
	atual=l1.read(1)


l1.close()
l2.close()
l3.close()