import numpy as np
import asyncio
import time
async def generate():
	now = time.time()
	result = ''
	while True:
		arr = np.random.randint(0, 64, (3, 3))
		if round(np.linalg.det(arr)) == 1:
			for i in arr:
				for j in i:
					result += str(j) + ' '
			return result
		print(str(np.linalg.det(arr)) + ' for THREE')
		await asyncio.sleep(0.01)
		if time.time() - now > 20:
			return result