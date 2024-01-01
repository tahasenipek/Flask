#flask api

from flask import Flask, jsonify, request, Response, abort
from flask_cors import CORS 
from datetime import datetime, timedelta 
import random

endpointroot = '/api'

global_variable = 0

app = Flask(__name__)
CORS(app)


ip_request_count = {}

# Bir IP'ye izin verilen maksimum istek sayısı
max_requests_per_minute = 70

# İstek geldiğinde çağrılan middleware fonksiyonu

# --------------------------------------- # MODELS # ---------------------------------------------------- #

matches = [
    {'match_id': '1', 'username': 'ahmet', 'score': '12', 'win': 'true'},
	{'match_id': '2', 'username': 'user2', 'score': '12', 'win': 'true'},
	{'match_id': '3', 'username': 'ahmet', 'score': '12', 'win': 'true'},
	{'match_id': '4', 'username': 'user4', 'score': '12', 'win': 'true'},
	{'match_id': '5', 'username': 'user5', 'score': '12', 'win': 'true'},
	{'match_id': '6', 'username': 'ahmet', 'score': '12', 'win': 'true'},
	{'match_id': '7', 'username': 'user7', 'score': '12', 'win': 'true'},
	{'match_id': '8', 'username': 'user8', 'score': '12', 'win': 'true'},
	{'match_id': '9', 'username': 'ahmet', 'score': '12', 'win': 'true'},
	{'match_id': '10', 'username': 'user1', 'score': '12', 'win': 'true'},
	{'match_id': '11', 'username': 'user1', 'score': '12', 'win': 'true'},
	{'match_id': '12', 'username': 'ahmet', 'score': '12', 'win': 'true'},
	{'match_id': '13', 'username': 'user1', 'score': '12', 'win': 'true'},
	{'match_id': '14', 'username': 'ahmet', 'score': '12', 'win': 'true'},
	{'match_id': '15', 'username': 'ahmet', 'score': '12', 'win': 'true'},
	{'match_id': '16', 'username': 'user16', 'score': '12', 'win': 'true'},
	{'match_id': '17', 'username': 'ahmet', 'score': '12', 'win': 'true'},
	{'match_id': '18', 'username': 'user18', 'score': '12', 'win': 'true'},
	{'match_id': '19', 'username': 'user19', 'score': '12', 'win': 'true'},
	{'match_id': '20', 'username': 'ahmet', 'score': '12', 'win': 'true'},
	{'match_id': '21', 'username': 'user21', 'score': '12', 'win': 'true'},
]


friends = [
	{'id': '1', 'username': 'ahmet' , 'online_status': True},
	{'id': '2', 'username': 'mehmet' , 'online_status': False},
	{'id': '1', 'username': 'hasan' , 'online_status': True},
	{'id': '2', 'username': 'orkun' , 'online_status': False},
	{'id': '1', 'username': 'melissa' , 'online_status': True},
	{'id': '2', 'username': 'tarık' , 'online_status': False},
	{'id': '1', 'username': 'ahmet' , 'online_status': True},
	{'id': '2', 'username': 'mehmet' , 'online_status': False},
	{'id': '1', 'username': 'hasan' , 'online_status': True},
	{'id': '2', 'username': 'orkun' , 'online_status': False},
	{'id': '1', 'username': 'melissa' , 'online_status': True},
	{'id': '2', 'username': 'tarık' , 'online_status': False},
]
user_profile = [{
	
	'username' : 'ahmet',
	'picture' : 'https://picsum.photos/200/300',
	'online_status' : True,
	'friends' : friends,
	'password' : '123',
	'language' : 'tr',
	'matches' : matches,
	'token' : '685578',
},
{
	'username' : 'mehmet',
	'online_status' : False,
	'friends' : friends,
	'password' : '1234',
	'language' : 'tr',
	'tournament-nickname': 'null',
	'matches' : matches,
	'token' : '685579',
	'picture' : 'https://picsum.photos/200/300',
},
]


users = [
    {'username': 'user1'},
    {'username': 'user2'},
    {'username': 'user3'},
	{'username': 'selam'},
	{'username': 'ahmet'},
	{'username': 'mehmet'},
	{'username': 'taha'},
	{'username': 'ahmet2'},
	{'username': 'kemal'},
	{'username': 'taha2'},
	{'username': 'caner'},
	{'username': 'selim'},
	{'username': 'mahmut'},
	{'username': 'ahmet4'},
	{'username': 'ahmet2'},
	{'username': 'kemal'},
	{'username': 'taha2'},
	{'username': 'caner'},
	{'username': 'selim'},
	{'username': 'mahmut'},
	{'username': 'ahmet4'},
	{'username': 'taha2'},
	{'username': 'caner'},
	{'username': 'selim'},
	{'username': 'mahmut'},
	{'username': 'ahmet4'},
	{'username': 'ahmet2'},
	{'username': 'kemal'},
	{'username': 'taha2'},
	{'username': 'caner'},
	{'username': 'selim'},
	{'username': 'mahmut'},
	{'username': 'ahmet4'},
	{'username': 'taha2'},
	{'username': 'caner'},
	{'username': 'selim'},
	{'username': 'mahmut'},
	{'username': 'ahmet4'},
	{'username': 'ahmet2'},
	{'username': 'kemal'},
	{'username': 'taha2'},
	{'username': 'caner'},
	{'username': 'selim'},
	{'username': 'mahmut'},
	{'username': 'ahmet4'},
]




# --------------------------------------- # MODELS FİNİSH # ---------------------------------------------------- #







@app.route(endpointroot + "/register", methods=['POST'])
def register():

	try:
		data = request.get_json()
		username = data['username']
		password = data['password']

		print(username)
		print(password)

		response_data = {
			'success': True,
		}

		return jsonify(response_data), 201
	except:
		return jsonify({'response': 'error'}), 500


@app.route(endpointroot + "/login", methods=['POST'])
def login():
	print("login")
	try:
		data = request.get_json()
		username = data['username']
		password = data['password']

		print(username)
		print(password)

		response_data = {
			'success': True,
			'access_token':  random.randint(100000, 999999),
			'language': 'tr',
		}

		return jsonify(response_data), 201
	except:
		return jsonify({'response': 'error'}), 500


@app.route(endpointroot + "/get-user-profile", methods=['GET'])
def get_user_profile():

	try:
		data = request.get_json()
		username = data['username']

		print(username)

		response_data = {
			'success': True,
			'user_profile': user_profile[0]
		}

		return jsonify(response_data), 201
	except:
		return jsonify({'response': 'error'}), 500


@app.route(endpointroot + "/change-picture", methods=['POST'])
def change_picture():

	try:
		data = request.get_json()
		access_token = data['access_token']
		picture = data['file']

		print(picture)

		response_data = {
			'success': True,
		}

		return jsonify(response_data), 201
	except:
		return jsonify({'response': 'error'}), 500



@app.route(endpointroot + "/search", methods=['POST'])
def search_users():

	try:
		data = request.get_json()
		search_query = data['searchQuery']
		if search_query:
			matching_users = [
                {
                    'username': user['username'],
                    'online_status': user['online_status']
                }
                for user in user_profile
                if search_query in user['username'].lower()
            ]
		else:
			matching_users = []
		Response = {
			'success': True,
			'users': matching_users
		}
		return jsonify(Response), 201
	except:
		return jsonify({'response': 'error'}), 500

	
@app.route(endpointroot + "/putTheNick" , methods=['POST'])
def putTheNick():
	global global_variable

	try:
		
		global_variable += 1
		data = request.get_json()
		nickname = data['nickname']
		token = data['token']

		print(nickname)
		print(token)

		response_data = {
			'success': True,
			'int': global_variable,
		}

		return jsonify(response_data), 201
	except:
		return jsonify({'response': 'error'}), 500
	
	
@app.route(endpointroot + "/startTournament" , methods=['POST'])
def startTournament():
	global global_variable
	try:
		print(global_variable)
		if global_variable == 4:
			print(global_variable)
			data = request.get_json()
			token = data['token']

			print(data)
			print(token)
			print(global_variable)
			if (token == '126795'):
				print(global_variable)
				print(token)
				print(data)
				response_data = {
					'success': True,
					'tournament': True,
					'int': global_variable,
					'token' : '126795',
				}
			return jsonify(response_data), 201
		else:
			print(global_variable),
			response_data = {
				'success': False,
				'tournament': '0',
				'int': global_variable,
				'token' : '126795',
			}
			return jsonify(response_data), 201
	except:
		return jsonify({'response': 'error'}), 500

126795
@app.route(endpointroot + "/ping" , methods=['GET'])
def ping():
	return jsonify({'response': 'pong!'})


@app.route( endpointroot + "/friendlist", methods=['GET'])
def get_friends():
	
    friends_list = [
		{
			'username': friend['username'],
			'online_status': friend['online_status'],
		} 
		for friend in friends
	]

    return jsonify({'friends': friends_list, 'success': True} )

@app.route(endpointroot+"/ping" , methods=['POST'])
def post_ping():
	data = request.get_json()
	return jsonify(data), 201



@app.route(endpointroot + '/update-profile', methods=['PUT'])
def update_profile():
    try:
        data = request.json

        # Kullanıcı adını güncelle
        user_profile[0]['username'] = data.get('username', user_profile[0]['username'])

        # Şifreyi güncelle
        user_profile[0]['password'] = data.get('password', user_profile[0]['password'])

        # Dil bilgisini güncelle
        user_profile[0]['language'] = data.get('language', user_profile[0]['language'])

        # Başarılı bir şekilde güncelleme gerçekleştirildiyse
        return jsonify({'success': True, 'language': user_profile[0]['language']})

    except Exception as e:
        # Hata durumunda
        return jsonify({'success': False, 'error': str(e)}), 500





@app.route(endpointroot + '/my-photo', methods=['POST'])
def my_photo():
	return jsonify({'photo': user_profile[1]['picture'], 'success': True })


@app.route(endpointroot + '/update-photo', methods=['PUT'])
def update_photo():
	try:
		user_profile[0]['picture'] = 'https://picsum.photos/200/300'
		return jsonify({'success': True}), 201
	except:
		return jsonify({'response': 'error'}), 500
			

@app.route(endpointroot + '/get-profile', methods=['POST'])
def get_profile():
	try:
		data = request.get_json()
		token = data['token']
		

		friends_count = len(user_profile[0]['friends'])
		matches_count = len(user_profile[0]['matches'])
		tournament = '12'

		response_data = {
			'success': True,
			'friends' : False,
			'username': user_profile[0]['username'],
			'friends_count': friends_count,
			'matches_count': matches_count,
			'tournament': tournament,
			'photo': user_profile[0]['picture'],
			'online_status': user_profile[0]['online_status'],
		}
		return jsonify(response_data), 201

	except:
		return jsonify({'response': 'error'}), 500		


@app.route(endpointroot + '/requestgame', methods=['POST'])
def request_game():
	try:
		data = request.get_json()
		print(data)
		gameid = str(random.randint(1000, 9999))
		print(gameid)
		password = str(random.randint(1000, 9999))
		print(password)
		password_p1 = '1234'

		response_data = {
			'success': True,
			'gameid': gameid,
			'password': password,
			"player": "p1",
			'playerpass': password_p1,
		}

		return jsonify(response_data), 201
	except:
		return jsonify({'response': 'error'}), 500
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2700)