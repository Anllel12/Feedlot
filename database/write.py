from . import ConnectionAbs

class Write:

    def __init__(self, connection: ConnectionAbs):
        self.connection_instance = connection  # Crear una instancia de la clase de conexión
        self.connection = self.connection_instance.connect()  # Conectar a la base de datos
        self.cursor = self.connection.cursor()

    def insert_provider(self, provider):
        try:
            query = "INSERT INTO provider (name, cif) VALUES (%s, %s)"
            self.cursor.execute(query, (provider.get_name(), provider.get_cif()))
            self.connection.commit()
            print("Provider inserted successfully.")
        except Exception as e:
            print(f"Error inserting provider: {e}")

    def insert_guide(self, guide):
        try:
            query = """INSERT INTO guide (num_guide, cost, price_males, price_females, date, num_male, num_female, kg_male, kg_female, provider) 
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            self.cursor.execute(query, (guide.get_num_guide(), guide.get_cost(), guide.get_price_males(),
                                        guide.get_price_females(), guide.get_date(), guide.get_num_male(),
                                        guide.get_num_female(), guide.get_kg_male(), guide.get_kg_female(),
                                        guide.get_provider()))
            self.connection.commit()
            print("Guide inserted successfully.")
        except Exception as e:
            print(f"Error inserting guide: {e}")

    def insert_calf(self, calf):
        try:
            query = "INSERT INTO calf (crotal, weight, gender, nationality) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query,
                                (calf.get_crotal(), calf.get_weight(), calf.get_gender(), calf.get_nationality()))
            self.connection.commit()
            print("Calf inserted successfully.")
        except Exception as e:
            print(f"Error inserting calf: {e}")

    def insert_belong(self, belong):
        try:
            query = "INSERT INTO belong (num_guide, num_crotal) VALUES (%s, %s)"
            self.cursor.execute(query, (belong.get_num_guide(), belong.get_num_crotal()))
            self.connection.commit()
            print("Belong inserted successfully.")
        except Exception as e:
            print(f"Error inserting belong: {e}")

    def disconnect(self):
        self.connection_instance.disconnect()  # Llama al método disconnect() ya implementado en connection_abs