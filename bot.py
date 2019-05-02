# encoding: utf-8
import logging

class Bot(object):
    def __init__(self, send_callback, users_dao, tree):
        self.send_callback = send_callback
        self.users_dao = users_dao
        self.tree = tree
    
    def handle(self, user_id, user_message):
        logging.info("Se invocó el método handle")
        #obtener el historial de ecentos/mensajes
        #en funcion al mensaje escrito por el usuario (y tree)
        response_text = self.tree['say']
        possible_answers = self.tree['answers'].keys()
        self.send_callback(user_id, response_text, possible_answers)