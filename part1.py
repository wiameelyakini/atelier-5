class Vecteur2D:
    def __init__(self, a, b):
        self.x = a
        self.y = b
        print('les deux parametres de vecteurs sont: ')
        print("x=", a)
        print("y=", b)


v = Vecteur2D(2, 4)


class Vecteur2D:

    def __init__(self):
        self.vx1 = 2
        self.vy1 = 4
        self.vx2 = 6
        self.vy2 = 8

    def afficher(self):

        print('les deux vecteurs sont: ')
        print('les composants de premiere vecteur est : (',
              self.vx1, ',', self.vy1, ')')
        print('les composants de deuxieme vecteur est : (',
              self.vx2, ',', self.vy2, ')')

    def somme(self):

        print('la somme de ces deux vecteurs est: ')
        self.sommex = self.vx1+self.vx2
        self.sommey = self.vy1+self.vy2
        print('(', self.sommex, ',', self.sommey, ')')


v = Vecteur2D()
v.afficher()
v.somme()


class Rectangle:

    def __init__(self):
        self.L = 4
        self.l = 2
        self.nom = "rectangle"

    # pour afficher les données et le resultat :
    def afficher(self):
        print('la longueur est :', self.L)
        print('la largeur est :', self.l)
        print('le nom est :', self.nom)

    # pour calculer la surface :
    def surface(self):
        self.sur = self.L * self.l
        print('la surface de rectangle est :', self.sur)


class carre(Rectangle):
    def __init__(self):

        self.L = 4
        self.l = 4
        self.nom = "carre"

    def surface(self):
        self.sur = self.L * self.L
        print('la surface du carre est :', self.sur)


R = Rectangle()
R.afficher()
R.surface()
C = carre()
C.afficher()
C.surface()


class point:
    def __init__(self, x=0.0, y=0.0):

        self.ptx = float(x)
        self.pty = float(y)


class segment:
    def __init__(self, x1, y1, x2, y2):

        self.org = point(x1, y1)
        self.ex = point(x2, y2)
        print('segment :')
        print(self.org.px, self.org.py, self.ex.px, self.ex.py)
