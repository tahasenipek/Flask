#flask api

from flask import Flask, jsonify, request, Response, abort
from flask_cors import CORS 
from datetime import datetime, timedelta 
import random

endpointroot = '/api'



app = Flask(__name__)
CORS(app)


ip_request_count = {}

# Bir IP'ye izin verilen maksimum istek sayısı
max_requests_per_minute = 70

# İstek geldiğinde çağrılan middleware fonksiyonu

# --------------------------------------- # MODELS # ---------------------------------------------------- #

matches = [
    {'match_id': '1', 'username': 'user1', 'score': '12', 'win': 'true'},
	{'match_id': '2', 'username': 'user2', 'score': '12', 'win': 'true'},
	{'match_id': '3', 'username': 'user3', 'score': '12', 'win': 'true'},
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
	'friens' : friends,
	'password' : '123',
	'language' : 'tr',
	'matches' : matches,
},
{
	'username' : 'mehmet',
	'picture' : 'https://picsum.photos/200/500',
	'online_status' : False,
	'friens' : friends,
	'password' : '1234',
	'language' : 'tr',
	'tournament-nickname': 'null',
	'matches' : matches,

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
		print()
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
	try:
		data = request.get_json()
		nickname = data['nickname']
		token = data['token']

		print(nickname)
		print(token)

		response_data = {
			'success': True,
		}

		return jsonify(response_data), 201
	except:
		return jsonify({'response': 'error'}), 500
	
	



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



@app.route('/update-profile', methods=['POST'])
def update_profile():
    try:
        data = request.get_json()
        user_id = data.get('id')
        new_username = data.get('username')
        new_password = data.get('password')
        new_language = data.get('language')

        for user in users:
            if user['id'] == user_id:
                user['username'] = new_username
                user['password'] = new_password
                user['language'] = new_language

                return jsonify({'success': True,})

        return jsonify({'success': False, 'message': 'User not found'}), 404
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'message': 'Error updating profile'}), 500






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2700)