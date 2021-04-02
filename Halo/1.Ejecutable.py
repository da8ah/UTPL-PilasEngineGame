# coding: utf-8
import pilasengine
import random

puntos = 0

pilas = pilasengine.iniciar()        

sonido_menu = pilas.sonidos.cargar('Z_Spirit_Of_Fire.wav')
sonido_nivel_1 = pilas.sonidos.cargar('Z_Nightfall.wav')
sonido_nivel_2 = pilas.sonidos.cargar('Z_Just_Ad_Nauseam.wav')
sonido_del_final = pilas.sonidos.cargar('Z_Know_Your_Enemie.wav')

##############################
## ---------------Mis Personajes--------------- ##
##############################
class Chief(pilasengine.actores.Actor):
    
    def iniciar(self):
        self.imagen = 'Jefe.png'
        self.x = -285
        self.y = -210
        self.escala = 0.05
        self.radio_de_colision = 25
        self.aprender("puedeexplotar")
        self.aprender("disparar", municion = 'Municion')
        
    def actualizar(self):
        if pilas.control.izquierda:
            self.x -= 5
        if pilas.control.derecha:
            self.x += 5
        if pilas.control.abajo:
            self.y -= 5
        if pilas.control.arriba:
            self.y += 5
        if self.x >= 250:
            self.x = 250
        if self.x <= -285:
            self.x = -285    
        if self.y >= 220:
            self.y = 220
        if self.y <= -210:
            self.y = -210
            
class ChiefSuperior(pilasengine.actores.Actor):
    
    def iniciar(self):
        self.imagen = 'Jefe.png'
        self.x = -285
        self.y = -210
        self.escala = 0.05
        self.radio_de_colision = 25
        self.aprender("puedeexplotar")
        self.aprender("disparar", municion = 'Municion')
        
    def actualizar(self):
        if pilas.control.izquierda:
            self.x -= 5
        if pilas.control.derecha:
            self.x += 5
        if pilas.control.abajo:
            self.y -= 5
        if pilas.control.arriba:
            self.y += 5
        if self.x > 80:
            self.x = -285
        if self.x <= -285:
            self.x = -285    
        if self.y >= 220:
            self.y = 220
        if self.y <= -210:
            self.y = -210
                                                           
class Plus(pilasengine.actores.Actor):
    
    def iniciar(self):
        self.imagen = pilas.imagenes.cargar('Mejora.png')
        self.radio_de_colision = 20
        self.escala = 0.20
        self.x = 100
        self.y = random.randint(-100,100)
        self.pilas.utils.interpolar(self, 'x', -365, duracion=5, tipo='gradual')
        if self.x == -300:
            self.eliminar()

class ChiefPlus(pilasengine.actores.Actor):
    
    def iniciar(self):
        self.imagen = 'JefeSPNRk.png'
        self.x = self.x
        self.y = self.y
        self.escala = 0.05
        self.radio_de_colision = 25
        self.aprender("puedeexplotar")
        self.aprender("disparar", municion = 'Cohete')
            
class DestructorPlus(pilasengine.actores.ActorInvisible):
    
    def iniciar(self):
        self.x = 300
        self.barraPP = pilas.actores.Energia(50,225,progreso=100, ancho=500, alto=10, color_relleno = pilasengine.colores.verde)
            
    def actualizar(self):
        self.barraPP.progreso=self.barraPP.progreso - 1
        if self.barraPP.progreso==0:
            self.x = 0
            self.barraPP.eliminar()
            self.figura_de_colision = pilas.fisica.Rectangulo(0, 0, 666, 666, sensor=True, dinamica=False)
                                                           
class Municion(pilasengine.actores.Actor):
    
    def iniciar(self):
        self.imagen = 'Sniper.png'
        self.figura_de_colision = pilas.fisica.Rectangulo(-285, -210, 17, 45, sensor=True, dinamica=False)
            
    def actualizar(self):
        self.figura_de_colision.x = self.x
        self.figura_de_colision.y = self.y
        if self.x > 300:
            self.eliminar()
            self.figura_de_colision.eliminar()

class Cohete(pilasengine.actores.Actor):
    
    def iniciar(self):
        self.imagen = 'SPNRk.png'
        self.aprender("puedeexplotar")
        self.figura_de_colision = pilas.fisica.Rectangulo(-285, -210, 17, 45, sensor=True, dinamica=False)
            
    def actualizar(self):
        self.figura_de_colision.x = self.x
        self.figura_de_colision.y = self.y
        if self.x > 300:
            self.eliminar()
            self.figura_de_colision.eliminar()

class Elite(pilasengine.actores.Actor):
    
    def iniciar(self):
        self.imagen = 'Enemigo_Elite.png'
        self.escala = 0.07
        self.y = 270
        self.x = random.randint(-300, 300)
        self.radio_de_colision = 25
            
    def actualizar(self):
        self.y -= 5
        if self.y <= -230:
            self.eliminar()
            
class AtrioxBoss(pilasengine.actores.Actor):
    
    def iniciar(self):
        self.imagen = 'Atriox.png'
        self.escala = 0.40
        self.x = 215
        self.y = -50
        self.figura_de_colision = pilas.fisica.Rectangulo(self.x, self.y, 215, 450, sensor=True, dinamica=False)
   
class BansheeBoss(pilasengine.actores.Actor):
                         
    def iniciar(self):
        self.imagen = pilas.imagenes.cargar('Banshee.png')
        self.radio_de_colision = 35
        self.escala = 0.1
        self.x = 195
        self.y = random.randint(-200, 255)
        self.aprender( pilas.habilidades.PuedeExplotarConHumo )
        self.pilas.utils.interpolar(self, 'x', -375, duracion=1, tipo='lineal')
        self.pilas.utils.interpolar(self, 'y', random.randint(-300, 300), duracion=1, tipo='lineal')
            
    def actualizar(self):   
        if self.x <= -365:
            self.eliminar()
            
class Grunt(pilasengine.actores.Actor):
    
    def iniciar(self):
        self.imagen = 'Puntos_Grunt.png'
        self.escala = 0.05
        self.radio_de_colision = 17
        self.aprender( pilas.habilidades.PuedeExplotarConHumo )
        self.izquierda = 300
        self.y = random.randint(-210,50)
        
    def actualizar(self):
        self.x-=5
        if self.x < -300:
            self.eliminar()   
        
##########################
## ---------------Botones--------------- ##
##########################
class Boton_Menu(pilasengine.actores.Actor):
    
    def iniciar(self):
        self.imagen = 'Casco_Mark.png'
        self.x = -280
        self.y = 180
        reiniciar_texto = pilas.interfaz.Boton("Volver al Menu")
        reiniciar_texto.conectar(self.escena_menu)
        reiniciar_texto.x = -265
        reiniciar_texto.y = 220
        self.cuando_hace_click = self.escena_menu
        
    def escena_menu(self):
        sonido_del_final.detener()
        self.pilas.escenas.MenuInicio()
        
class Boton_Nivel_1(pilasengine.actores.Actor):
    
    def iniciar(self):
        self.imagen = 'Casco_Chief.jpg'
        self.x = 0
        self.y = -30
        self.escala = 0.25
        reiniciar_texto = pilas.interfaz.IngresoDeTexto("     Click en el icono para iniciar o reiniciar.")
        reiniciar_texto.x = 0
        reiniciar_texto.y = -115
        self.cuando_hace_click = self.escena_inicial
        
    def escena_inicial(self):
        sonido_menu.detener()
        sonido_del_final.detener()
        self.pilas.escenas.Nivel_1()
        
class Boton_Nivel_2(pilasengine.actores.Actor):
    
    def iniciar(self):
        self.imagen = 'Casco_Chief.jpg'
        self.x = 0
        self.y = -30
        self.escala = 0.25
        reiniciar_texto = pilas.interfaz.IngresoDeTexto("     Click en el icono para iniciar o reiniciar.")
        reiniciar_texto.x = 0
        reiniciar_texto.y = -115
        self.cuando_hace_click = self.escena_inicial
        
    def escena_inicial(self):
        sonido_del_final.detener()
        self.pilas.escenas.Nivel_2()

class Boton_Info(pilasengine.actores.Actor):
     
    def iniciar(self):
        self.imagen = 'Casco_Mark.png'
        self.x = -280
        self.y = 180
        reiniciar_texto = pilas.interfaz.Boton("Informacion")
        reiniciar_texto.conectar(self.escena_info)
        reiniciar_texto.x = -270
        reiniciar_texto.y = 220
        self.cuando_hace_click = self.escena_info
        
    def escena_info(self):
        sonido_menu.reproducir(repetir = True)
        self.pilas.escenas.Info()
                             
###########################
## ---------------Escenarios--------------- ##
###########################
class MenuInicio(pilasengine.escenas.Escena):
    
    def iniciar(self):   
        fondo_inicio = pilas.fondos.Fondo()
        fondo_inicio.imagen = pilas.imagenes.cargar('Menu.jpg')
        fondo_inicio.x = 75
        fondo_inicio.escala = 0.65
        self.boton()
        
    def boton(self):
        pilas.actores.Boton_Nivel_1()    
        pilas.actores.Boton_Info()

class Info(pilasengine.escenas.Escena):
    
    def iniciar(self):
        fondo_info = pilas.fondos.Fondo()
        fondo_info.imagen = pilas.imagenes.cargar('Eclipse.png')
        fondo_info.x = 40
        fondo_info.escala = 0.85
        textoT = pilas.interfaz.IngresoDeTexto("                       TIBERPLANOIBE")
        textoT.y = 225
        texto = pilas.actores.Texto("Todo el contenido grafico y auditivo de\neste juego ha sido obtenido de la popular\nsaga \"Halo\". Nada de este material es de\nmi autoria.\nPor otro lado, todo el codigo ha sido\nescrito por mi, usando esta herramienta\ndenominada \"Pilas-engine\".\nAtte. Danilo A. Ochoa Hidalgo.")
        texto.x = 70
        texto.y = -100
        self.boton()
        
    def boton(self):
        pilas.actores.Boton_Menu()
              
class Nivel_1(pilasengine.escenas.Escena):

    def iniciar(self):
        global puntos
        sonido_nivel_1.reproducir(repetir = True)
        homunculus = pilas.fondos.Fondo()
        homunculus.imagen = pilas.imagenes.cargar('Fondo.jpg')
        homunculus.escala = 0.45
        texto = pilas.actores.Texto("Debes conseguir 100:")
        texto.x = 0
        texto.y = 225
        self.puntaje = self.pilas.actores.Puntaje(150, 225, color=pilas.colores.blanco)
        self.puntaje.definir(puntos)
        self.pilas.actores.Chief()
         
        self.pilas.tareas.siempre(0.5,self.crear_baneador)
        self.pilas.tareas.siempre(1,self.crear_chupa_pitos)
        
        self.pilas.colisiones.agregar('Chief','Elite', self.cuando_elite_toca)
        self.pilas.colisiones.agregar('Municion','Grunt', self.cuando_municion_toca)

    def crear_baneador(self):
        self.pilas.actores.Elite()
    def crear_chupa_pitos(self):
        self.pilas.actores.Grunt()

    def cuando_elite_toca(self, chief, elite):
        chief.eliminar()
        self.puntaje = 0
        if self.puntaje == 0:
            self.pilas.escena_actual().tareas.eliminar_todas()
            sonido_nivel_1.detener()
            self.pilas.escenas.Perdedor()
    
    def cuando_municion_toca(self, municion, grunt):
        global puntos
        grunt.eliminar() 
        puntos += 5
        self.puntaje.aumentar(5)
        if puntos == 100:
                self.pilas.escena_actual().tareas.eliminar_todas()
                sonido_nivel_1.detener()
                self.pilas.escenas.Nivel_2()

class Nivel_2(pilasengine.escenas.Escena):

    def iniciar(self):
        sonido_nivel_2.reproducir(repetir = True)
        homunculus = pilas.fondos.Fondo()
        homunculus.imagen = pilas.imagenes.cargar('Fondox2.jpg')
        homunculus.escala = 0.45
        self.barraP = pilas.actores.Energia(-260,225,progreso=100, ancho=100, alto=20, color_relleno = pilasengine.colores.verde)
        self.barraZ = pilas.actores.Energia(0,-225,progreso=100, ancho=500, alto=20, color_relleno = pilasengine.colores.verde)
        self.pilas.actores.ChiefSuperior()
        self.pilas.actores.AtrioxBoss()
        self.pilas.actores.Plus() 
        
        self.pilas.tareas.siempre(0.5,self.ban)
        self.pilas.tareas.siempre(15,self.crear_mejora)
        
        self.pilas.colisiones.agregar('ChiefSuperior','Plus', self.cuando_toca_plus)
        self.pilas.colisiones.agregar('Cohete','AtrioxBoss', self.cuando_cohete_toca_atriox)
        self.pilas.colisiones.agregar('Municion','AtrioxBoss', self.cuando_municion_toca_atriox)
        self.pilas.colisiones.agregar('ChiefSuperior','BansheeBoss', self.cuando_toca_ban)
        self.pilas.colisiones.agregar('ChiefPlus','DestructorPlus', self.cuando_plus_termina)
         
    def destruye_plus(self):
        self.pilas.actores.DestructorPlus()
    def crear_mejora(self):
        self.pilas.actores.Plus()    
    def ban(self):
        self.pilas.actores.BansheeBoss()  
                
    def cuando_toca_plus(self, puck, plus):
        plus.eliminar()
        puck.eliminar()
        self.pilas.actores.ChiefPlus()
        self.pilas.actores.DestructorPlus()
        
    def cuando_plus_termina(self, pplus, destructor):
        pplus.eliminar()
        destructor.eliminar()
        self.pilas.actores.ChiefSuperior()
        self.barraP.progreso=self.barraP.progreso + 20
     
    def cuando_cohete_toca_atriox(self, cohete, atrioxboss):
        cohete.eliminar()
        self.barraZ.progreso=self.barraZ.progreso - 2
                                   
    def cuando_municion_toca_atriox(self, municion, atrioxboss):
        municion.eliminar()
        self.barraZ.progreso=self.barraZ.progreso - 0.1
        if self.barraZ.progreso<=200:
            self.barraZ.color_relleno=pilasengine.colores.amarillo
        if self.barraZ.progreso<=100:
            self.barraZ.color_relleno=pilasengine.colores.naranja
        if self.barraZ.progreso<=50:
            self.barraZ.color_relleno=pilasengine.colores.rojo
        if self.barraZ.progreso<=0:
            self.pilas.escena_actual().tareas.eliminar_todas()
            sonido_nivel_2.detener()
            self.pilas.escenas.Ganador()

    def cuando_toca_ban(self, chief, ban):
        ban.eliminar()
        self.barraP.progreso=self.barraP.progreso - 20
        if self.barraP.progreso<=70:
            self.barraP.color_relleno=pilasengine.colores.amarillo
        if self.barraP.progreso<=50:
            self.barraP.color_relleno=pilasengine.colores.naranja
        if self.barraP.progreso<=30:
            self.barraP.color_relleno=pilasengine.colores.rojo
        if self.barraP.progreso<=0:
            self.pilas.escena_actual().tareas.eliminar_todas()
            sonido_nivel_2.detener()
            self.pilas.escenas.Perdedor_x2()

class Ganador(pilasengine.escenas.Escena):
    
    def iniciar(self):
        sonido_del_final.reproducir(repetir = True)
        fondo_ganador = pilas.fondos.Fondo()
        fondo_ganador.imagen = pilas.imagenes.cargar('Ganar.jpg')
        fondo_ganador.escala = 0.5
        fondo_ganador.x = -150
        texto = pilas.interfaz.Boton("Luego de la caida de \"Atriox\" el Jefe Maestro")
        texto1 = pilas.interfaz.Boton("se encontro perdido en el espacio.")
        texto2 = pilas.interfaz.Boton("Como nadie logro dar con su paradero")
        texto3 = pilas.interfaz.Boton("la UNSC lo declaro como desaparecido en combate.")
        texto.y = 100
        texto1.y = 40
        texto2.y = -20
        texto3.y = -80
        pilas.actores.Boton_Menu()
        
class Perdedor(pilasengine.escenas.Escena):
    
    def iniciar(self):
        global puntos
        puntos = 0
        sonido_del_final.reproducir()
        fondo_perdedor = pilas.fondos.Fondo()
        fondo_perdedor.imagen = pilas.imagenes.cargar('Perder.jpg')
        fondo_perdedor.escala = 1.5
        texto = pilas.interfaz.Boton("Luego de la caida del Jefe Maestro,")
        texto1 = pilas.interfaz.Boton("y sin nadie que pudiera proteger,")        
        texto2 = pilas.interfaz.Boton("la Tierra fue arrasada hasta convertirse en polvo.")
        texto3 = pilas.interfaz.Boton("Paz en la tumba de Jhon-117") 
        texto.x = 0
        texto.y = 180
        texto1.x = 0
        texto1.y = 140
        texto2.x = 0
        texto2.y =100
        texto3.x = 0
        texto3.y = -180
        self.pilas.actores.Boton_Nivel_1()
        self.pilas.actores.Boton_Menu()

class Perdedor_x2(pilasengine.escenas.Escena):
    
    def iniciar(self):
        global puntos
        puntos = 0
        sonido_del_final.reproducir()
        fondo_perdedor = pilas.fondos.Fondo()
        fondo_perdedor.imagen = pilas.imagenes.cargar('Perderx2.jpg')
        fondo_perdedor.escala = 1.3
        fondo_perdedor.x = 180
        fondo_perdedor.y = -80
        texto = pilas.interfaz.Boton("Con Atriox al mando de los \"Desterrados\",")
        texto1 = pilas.interfaz.Boton("y sin nadie en pie para proteger nuestro hogar,")        
        texto2 = pilas.interfaz.Boton("nuestro planeta se vio consumido por la ambicion del Brute.") 
        texto3 = pilas.interfaz.Boton("Ahora nuestro legado ha llegado a su fin.") 
        texto.x = 0
        texto.y = 180
        texto1.x = 0
        texto1.y = 140
        texto2.x = 0
        texto2.y =100
        texto3.x = 0
        texto3.y = -180
        self.pilas.actores.Boton_Nivel_2()
        self.pilas.actores.Boton_Menu()
        
#############################
## ---------------Vinculaciones--------------- ##
#############################
pilas.escenas.vincular(MenuInicio)
pilas.escenas.vincular(Info)
pilas.escenas.vincular(Nivel_1)
pilas.escenas.vincular(Nivel_2)
pilas.escenas.vincular(Ganador)
pilas.escenas.vincular(Perdedor)
pilas.escenas.vincular(Perdedor_x2)

pilas.actores.vincular(Chief)
pilas.actores.vincular(ChiefSuperior)
pilas.actores.vincular(Plus)
pilas.actores.vincular(ChiefPlus)
pilas.actores.vincular(DestructorPlus)
pilas.actores.vincular(Municion)
pilas.actores.vincular(Cohete)
pilas.actores.vincular(Elite)
pilas.actores.vincular(AtrioxBoss)
pilas.actores.vincular(BansheeBoss)
pilas.actores.vincular(Grunt)
pilas.actores.vincular(Boton_Menu)
pilas.actores.vincular(Boton_Nivel_1)
pilas.actores.vincular(Boton_Nivel_2)
pilas.actores.vincular(Boton_Info)

pilas.escenas.MenuInicio()

pilas.ejecutar()