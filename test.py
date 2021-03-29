from ym import ui

def create ( self ):
	jq = ui .load ( ui .get ( self , '/data' ) )
	jq .show ( )
	jq .find ( '#main!.button,.text+:/main:[:1]' ) .settext ( 'main' ) .setcolor ( '#ffffff' )
	jq .find ( 'say[first]' ) .onclick ( '''click func''' ) .settext ( 'hello' )
ui .create ( create )