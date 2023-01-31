from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
  except:
    print("Hubo un error Chico")
  print("Se Completo La Descarga!!!!")

link = input("Pon tu URL De youtube Aqui ")
Download(link)

"""
Para funcion de esta aplicacion se necesita el modulo pytube porque se me olvido hacerlo en
un entorno virtual XD
Para instalarlo ponga pip install pytube
"""