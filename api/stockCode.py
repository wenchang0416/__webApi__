from . import api1
import pandas as pd
import json

@api1.route("/stockCode")
def stockCode():
    code_dataframe = pd.read_csv("api/codeSearch.csv")
    code_dataframe1 = code_dataframe[['code','name']]
    all_list = code_dataframe1.values.tolist()
    python_list = [{item[0]:item[1]} for item in all_list]

    return json.dumps(python_list, ensure_ascii=False)


@api1.route("/stockCode/<int:code>")
def stockName(code):    
    code_dataframe = pd.read_csv("api/codeSearch.csv")
    code_dataframe1 = code_dataframe[['code','name']]
    try: 
        name = code_dataframe1.query('code == @code')['name'].values[0]
    except IndexError: 
        return f"抱歉! 股票代號{code}有誤"
    
    return name
    # 
    # return jsonify(python_list)
    # return "<h1>stockcode</h1>"


