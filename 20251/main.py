from coche import Coche
from motor import Motor
from llanta import Llanta


def main():
    tsuru = Coche(True)
    camaro = Coche()

    print(tsuru)

    tsuru.cambiarMarcha(2)

    for i in range(1, 9):
        tsuru.acelerar()

    tsuru.cambiarMarcha(3)
    tsuru.frenar()

    print(f"{tsuru}")
    print(camaro)

    print("=====")

    motor = Motor("ABC123")
    tsuru.encender(motor)

    fi = Llanta("FI")
    fd = Llanta("FD")

    fi.inflar(30)
    fd.inflar()

    tsuru.agregarLlanta(fi)
    tsuru.agregarLlanta(fd)


if __name__ == '__main__':
    main()
