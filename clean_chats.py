import os
path =  r'C:\Users\sande\PycharmProjects\chatbot\chatbot_datasets'
for _file in os.listdir(path):
    if _file.endswith(''):
        f = open(os.path.join(path,_file),encoding='utf8')
        lines = f.readlines()
        f.close()
        f = open(os.path.join(path,_file), 'w',encoding='utf8')
        for line in lines:
            f.write(line[29:])
        f.close()