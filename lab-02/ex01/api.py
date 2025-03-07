from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
app = Flask (__name__)

#CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@approute("/api/caesar/encrypt" , methods=[POST])
def caesat_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypt_text})
@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.jsoncipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypt_message': decrypted_text})

#main function if__name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)