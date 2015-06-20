def FlipaBits(value, flip)
	if flip == 1:
		mask = '{0:032b}'.format(1431655765) #0x55555555
	elif flip == 2:
		mask = '{0:032b}'.format(2863311530) #0xAAAAAAAA
	elif flip == 3:
		mask = '{0:032b}'.format(randint(0, 4294967295)) #random de 0x00000000 e 0xFFFFFFFF

	if flip != 0:
		valueInt = int(value)
		valueBin = '{0:032b}'.format(valueInt)
		valueBinFlip = int(valueBin,2) ^ int(mask,2)
		value = valueBinFlip
	return value