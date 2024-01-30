import web

urls = (
    '/(.*)', 'hello world'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World---hello'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()

