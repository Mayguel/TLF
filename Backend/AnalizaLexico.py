class AnalizadorLexico:
    def __init__(self):
        self.tokens = []
        self.palabras_reservadas = {
            'sino si': 'Palabra reservada',
            'haz mientras': 'Palabra reservada',
            'rep': 'Palabra reservada',
            'cada': 'Palabra reservada',
            'mientras': 'Palabra reservada',
            'si': 'Palabra reservada',
            'sino': 'Palabra reservada',
            'segun': 'Palabra reservada',
            'caso': 'Palabra reservada',
            'defecto': 'Palabra reservada',
            '¿?': 'Palabra reservada',
            'tipo': 'Palabra reservada',
            'norma': 'Palabra reservada',
            'crea': 'Palabra reservada',
            'ext': 'Palabra reservada',
            'imp': 'Palabra reservada'
        }

        self.operadores = {
            '/+/': 'Operador',
            '/-/': 'Operador',
            '/*/': 'Operador',
            '///': 'Operador',
            '////': 'Operador',
            '/**/': 'Operador',
            '/%/': 'Operador',
            'eq': 'Operador',
            'ne': 'Operador',
            'gt': 'Operador',
            'ge': 'Operador',
            'it': 'Operador',
            'le': 'Operador',
            'y': 'Operador',
            'ou': 'Operador',
            'nel': 'Operador',
            '~~': 'Operador',
            '~+': 'Operador',
            '~-': 'Operador',
            '~x': 'Operador',
            '~/': 'Operador',
            '~%': 'Operador',
            '((': 'Operador',
            '{{': 'Operador',
            '[[': 'Operador',
            '))': 'Operador',
            '}}': 'Operador',
            ']]': 'Operador',
            '.': 'Operador',
            '..': 'Operador',
            '|': 'Operador'
        }

        self.identificadores = {
            '@cls': 'Identificador de Clase'
        }

        self.tipo_dato = {
            'decimal': 'Tipo de dato',
            'doble': 'Tipo de dato',
            'texto': 'Tipo de dato',
            'symbol': 'Tipo de dato'
        }

    def tokenizar(self, codigo):
        self.tokens = []
        token_actual = ''
        i = 0
        linea = 1
        columna = 1

        while i < len(codigo):
            char = codigo[i]
            if char.isspace():
                if char == '\n':
                    linea += 1
                    columna = 1
                else:
                    columna += 1
                i += 1
                continue

            token_identificado = False

            for op in sorted(self.operadores.keys(), key=len, reverse=True):
                if codigo[i:i+len(op)] == op:
                    self.tokens.append((self.operadores[op], op, linea, columna))
                    i += len(op)
                    columna += len(op)
                    token_identificado = True
                    break

            if token_identificado:
                continue

            for pr in sorted(self.palabras_reservadas.keys(), key=len, reverse=True):
                if codigo[i:i+len(pr)] == pr:
                    self.tokens.append((self.palabras_reservadas[pr], pr, linea, columna))
                    i += len(pr)
                    columna += len(pr)
                    token_identificado = True
                    break

            if token_identificado:
                continue

            for td in sorted(self.tipo_dato.keys(), key=len, reverse=True):
                if codigo[i:i+len(td)] == td:
                    self.tokens.append((self.tipo_dato[td], td, linea, columna))
                    i += len(td)
                    columna += len(td)
                    token_identificado = True
                    break

            if token_identificado:
                continue

            # Manejo de identificadores de variable que comienzan con '-'
            if codigo[i] == '-':
                token_actual += codigo[i]
                i += 1
                columna += 1
                while i < len(codigo) and codigo[i].isalnum():
                    token_actual += codigo[i]
                    i += 1
                    columna += 1
                self.tokens.append(('Identificador de Variable', token_actual, linea, columna))
                token_actual = ''
                continue

            # Manejo de identificadores de método que comienzan con 'Met'
            if codigo[i:i+3] == 'Met':
                token_actual += codigo[i:i+3]
                i += 3
                columna += 3
                while i < len(codigo) and codigo[i].isalpha():
                    token_actual += codigo[i]
                    i += 1
                    columna += 1
                self.tokens.append(('Identificador de Metodo', token_actual, linea, columna))
                token_actual = ''
                continue

            while i < len(codigo) and (codigo[i].isalnum() or codigo[i] == '-' or codigo[i] == '@'):
                token_actual += codigo[i]
                i += 1
                columna += 1

            if token_actual:
                if token_actual in self.identificadores:
                    self.tokens.append((self.identificadores[token_actual], token_actual, linea, columna))
                elif token_actual.isdigit():
                    self.tokens.append(('Numero', token_actual, linea, columna))
                elif token_actual.replace('.', '', 1).isdigit():
                    self.tokens.append(('Decimal', token_actual, linea, columna))
                else:
                    self.tokens.append(('Error', token_actual, linea, columna))
                token_actual = ''
            else:
                # Token no reconocido
                self.tokens.append(('Error', codigo[i], linea, columna))
                i += 1
                columna += 1

        return self.tokens


