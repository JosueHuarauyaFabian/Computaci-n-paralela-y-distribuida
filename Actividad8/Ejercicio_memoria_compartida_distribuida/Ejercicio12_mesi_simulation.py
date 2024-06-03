class CacheLine:
    def __init__(self):
        self.state = 'I'  # Estado inicial es Inválido
        self.value = None

    def read(self):
        if self.state == 'I':
            # Si está en estado Inválido, debe transicionar a Compartido o Exclusivo (aquí simplificado)
            self.state = 'S'
            print("Transition to Shared")
        elif self.state == 'M':
            print("Read from Modified")
        elif self.state == 'E':
            self.state = 'S'
            print("Transition to Shared from Exclusive")
        return self.value

    def write(self, value):
        if self.state == 'I' or self.state == 'S':
            self.state = 'M'
            print("Transition to Modified")
        elif self.state == 'E':
            self.state = 'M'
            print("Transition to Modified from Exclusive")
        self.value = value

    def get_state(self):
        return self.state

def main():
    cache_line = CacheLine()

    # Simular operación de escritura
    print("Writing value 42")
    cache_line.write(42)
    print(f"State after write: {cache_line.get_state()}")

    # Simular operación de lectura
    print("Reading value")
    value = cache_line.read()
    print(f"State after read: {cache_line.get_state()}")

    # Otra operación de lectura para verificar transición de E a S
    cache_line = CacheLine()
    print("\nSetting to Exclusive and then reading")
    cache_line.state = 'E'  # Forzar estado Exclusivo para prueba
    value = cache_line.read()
    print(f"State after read from Exclusive: {cache_line.get_state()}")

if __name__ == "__main__":
    main()
