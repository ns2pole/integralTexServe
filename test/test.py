from bottle import run, route, template, static_file, error, redirect
import os
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

@route('/pdf/<city_name>')
def pdfTest(city_name):
    f = open('./myfile.tex', 'w', encoding='UTF-8')
    datalist = ['\documentclass{jarticle}\n', '\\begin{document}\n', '$f(x)=e^{x^2}$', city_name, 'それではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまた\n', '\end{document}\n']
    f.writelines(datalist)
    f.close()
    os.system('platex ./myfile.tex')
    os.system('dvipdfm ./myfile.dvi')
    os.system('open ./myfile.pdf')
    return "通信に成功しました。"
    
@route('/static/pdf/<filename>')
def send_img(filename):
    return static_file(filename, root= STATIC_DIR + "/pdf")

@error(404)
def error404(error):
    return 'このページは存在しません。'

if __name__ == "__main__":
    run(host='localhost', port=8080, reloader=True, debug=True)