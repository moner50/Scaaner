from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, '{self.value}')"

# Updated token specifications for C language
token_specs = [
    ('KEYWORD', r'\b(int|float|if|else|for|while|return|void|char|double|break|continue|switch|case|default|do)\b'),
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),
    ('NUMBER', r'\d+(\.\d*)?'),
    ('ASSIGN', r'='),
    ('RELOP', r'(==|!=|<=|>=|<|>)'),
    ('OP', r'(\+{1,2}|-{1,2}|\*|/|%|&&|\|\||!|&|\||\^)'),
    ('SEMICOLON', r';'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('COMMA', r','),
    ('COLON', r':')
]

token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specs)

def scan(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group(kind)
        tokens.append(Token(kind, value))
    return tokens

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/scan', methods=['POST'])
def scan_code():
    data = request.json
    code = data.get('code', '')
    tokens = scan(code)
    token_list = [str(token) for token in tokens]
    return jsonify(token_list)

if __name__ == '__main__':
    app.run(debug=True)
