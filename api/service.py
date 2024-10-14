class GS1Service:
    
    def __init__(self):
        self.final_states = {58, 59, 60}  
        self.transitions = {
            (0, '('): 1,
            (1, '0'): 2,
            (2, '1'): 3,
            (3, ')'): 4,
            (4, '0-9'): 5,
            (5, '0-9'): 6,
            (6, '0-9'): 7,
            (7, '0-9'): 8,
            (8, '0-9'): 9,
            (9, '0-9'): 10,
            (10, '0-9'): 11,
            (11, '0-9'): 12,
            (12, '0-9'): 13,
            (13, '0-9'): 14,
            (14, '0-9'): 15,
            (15, '0-9'): 16,
            (16, '0-9'): 17,
            (17, '0-9'): 18,
            (18, '('): 19,
            (19, '1'): 20,
            (20, '7'): 21,
            (21, ')'): 22,
            (22, "0, 2, 4, 6, 8"): 23,  
            (22, "1, 3, 5, 7, 9"): 24,  
            (23, "0, 4, 8"): 25,     
            (23, "1, 2, 3, 5, 6, 7, 9"): 26,  
            (24, "2, 6"): 25,      
            (24, "0, 1, 3, 4, 5, 7, 8, 9"): 26,  
            (25, '0'): 27,
            (25, '1'): 28,
            (26, '1'): 28,
            (26, '0'): 29,
            (28, "0, 2"): 30,
            (28, '1'): 32,
            (27, "1, 3, 5, 7, 8"): 30,
            (27, '2'): 31,
            (27, "4, 6, 9"): 32,
            (29, "1, 3, 5, 7, 8"): 30,
            (29, "4, 6, 9"): 32,
            (29, '2'): 33,
            (30, '0'): 34,
            (30, '3'): 35,
            (30, "1, 2"): 36,
            (31, '0'): 34,
            (31, "1, 2"): 36,
            (32, '0'): 34,
            (32, "1, 2"): 36,
            (32, '3'): 37,
            (33, '0'): 34,
            (33, '1'): 36,
            (33, '2'): 38,
            (34, '1, 2, 3, 4 ,5, 7, 8, 9'): 39,
            (35, '0, 1'): 40,
            (36, '0, 1, 2, 3, 4, 5, 6, 7, 8, 9 '): 41,
            (37, '0'): 42,
            (38, '0, 1, 2, 3, 4, 5, 6, 7, 8'): 43,
            (39, '('): 44,
            (40, '('): 44,
            (41, '('): 44,
            (42, '('): 44,
            (43, '('): 44,
            (44, '1'): 45,
            (45, '0'): 46,
            (46, ')'): 47,
            (47, 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'): 48,
            (48, 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'): 49,
            (49, 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'): 50,
            (50, '0, 1, 2, 3, 4, 5, 6, 7, 8, 9 '): 51,
            (51, '0, 1, 2, 3, 4, 5, 6, 7, 8, 9 '): 52,
            (52, '0, 1, 2, 3, 4, 5, 6, 7, 8, 9 '): 53,
            (53, '('): 54,
            (54, '3'): 55,
            (55, '0'): 56,
            (56, ')'): 57,
            (57, "1, 2, 3, 4, 5, 6, 7, 8, 9 , e"): 58,  # Estado final
            (58, "0, 1, 2, 3, 4, 5, 6, 7, 8, 9 , e"): 59,  # Estado final
            (58, '0, 1, 2, 3, 4, 5, 6, 7, 8, 9 '): 60,     # Estado final
        }
        
        self.add_range_transitions()

    def add_range_transitions(self):
        for i in range(10):
            self.transitions[(4, str(i))] = 5
            self.transitions[(5, str(i))] = 6
            self.transitions[(6, str(i))] = 7
            self.transitions[(7, str(i))] = 8
            self.transitions[(8, str(i))] = 9
            self.transitions[(9, str(i))] = 10
            self.transitions[(10, str(i))] = 11
            self.transitions[(11, str(i))] = 12
            self.transitions[(12, str(i))] = 13
            self.transitions[(13, str(i))] = 14
            self.transitions[(14, str(i))] = 15
            self.transitions[(15, str(i))] = 16
            self.transitions[(16, str(i))] = 17
            self.transitions[(17, str(i))] = 18
            
        for i in range(1, 10): 
            self.transitions[(34, str(i))] = 39
            self.transitions[(34, str(i))] = 40
            self.transitions[(34, str(i))] = 41
            self.transitions[(39, '0-9')] = 59  # Estado final
            self.transitions[(41, '0-9')] = 60  # Estado final

    def validate_gs1_code(self, code: str) -> dict:
        current_state = 0 
        year, month, day = '', '', ''  
        is_date_segment = False 

        for char in code:
            found_transition = False
            for (state, input_char), next_state in self.transitions.items():
                if state == current_state:
                    if char in input_char.replace(" ", "").split(','):
                        current_state = next_state
                        found_transition = True

                        if current_state == 17: 
                            is_date_segment = True
                        break

            if not found_transition:
                print(f"Transición no válida: estado={current_state}, carácter='{char}'")
                return {"code": code, "is_valid": False, "message": "Transición no válida"}

            if is_date_segment:
                if char.isdigit():
                    if len(year) < 2:
                        year += char  
                    elif len(month) < 2:
                        month += char  
                    elif len(day) < 2:
                        day += char  
                    if len(year) == 2 and len(month) == 2 and len(day) == 2:
                        if not self.validate_date(year, month, day):
                            print(f"Fecha inválida: {year}-{month}-{day}")
                            return {"code": code, "is_valid": False, "message": "Fecha inválida"}
                        year, month, day = '', '', ''
                        is_date_segment = False  

        if current_state in self.final_states:
            return {"code": code, "is_valid": True, "message": "Código válido"}
        else:
            print(f"Código inválido: estado final={current_state}")
            return {"code": code, "is_valid": False, "message": "Código inválido"}

    def validate_date(self, year: str, month: str, day: str) -> bool:
        if month == '02':
            if day > '29':
                return False
            elif day == '29':
                return (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0)
            return True
        elif month in ['04', '06', '09', '11'] and day > '30':
            return False
        return True


# Ejemplo de uso
gs1_service = GS1Service()
codigo_a_validar = "(01)12345678901234(17)000229(10)LOT156(30)5"
resultado = gs1_service.validate_gs1_code(codigo_a_validar)
print(resultado)
