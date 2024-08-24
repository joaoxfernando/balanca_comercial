import wget
import dotenv
import os

dotenv.load_dotenv('.env')
save_path_dir = os.getenv('PATH_DIR')
save_path_dir = r'{}'.format(save_path_dir)

def get_files(year):
    files = [f'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_{year}.csv', f'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/IMP_{year}.csv']

    for file in files:
        print(f'Baixando o arquivo {os.path.basename(file)}, isso pode levar alguns segundos/minutos... não feche a aplicação!')
        if os.path.basename(file).find('EXP') >= 0:
            filename = save_path_dir+'Exportação/'+os.path.basename(file)
            if os.path.exists(filename):
                os.remove(filename) 
            wget.download(file, os.path.join(save_path_dir, 'Exportação/'))
        else:
            filename = save_path_dir+'Importação/'+os.path.basename(file)
            if os.path.exists(filename):
                os.remove(filename)
            wget.download(file, save_path_dir+'Importação/')
        print(f'\nArquivo {os.path.basename(file)} salvo com sucesso!')
    return None