from flask import Flask, jsonify
from flask_cors import CORS
import os
import time


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# print route
@app.route('/banana', methods=['GET'])
def print_banana():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Banana/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Banana/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Banana/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Banana/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Banana/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Banana/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Banana/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/bell-pepper', methods=['GET'])
def print_bell_pepper():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/BellPepper/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/BellPepper/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/BellPepper/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/BellPepper/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/BellPepper/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/BellPepper/6.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/bitter-melon', methods=['GET'])
def print_bitter_melon():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/BitterMelon/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/BitterMelon/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/BitterMelon/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/BitterMelon/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/BitterMelon/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/BitterMelon/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/BitterMelon/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/chinese-chive', methods=['GET'])
def print_chinese_chive():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseChive/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseChive/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseChive/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseChive/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseChive/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseChive/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseChive/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/chinese-kale', methods=['GET'])
def print_chinese_kale():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseKale/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseKale/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseKale/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseKale/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseKale/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseKale/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/ChineseKale/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/choy-sum', methods=['GET'])
def print_choy_sum():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Choysum/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Choysum/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Choysum/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Choysum/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Choysum/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Choysum/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Choysum/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/corn', methods=['GET'])
def print_corn():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Corn/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Corn/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Corn/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Corn/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Corn/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Corn/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Corn/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/cucumber', methods=['GET'])
def print_cucumber():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Cucumber/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Cucumber/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Cucumber/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Cucumber/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Cucumber/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Cucumber/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Cucumber/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/egg-plant', methods=['GET'])
def print_egg_plant():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Eggplant/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Eggplant/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Eggplant/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Eggplant/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Eggplant/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Eggplant/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Eggplant/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/okra', methods=['GET'])
def print_okra():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Okra/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Okra/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Okra/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Okra/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Okra/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Okra/6.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/papaya', methods=['GET'])
def print_papaya():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Papaya/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Papaya/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Papaya/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Papaya/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Papaya/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Papaya/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Papaya/7.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Papaya/8.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/potato', methods=['GET'])
def print_potato():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Potato/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Potato/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Potato/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Potato/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Potato/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Potato/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Potato/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/rice', methods=['GET'])
def print_rice():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rice/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rice/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rice/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rice/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rice/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rice/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rice/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/rye', methods=['GET'])
def print_rye():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rye/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rye/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rye/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rye/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rye/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rye/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Rye/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/snow-pea', methods=['GET'])
def print_snow_pea():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SnowPea/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SnowPea/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SnowPea/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SnowPea/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SnowPea/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SnowPea/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SnowPea/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/spinach', methods=['GET'])
def print_spinach():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Spinach/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Spinach/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Spinach/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Spinach/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Spinach/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Spinach/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Spinach/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/sweet-potato', methods=['GET'])
def print_sweet_potato():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SweetPotato/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SweetPotato/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SweetPotato/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SweetPotato/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SweetPotato/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SweetPotato/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/SweetPotato/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/taro', methods=['GET'])
def print_taro():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Taro/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Taro/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Taro/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Taro/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Taro/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Taro/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Taro/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/tomato', methods=['GET'])
def print_tomato():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Tomato/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Tomato/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Tomato/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Tomato/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Tomato/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Tomato/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/Tomato/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

@app.route('/water-spinach', methods=['GET'])
def print_water_spinach():
    response_object = {'status':'success'}
    os.system("lp -o fit-to-page -o orientation-requested=3 print/WaterSpinach/1.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/WaterSpinach/2.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/WaterSpinach/3.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/WaterSpinach/4.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/WaterSpinach/5.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/WaterSpinach/6.jpg")
    time.sleep(30)
    os.system("lp -o fit-to-page -o orientation-requested=3 print/WaterSpinach/7.jpg")
    response_object['message'] = 'Print Order Received'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()