from flask import Flask, request, jsonify
from models.tasks import Task
#__name__ = '__main__'
app = Flask(__name__)

'''
PRATICANDO CAMINHOS
@app.route("/")
def hello_word():
    return 'Olá Mundo!'

@app.route("/about")
def about():
    return"Página Sobre"
'''

'''
CRIANDO CRUD
CREATE - CRIA - POST
READ - LER - GET
UPDATE - ATUALIZA - PUT
DELETE - DELETA - DELETE
'''

tasks = []
task_id_control = 1
#CRIA TAREFA
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control#USADO PARA FUNCIONAR A ITERAÇÃO
    data = request.get_json(force=True)# força a leitura como JSON
    new_task = Task(id=task_id_control,title=data['title'], description=data.get('description', ''))
    task_id_control +=1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message":"Nova tarefa criada com sucesso"})
#CHAMA TODA LISTA DE TAREFAS
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": tasks_list,
        "total_tasks" : len(tasks_list)
    }
    return jsonify(output)
#CHAMA TAREFA POR ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message" : "Não foi possivel encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({"message" : "Não foi possivel encontrar atividade"}), 404
    #ID NÃO SE ALTERA POIS PERDERIAMOS O USUARIO DENTRO DA APLICAÇÃO
    data = request.get_json(force=True)
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message" : "Tarefa atualizada com sucesso!"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            print(t)
            task = t
            break#caso não tenha break ele percorrera o laço mesmo ja tendo encontrado

    if task == None:
        return jsonify({"message":"Não foi possivel encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message" : "Tarefa deletado com sucesso"})
'''
PARAMETROS DE ROTA
@app.route('/user/<username>')
def show_user(username):
    print(username)
    print(type(username))
    return username

'''
#APENAS PARA DESENVOLVIMENTO LOCAL
if __name__ == '__main__': 
    app.run(debug=True)
