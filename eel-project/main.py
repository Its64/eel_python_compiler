from io import StringIO
import sys
import eel

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

@eel.expose
def get_code(code):
    with Capturing() as output:
      try:
          exec(code)
      except:
          print("Error!")
  
    return output

eel.init("web")
eel.start("index.html")