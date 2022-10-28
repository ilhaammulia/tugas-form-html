from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nama = request.form['nama']
        umur = request.form['umur']
        password = request.form['password']
        jeniskelamin = request.form['jeniskelamin']
        alamat = request.form['alamat']
        hobbies = request.form.getlist('hobbies')
        agama = request.form['agama']
        kode = request.form['kode']
        return render_template('response.html',
                               nama=nama, umur=umur,
                               password=password, jeniskelamin=jeniskelamin,
                               alamat=alamat, hobbies=hobbies,
                               agama=agama, kode=kode)
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
