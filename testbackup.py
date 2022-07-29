import os
f = open('myfile.tex', 'w', encoding='UTF-8')
datalist = ['\documentclass{jarticle}\n', '\\begin{document}\n', '$f(x)=e^{x^2}$', 'それではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまたそれではまた\n', '\end{document}\n']
f.writelines(datalist)
f.close()
os.system('platex ./myfile.tex')
os.system('dvipdfm ./myfile.dvi')
os.system('open ./myfile.pdf')