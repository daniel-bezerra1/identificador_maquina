import subprocess
import hashlib
import pyperclip
import time

def get_bios_serial_windows():
    try:
        result = subprocess.run(['wmic', 'bios', 'get', 'serialnumber'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8').strip().split('\n')[-1]
        return output
    except Exception as e:
        return None

def get_motherboard_uuid_windows():
    try:
        result = subprocess.run(['wmic', 'baseboard', 'get', 'serialnumber'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8').strip().split('\n')[-1]
        return output
    except Exception as e:
        return None

def generate_unique_id():
    bios_serial = get_bios_serial_windows()
    motherboard_uuid = get_motherboard_uuid_windows()
    if not bios_serial or not motherboard_uuid:
        raise Exception("Não foi possível obter o unique id")
    unique_string = bios_serial + motherboard_uuid
    return hashlib.sha256(unique_string.encode()).hexdigest()

if __name__ == "__main__":
    try:
        unique_id = generate_unique_id()
        print(f"Identificador único: {unique_id}")

        pyperclip.copy(unique_id)
        print("Identificador copiado para a área de transferência.")

        time.sleep(10)
    except Exception as e:
        print(f"Erro: {e}")


