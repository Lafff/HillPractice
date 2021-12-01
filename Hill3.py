import numpy as np

dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,
		'V':21,'W':22,'X':23,'Y':24,'Z':25,'а':26,'б':27,'в':28,'г':29,'д':30,'е':31,'ж':32,'з':33,'и':34,'й':35,'к':36,'л':37,'м':38,'н':39,
		'о':40,'п':41,'р':42,'с':43,'т':44,'у':45,'ф':46,'х':47,'ц':48,'ч':49,'ш':50,'щ':51,'ъ':52,'ы':53,'ь':54,'э':55,'ю':56,'я':57,' ':58,
		',':59,'.':60,':':61,'!':62,'?':63}
def solve(open_text,key):
	key_matrica = np.array(([key[0],key[1],key[2]],[key[3],key[4],key[5]],[key[6],key[7],key[8]]))
	obr_matrix = np.linalg.inv(key_matrica)
	obr_matrix %= 64
	obr_matrix = np.round(obr_matrix).astype(int)

	result= '<table align="center" cellspacing=30px"><tr><th>Ключевая матрица</th><th>Обратная матрица</th></tr> <tr><td>'+str(key_matrica[0]) + '<p>' + str(key_matrica[1]) + '<p>'+ str(key_matrica[2])+'</td><td>'+str(obr_matrix[0]) + '<p>' + str(obr_matrix[1]) + '<p>'+ str(obr_matrix[2])+'</td></tr></table>'
	closed_text = ''
	decoded_text = ''

	if len(open_text) % 3 != 0:
		open_text += ' ' * (3 - (len(open_text) % 3))

	result += '<div style="text-align:center;">!!!-------------------КОДИРОВАНИЕ-------------------!!!</div><br>'
	for i in range(0, len(open_text),+3):
		cycle_count = 1
		block = np.array((dict[open_text[i]], dict[open_text[i+1]],dict[open_text[i+2]]))
		result+= '<p><span style="color:#ed9393;">Текущий блок: </span>' + str(block[0]) + ' '+ str(block[1]) + ' '+ str(block[2]) + '</p>'
		for j in key_matrica:
			result += f'C{cycle_count} = {j[0]}*{block[0]} + {j[1]}*{block[1]} + {j[2]}*{block[2]} = {j[0]*block[0]} + {j[1]*block[1]} + {j[2]*block[2]} = {j[0]*block[0] + j[1]*block[1] + j[2]*block[2]}(mod64) = {(j[0]*block[0] + j[1]*block[1] + j[2]*block[2])%64}<br>'
			cycle_count+=1
		for j in key_matrica.dot(block):
			for key,value in dict.items():
				if j%64 == value:
					closed_text = closed_text + key
	result +='<div style="text-align:center;margin-top:40px;">Закрытый текст:   ' + closed_text + '</div>'

	result +='<div style="text-align:center;margin-top:40px;">!!!-------------------ДЕКОДИРОВАНИЕ-------------------!!!</div>'
	for i in range(0, len(closed_text),+3):
		cycle_count = 1
		block = np.array((dict[closed_text[i]], dict[closed_text[i+1]],dict[closed_text[i+2]]))
		result+= '<p><span style="color:#ed9393;">Текущий блок: </span>' + str(block[0]) + ' '+ str(block[1]) + ' '+ str(block[2]) + '</p>'
		for j in obr_matrix:
			result += f'C{cycle_count} = {j[0]}*{block[0]} + {j[1]}*{block[1]} + {j[2]}*{block[2]} = {j[0]*block[0]} + {j[1]*block[1]} + {j[2]*block[2]} = {j[0]*block[0] + j[1]*block[1] + j[2]*block[2]}(mod64) = {(j[0]*block[0] + j[1]*block[1] + j[2]*block[2])%64}<br>'
			cycle_count+=1
		for j in obr_matrix.dot(block):
			for key,value in dict.items():
				if j%64 == value:
					decoded_text = decoded_text + key
	result +='<div style="text-align:center;margin-top:40px;">Декодированный текст:   ' + decoded_text + '</div>'
	return result