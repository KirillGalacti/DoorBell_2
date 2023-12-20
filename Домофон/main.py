import serial
import json

# Инициализация последовательного порта
ser = serial.Serial('COM3', 19200)  # Замените 'COM3' на ваш последовательный порт

def read_json_data():
    # Чтение данных из JSON файла
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

def main():
    try:
        while True:
            print("Ожидание данных...")
            uid = ser.readline().decode().strip()
            print("UID жильца:", uid)
            
            # Чтение данных из JSON файла
            data = read_json_data()
            
            if uid in data:
                print("UID жильца найден, он есть в базе дома.", data[uid])
                
                # Ваш код для управления реле здесь
                
            else:
                print("UID не найден, такого жильца нет в базе дома.")

    except KeyboardInterrupt:
        ser.close()

if __name__ == "__main__":
    main()