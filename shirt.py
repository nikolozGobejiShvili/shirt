from fpdf import FPDF
text=input("Name: ")
image = "shirtificate.png"
shirt = FPDF(orientation='portrait', format="A4")
shirt.add_page()
shirt.set_font("Arial", size=60)
shirt.cell( 0, 75,  txt="CS50 Shirtificate", align="C" )
shirt.image(image, x=0, y=85, w=210)
shirt.set_font("Arial", size=30)
shirt.cell(-190, 300, txt=text , align="C")


shirt.output("shirt.pdf")

