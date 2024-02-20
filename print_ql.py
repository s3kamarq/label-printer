import brother_ql as ql

class etickettendrucker:

	###Printer Parameter
	backend ="pyusb"
	model ="QL-800"
	printer ="usb://0x04f9:0x209b"
	PRINTER_IDENTIFIER = "file:///dev/usb/lp0"

	def print_label(self, labels):
		try:
			self.printer = ql.BrotherQLRaster("QL-800")
			print_data = ql.brother_ql_create.convert(self.printer, labels, "62", dither=True, rotate=0, red=True)
			send(print_data, PRINTER_IDENTIFIER)
			print("Drucken")
		except:
			print("Drucker Fehler")
		

#testing
#drucker = etickettendrucker()
#drucker.print_label('11')


#printer = ql.BrotherQLRaster("QL-800")
#print_data = ql.brother_ql_create.convert(printer, '11', "62", dither=True, rotate=0, red=True)
#send(print_data, PRINTER_IDENTIFIER)
#print("Drucken")


#printer = ql.BrotherQLRaster("QL-800")
#print_data = ql.brother_ql_create.convert(printer, labels, "62", dither=True, rotate=0, red=True)
		#send(print_data, PRINTER_IDENTIFIER)
	
#print("Drucken")
#image.show()