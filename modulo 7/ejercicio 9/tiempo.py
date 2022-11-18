import time

actual = time.localtime().tm_hour
inicio= 8
final = 18
def main():
    if inicio >= actual <= final:
        rest = final - inicio
        print("estas trabajando te quedan: ", rest, " h, para teminar")
    else:
        print("ya terminaste las horas laborables, estas descansando!!")

if __name__ == '__main__':
    main()

