import payloads


def control( **kwargs):
	if kwargs['payload'] in payloads.Encoders().py:
		import pyminifier
		from pyminifier import hero
		if "bzip2" in kwargs['payload']:
			hero.main(obfuscate=True, bzip2=True, gzip=False ,files=kwargs['files'])
		else:
			hero.main(obfuscate=True, bzip2=False, gzip=True ,files=kwargs['files'])	
