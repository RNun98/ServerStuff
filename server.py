#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cherrypy
import os


config = {
    'global' : {
        'server.socket_host' : '127.0.0.1',
        'server.socket_port' : 8080
    }
}

class App(object):

    @cherrypy.expose
    def upload(self, ufile):
        # Either save the file to the directory where server.py is
        # or save the file to a given path:
        # upload_path = '/path/to/project/data/'
        upload_path = os.path.dirname(__file__)

        # Save the file to a predefined filename
        # or use the filename sent by the client:
        # upload_filename = ufile.filename
        upload_filename = 'saved.txt'

        upload_file = os.path.normpath(
            os.path.join(upload_path, upload_filename))
        
        size = 0

        path_to_ufile = os.path.abspath(ufile.filename)

        # upload file: /Users/robinsonnunez/Desktop/MISC./serverProject/saved.txt
        # ufile: /Users/robinsonnunez/Desktop/MISC./serverProject/alphabet.txt 
        """
        alphabet.txt
        
        Dummy text
        """
        
        with open(upload_file, 'wb') as out:
            while True:
                try:
                    data_byte_array = self.create_byte_array(path_to_ufile)
                except:
                    raise

                out.write(data_byte_array)
        return "Hello"

    def create_byte_array(self, path_to_ufile):
        """
        Parse a file and create a byte array from the file
        """
        # Not reading from the ufile correctly
        data = open(path_to_ufile, 'rb')
        
        if data is None:
            return Exception

        byte_array_data = []
        data_lines = data.readlines()
        for line in data_lines:
            byte_array_data.append(line)
        
        byte_array = bytearray(data.readlines())
        return byte_array
            


        
if __name__ == '__main__':
    cherrypy.quickstart(App(), '/', config)