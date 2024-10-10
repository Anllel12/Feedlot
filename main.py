from database.localconnection import LocalConnection
from database.write import Write

from object.belong import Belong
from object.calf import Calf
from object.guide import Guide
from object.provider import Provider

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Pasar la clase local_connection directamente a Write
    write_manager = Write(LocalConnection())

    # Crear los objetos correspondientes
    provider = Provider(id=None, name="Provider One", cif="B12345678")
    guide = Guide(num_guide=2, cost=100.5, price_males=50.0, price_females=45.0, date="2024-10-10",
                  num_male=10, num_female=12, kg_male=300.0, kg_female=280.0, provider=1)
    calf = Calf(crotal=1234, weight=350.0, gender='Male', nationality='ES')
    belong = Belong(num_guide=1, num_crotal=12345)

    # Insertar los objetos en la base de datos utilizando la conexión abstracta
    write_manager.insert_provider(provider)
    write_manager.insert_guide(guide)
    write_manager.insert_calf(calf)
    write_manager.insert_belong(belong)

    # Desconectar de la base de datos cuando se hayan terminado las operaciones utilizando la función de connection_abs
    write_manager.disconnect()
