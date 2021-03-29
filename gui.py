#Author: YmStrip
#Hint: Unauthorized use is prohibited 
#Github: github.com/YamStrip/mcpy/gui.py
#Website: www.pomelors.com

#UI encapsulation plug-in 

#Introduce client.extraClientApi
#import client.extraClientApi as cl

#Create a UI object
#uilib = cl .GetScreenNodeCls ( )

#Gpl protocol 

#Category 
"""
class fa ( uilib ):
	def __init__ ( self , names , name , p ):
		cl .__init__ ( self , names , name , p )
"""
#ast
def ast ( data ):
	"""
	#name getbyUIName
	.type getbyUItype
	:src: getbyUIsrc
	*, and
	*+ logic and
	*! logic not
	*[] Additional parameters 
	Example: :/name:[3:3],.type[first]
	*[first] the first
	*[last] the last
	*[index] the Fix index
	*[index1:] the slice index , ...
	*[:index1] the slice ... , index
	*[index:index1] slice index1:index2
	*[random]
	The body uses "," or "+" Segmentation 
	"""
	def gettype ( d ):
		if ( d == ":" ):
			return "src"
		elif ( d == "." ):
			return "type"
		else:
			return "name"
	def getappend ( d ):
		k = d .split ( ":" )
		f = len ( k )
		if ( d == "first" ):
			return {"type":"first"}
		elif ( d == "last" ):
			return {"type":"last"}
		elif ( f == 1 ):
			return {"type":"slice","data":[ int ( d ), int ( d ) ]}
		elif ( f == 2 ):
			if ( k [ 0 ] == "" ):
				return {"type":"slice","data":[0,int(k[1])]}
			elif ( k[1] == "" ):
				return {"type":"slice","data":[int(k[0]),999999]}
			else:
				return {"type":"slice","data":[int(k[0]),int(k[1])]}
	#state Simple ast 
	task = [ ]
	length = len ( data )
	i = 0
	ids = 0
	log = None
	ini = False
	while i < length:
		d = data [ i ]
		if d == " ":
			i += 1
			continue
		if ( d == "," or d == "+" or d == ":" or d == "." or d == "#" or d == " " or d == "!" ):
			#test
			if ( d == " " ):
				i += 1
				continue
			if ( d == "," or d == "+" or d == "!" ):
				if ( len ( task ) == 0 ):
					return [ ]
				else:
					#split task
					if ( d == "," ):
						ids += 1
						log = None
					elif ( d == "!" ):
						log = "!"
					elif ( d == "+" ):
						log = "+"
						i
					i += 1
					continue
			#self
			types = None
			datas = None
			append = None
			for j in range ( i+1 , length ):
				#state: auto
				l1 = False
				if ( j < length -1 ):
					fg = data[j+1]
					if ( fg == "+" or fg == "," or fg == "!" or j == length -1 or fg == ":" or fg == "[" ):
						l1 = True
					if ( fg == " " ):
						continue
				if ( l1 == True or j == length -1 ):
					datas = data[i+1:j+1]
					types = gettype ( d )
					if ( l1 == True ):
						if data[j+1] == ":":
							j+=1
						l2 = False
						if ( j < length -2 ):
							if ( data [ j+1 ] == "[" ):
								l2 = True
						if l2 == True:
							t = False
							for k in range ( j+2 , length ):
								if ( data [k] == "]" ):
									t = True
									append = getappend ( data[j+2:k] )
									j = k
									break
							if t == False:
								return [ ]
					task .append ( {
						"type": types,
						"data": datas,
						"append": append,
						"id": ids,
						"logic": log
					} )
					i = j
					break
		else:
			return [ ]
		i += 1
	#pack
	nt = [ ]
	ntf = [ ]
	ide = None
	for i in task:
		if ide == None: ide = i [ "id" ]
		if ide != i [ "id" ]:
			ide = i [ "id" ]
			nt .append ( ntf )
			ntf = [ ]
			ntf .append ( i )
		else:
			ntf .append ( i )
	if ( len ( ntf ) != 0 ):
		nt .append ( ntf )
	return nt

print(ast(" #test ! #data + :/src.json:[:1] , .a+#test1[first] ! .button[128:]"))

#mcUI jquery
def mcjq ( UI ):
	def S1 ( src , fat ):
		return S ( src , fat )
	class S ( src , fat ):
		ites = [ ]
		types = None
		srclib = [ None ]
		try:
			src .ChangeBindEntityId ( )
			src .GetBindAutoScale ( )
			ites = [ src ]
		except:
			#jquer Test
			asts = ast ( src )
			for i in asts:
				for j in i:
					pass
		#def
		
		#Ultra-simple AST
		ast = ast
		
		#id
		def getid ( ):
			return UI .GetBindEntityId ( )
		def setid ( id ):
			return UI .ChangeBindEntityId ( id )
		bind = setid
		bindid = setid
		setbind = setid
		id = setid
		isid = getid
		
		#zoom
		def zoom ( bol = True ):
			if bol == True:
				return UI .ChangeBindAutoScale ( 1 )
			else:
				return UI .ChangeBindAutoScale ( 0 )
		def iszoom ( ):
			return UI .GetBindAutoScale ( )
		getzoom = iszoom
		setzolm = zoom
		
		
		#offset
		def offset ( x , y , z ):
			return UI .ChangeBindOffset ( ( x , y , z ) )
		def getoffset ( ):
			return UI .GetBindOffset ( )
		isoffset = getoffset
		setoffset = offset
		
		#getChildren
		def get ( ):
			return ites
		
		#path
		def path ( ):
			return srclib 
		def apath ( ):
			return srclib [ 0 ]
		
		#pos
		def father ( num = 1 ):
			s = fat
			for i in range ( 1 , num ):
				s = fat .father ( )
			return s
		def next ( ):
			#I don't know how to query the node path for the time being 
			pass
		
		#jq search
		def find ( jq ):
			#ast Frame 
			task = ast ( jq )

class ui:
	pass