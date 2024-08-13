from flask import Flask, render_template, redirect, url_for 
  
app = Flask(__name__, template_folder = 'app') 
  
  
@app.route("/") 
def home(): 
    return render_template("index.html") 
  
  
@app.route("/default") 
def default(): 
    return render_template("layout.html") 
  
  
@app.route("/variable") 
def var(): 
    user = "Jason"
    return render_template("variable_example.html", name=user) 
  
  
@app.route("/if") 
def ifelse(): 
    user = "Jason"
    return render_template("if_example.html", name=user) 
  
  
@app.route("/for") 
def for_loop(): 
    names = ['Jason', 'Philip', 'Jaden', 'Jesse'] 
    return render_template("for_example.html", people=names) 
  
  
@app.route("/choice/<pick>") 
def choice(pick): 
    if pick == 'variable': 
        return redirect(url_for('var')) 
    if pick == 'if': 
        return redirect(url_for('ifelse')) 
    if pick == 'for': 
        return redirect(url_for('for_loop')) 
  
  
if __name__ == "__main__": 
    app.run(debug=False) 