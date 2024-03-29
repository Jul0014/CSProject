from backend.models.post_connection_pool import PostgreSQLPool

class PersonaModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_persona(self, persona_dni):    
        params = {'dni' : persona_dni}      
        rv = self.post_pool.execute("SELECT * from personas where dni=%(dni)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5],  'password': result[6]}
            data.append(content)
            content = {}
        return data

    def get_personas(self):  
        rv = self.post_pool.execute("SELECT * from personas")  
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5],  'password': result[6]}
            data.append(content)
            content = {}
        return data

    def create_persona(self, dni, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, correo_institucional, password):    
        data = {
            'dni' : dni,
            'nombres' : nombres,
            'apellido_paterno': apellido_paterno,
            'apellido_materno': apellido_materno,
            'fecha_nacimiento': fecha_nacimiento,
            'correo_institucional': correo_institucional,
            'password': password
        }  
        query = """insert into personas (dni, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, correo_institucional, password) 
            values (%(dni)s, %(nombres)s, %(apellido_paterno)s, %(apellido_materno)s, %(fecha_nacimiento)s, %(correo_institucional)s, %(password)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)   
        return data

    def update_persona(self, dni, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, correo_institucional, password):    
        data = {
            'dni' : dni,
            'nombres' : nombres,
            'apellido_paterno': apellido_paterno,
            'apellido_materno': apellido_materno,
            'fecha_nacimiento': fecha_nacimiento,
            'correo_institucional': correo_institucional,
            'password': password
        }  
        query = """update personas set nombres = %(nombres)s, apellido_paterno = %(apellido_paterno)s,
                    apellido_materno = %(apellido_materno)s, fecha_nacimiento = %(fecha_nacimiento)s,
                    correo_institucional = %(correo_institucional)s, password = %(password)s where dni = %(dni)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_persona(self, dni):    
        params = {'dni' : dni}      
        query = """delete from personas where dni = %(dni)s"""    
        self.post_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 

"""if __name__ == "__main__":    
    pm = PersonaModel()     
    print(pm.create_persona('71218699', 'Rebeca', 'del Río', 'Santos', '12/14/1982', 'rdelrios@universidad.edu.pe', '12345')) """

