from datetime import datetime

from flask import Flask, render_template,request,redirect

app = Flask(__name__)

# 플레이어 정보
player_info = {
    'player1': {
        'name': 'player1',
        'turn_order': 1
    },
    'player2': {
        'name': 'player2',
        'turn_order': 2
    },
    # 추가적인 플레이어들의 정보를 계속해서 추가할 수 있음
}

# 카드 정보
card_info = {
        # 추가적인 카드들의 정보를 계속해서 추가할 수 있음
    }

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/post', methods=['POST'])
def post():
    color = request.form['color']
    number = request.form['number']
    order = request.form['order']
    player_name = request.form['player_name']
    # 여기에서 폼 데이터를 사용하여 카드를 추가하거나 처리하는 로직을 구현할 수 있습니다.
    # 예를 들어, 받아온 color와 number를 사용하여 카드를 추가하는 함수를 호출하거나
    # 데이터베이스에 저장할 수 있습니다.
    new_card = {
        f'card{len(card_info) + 1}': {
            'card_number': number,
            'color': color,
            'turn_order': order,
            'owner': player_name
        }
    }   
    
    # card_info 딕셔너리에 새로운 카드를 추가
    card_info.update(new_card)
   #print(card_info)
    print("카드가 성공적으로 제출되었어요!")
    return redirect(f'/{player_name}')
@app.route('/<player_name>', methods=['GET', 'POST'])
def game(player_name):
    card_data_list = []  # 플레이어의 모든 카드 정보를 저장할 빈 리스트 생성
    for card_name, card_data in card_info.items():
        if card_data['owner'] == player_name:  
            card_data_list.append(card_data)  # 플레이어의 카드 정보를 리스트에 추가
    
    return render_template('game.html', card_data_list=card_data_list, player_name=player_name)  # 모든 카드 정보를 전달




@app.route('/about')
def about():
  return render_template('about.html', title='About')
#run
if __name__ == '__main__':
    app.run(debug=True)