from PyQt6 import QtWidgets


app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()


window.resize(900, 500)
window.setMinimumSize(500, 500)
window.setMaximumSize(1000, 1000)


# Complete nosso formulário com informações de um
# usuário. Pense que este seria um formulário de
# registro, onde o usuário vai preencher nome, sobrenome,
# senha, etc.

# formulario do nome
input_nome = QtWidgets.QLineEdit(window)
input_nome.move(10, 10)
input_nome.setPlaceholderText("Digite seu nome aqui")

# formulario do sobrenome
# coomo deixar a caixinha mais larga
input_sobrenome = QtWidgets.QLineEdit(window)
input_sobrenome.move(10, 35)
input_sobrenome.resize(162, 20)
input_sobrenome.setPlaceholderText("Digite seu sobrenome aqui")

# formulario do e-mail
input_email= QtWidgets.QLineEdit(window)
input_email.move(10, 85)
input_email.setPlaceholderText("Digite seu e-mail aqui")

# formulario da senha
input_senha = QtWidgets.QLineEdit(window)
input_senha.move(10, 60)
input_senha.setPlaceholderText("Digite sua senha aqui")




combobox = QtWidgets.QComboBox(window)
combobox.move(10, 105)
combobox.addItems([
    "Python",
    "C++",
    "C#",
    "JavaScript",
    "Java"
])



table = QtWidgets.QTableWidget(window)
table.setEnabled(False)
table.setColumnCount(5)
table.setRowCount(0)
table.setHorizontalHeaderLabels(["Nome", "Sobrenome", "E-mail", "senha", "Cursos"])
table.move(220, 30)
table.resize(550, 400)
table.setStyleSheet("""
    QTableWidget {
        border: 2px solid black;
    }
""")

# # Primeira linha
# table.setItem(0, 0, QtWidgets.QTableWidgetItem(""))
# table.setItem(0, 1, QtWidgets.QTableWidgetItem(""))

# # Segunda linha
# table.setItem(1, 0, QtWidgets.QTableWidgetItem(""))
# table.setItem(1, 1, QtWidgets.QTableWidgetItem(""))

# table.insertRow(table.rowCount())

# Sabendo criar e manipular tabelas, exiba os usuários atualizados 
# sempre que o usuário criar um novo.
# Dica: Crie uma função para re-renderizar a tabela inteira

users= []


def renderTable():
    table.setRowCount(len(users))
    for i in range(len(users)):
        user = users[i]
        table.setItem(i, 0, QtWidgets.QTableWidgetItem(user["nome"]))
        table.setItem(i, 1, QtWidgets.QTableWidgetItem(user["sobrenome"]))
        table.setItem(i, 2, QtWidgets.QTableWidgetItem(user["e-mail"]))
        table.setItem(i, 3, QtWidgets.QTableWidgetItem(user["senha"]))
        table.setItem(i, 4, QtWidgets.QTableWidgetItem(user["cursos"]))



# vinculando os inputs ao clique do butão
def onClick():
    novo_user = {
        "nome": input_nome.text(),
        "sobrenome": input_sobrenome.text(),
        "e-mail": input_email.text(),
        "senha": input_senha.text(),
        "cursos": combobox.currentText(),
    }
    users.append(novo_user)
    renderTable()
    print(users)





button = QtWidgets.QPushButton("Enviar", window)
button.clicked.connect(onClick)
button.move(10, 130)



window.show()
app.exec()

