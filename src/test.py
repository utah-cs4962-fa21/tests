"""
This file contains the mock framework for testing
"""

import builtins
import io
import sys
import tkinter
import tkinter.font
import unittest
import email
from unittest import mock




class socket:
    URLs = {}
    Requests = {}

    def __init__(self, *args, **kwargs):
        self.request = b""
        self.connected = False

    def connect(self, host_port):
        self.scheme = "http"
        self.host, self.port = host_port
        self.connected = True

    def send(self, text):
        self.request += text
        self.method, self.path, _ = self.request.decode("latin1").split(" ", 2)
        
        if self.method == "POST":
            beginning, self.body = self.request.decode("latin1").split("\r\n\r\n")
            headers = [item.split(": ") for item in beginning.split("\r\n")[1:]]
            assert headers[0][0] == "Content-Length"
            content_length = headers[0][1]

            assert len(self.body) == int(content_length), len(self.body)

    def makefile(self, mode, encoding, newline):
        assert self.connected and self.host and self.port
        if self.port == 80 and self.scheme == "http":
            url = self.scheme + "://" + self.host + self.path
        elif self.port == 443 and self.scheme == "https":
            url = self.scheme + "://" + self.host + self.path
        else:
            url = self.scheme + "://" + self.host + ":" + str(self.port) + self.path
        self.Requests.setdefault(url, []).append(self.request)
        assert self.method == self.URLs[url][0]
        output = self.URLs[url][1]
        if self.URLs[url][2]:
            assert self.body == self.URLs[url][2], (self.body, self.URLs[url][2])
        return io.StringIO(output.decode(encoding).replace(newline, "\n"), newline)

    def close(self):
        self.connected = False

    @classmethod
    def patch(cls):
        return mock.patch("socket.socket", wraps=cls)

    @classmethod
    def respond(cls, url, response, method="GET", body=None):
        cls.URLs[url] = [method, response, body]

    @classmethod
    def last_request(cls, url):
        return cls.Requests[url][-1]

    @classmethod
    def parse_last_request(cls, url):
        raw_request = cls.Requests[url][-1].decode()
        raw_command, raw_headers = raw_request.split('\r\n', 1)
        message = email.message_from_file(io.StringIO(raw_headers))
        headers = dict(message.items())
        headers = {key.lower(): val for key,val in headers.items()}
        command, path, version = raw_command.split(" ", 2)
        return command, path, version, headers

    @classmethod
    def redirect_url(cls, from_url, to_url):
        cls.respond(url=from_url,
                    response=("HTTP/1.0 301 Moved Permanently\r\n" +
                              "Location: {}\r\n" +
                              "\r\n").format(to_url).encode(),
                    method="GET")
class ssl:
    def wrap_socket(self, s, server_hostname):
        assert s.host == server_hostname
        s.scheme = "https"
        return s

    @classmethod
    def patch(cls):
        return mock.patch("ssl.create_default_context", wraps=cls)

class SilentTk:
    def bind(self, event, callback):
        pass

tkinter.Tk = SilentTk

class SilentCanvas:
    def __init__(self, *args, **kwargs):
        pass

    def create_text(self, x, y, text, font=None, anchor=None, fill=None):
        pass

    def create_rectangle(self, x1, y1, x2, y2, width=None, fill=None):
        pass

    def create_line(self, x1, y1, x2, y2):
        pass

    def create_line(self, x1, y1, x2, y2):
        pass

    def create_polygon(self, *args, **kwargs):
        pass

    def pack(self, expand=None, fill=None):
        pass

    def delete(self, v):
        pass

tkinter.Canvas = SilentCanvas

class MockCanvas:
    def __init__(self, *args, **kwargs):
        pass

    def create_text(self, x, y, text, font=None, anchor=None):
        if font or anchor:
            print("create_text: x={} y={} text={} font={} anchor={}".format(
                x, y, text, font, anchor))
        else:
            print("create_text: x={} y={} text={}".format(
                x, y, text))

    def pack(self, expand=None, fill=None):
        pass

    def delete(self, v):
        pass

original_tkinter_canvas = tkinter.Canvas


class resize_event:
    def __init__(self, width, height):
        self.height = height
        self.width = width
    

def patch_canvas():
    tkinter.Canvas = MockCanvas

def unpatch_canvas():
    tkinter.Canvas = original_tkinter_canvas

class MockFont:
    def __init__(self, size=None, weight=None, slant=None, style=None):
        self.size = size
        self.weight = weight
        self.slant = slant
        self.style = style

    def measure(self, word):
        return self.size * len(word)

    def metrics(self, name=None):
        all = {"ascent" : self.size * 0.75, "descent": self.size * 0.25,
            "linespace": self.size}
        if name:
            return all[name]
        return all

    def __repr__(self):
        return "Font size={} weight={} slant={} style={}".format(
            self.size, self.weight, self.slant, self.style)

tkinter.font.Font = MockFont

def errors(f, *args, **kwargs):
    try:
        f(*args, **kwargs)
    except Exception as e:
        return True
    else:
        return False

def breakpoint(name, *args):
    args_str = (", " + ", ".join(["'{}'".format(arg) for arg in args]) if args else "")
    print("breakpoint(name='{}'{})".format(name, args_str))

builtin_breakpoint = builtins.breakpoint

def patch_breakpoint():
    builtins.breakpoint = breakpoint

def unpatch_breakpoint():
    builtins.breakpoint = builtin_breakpoint

class Event:
    def __init__(self, x, y):
        self.x = x
        self.y = y

